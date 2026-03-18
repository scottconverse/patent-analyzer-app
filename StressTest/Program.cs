using System.Diagnostics;
using System.Text;
using PatentAnalyzer.Models;
using PatentAnalyzer.Services;

namespace StressTest;

class Program
{
    static int _passed;
    static int _failed;
    static readonly List<string> _failures = new();

    static async Task<int> Main()
    {
        Console.WriteLine("=== PATENT ANALYZER v1.1 — STRESS TEST ===\n");

        TestConfigEncryptDecrypt();
        TestConfigPath();
        TestPromptTemplates();
        TestHtmlRenderer();
        TestReportExporter();
        TestNarrativeBuilder();
        TestEdgeCaseInputs();
        await TestApiClient();
        await TestFullPipeline();

        Console.WriteLine("\n" + new string('=', 60));
        Console.WriteLine($"RESULTS: {_passed} passed, {_failed} failed, {_passed + _failed} total");
        if (_failures.Count > 0)
        {
            Console.WriteLine("\nFAILURES:");
            foreach (var f in _failures) Console.WriteLine($"  - {f}");
        }
        Console.WriteLine(new string('=', 60));
        return _failed > 0 ? 1 : 0;
    }

    static void TestConfigEncryptDecrypt()
    {
        Console.WriteLine("[TEST 1] Config encrypt/decrypt cycle");
        try
        {
            // Preserve real config
            var originalSettings = ConfigManager.Load();

            var testKey = "sk-ant-test-" + Guid.NewGuid().ToString("N")[..20];
            var settings = new AppSettings { ApiKey = testKey, Model = "claude-haiku-4-5-20251001" };
            ConfigManager.Save(settings);
            var loaded = ConfigManager.Load();

            Assert("API key survives encrypt/decrypt", loaded.ApiKey == testKey);
            Assert("Model preserved", loaded.Model == "claude-haiku-4-5-20251001");

            var configDir = Path.Combine(
                Environment.GetFolderPath(Environment.SpecialFolder.LocalApplicationData), "PatentAnalyzer");
            var configPath = Path.Combine(configDir, "config.json");
            if (File.Exists(configPath))
            {
                var raw = File.ReadAllText(configPath);
                Assert("API key encrypted on disk (dpapi: prefix)", raw.Contains("dpapi:"));
                Assert("Plaintext key NOT on disk", !raw.Contains(testKey));
            }
            else Fail("Config file not found at: " + configPath);

            // Restore real config
            ConfigManager.Save(originalSettings);
            var verify = ConfigManager.Load();
            Assert("Original key restored after test", verify.ApiKey == originalSettings.ApiKey);
        }
        catch (Exception ex) { Fail($"Crashed: {ex.Message}"); }
    }

    static void TestConfigPath()
    {
        Console.WriteLine("[TEST 2] Config uses AppData path");
        try
        {
            var dir = Path.Combine(
                Environment.GetFolderPath(Environment.SpecialFolder.LocalApplicationData), "PatentAnalyzer");
            Assert("Config dir under LocalAppData", dir.Contains("AppData"));
            Assert("Config dir exists", Directory.Exists(dir));
        }
        catch (Exception ex) { Fail($"Crashed: {ex.Message}"); }
    }

    static void TestPromptTemplates()
    {
        Console.WriteLine("[TEST 3] Prompt templates — all 6 stages + audit fixes");
        try
        {
            for (int i = 1; i <= 6; i++)
            {
                var prompt = PromptTemplates.GetSystemPrompt(i);
                Assert($"Stage {i} non-empty and > 500 chars", !string.IsNullOrWhiteSpace(prompt) && prompt.Length > 500);
                Assert($"Stage {i} has MANDATORY RULES", prompt.Contains("MANDATORY RULES"));
            }
            Assert("Fix 7: 50-word threshold", PromptTemplates.GetSystemPrompt(1).Contains("fewer than 50 words"));
            Assert("Fix 1: web search fallback", PromptTemplates.GetSystemPrompt(2).Contains("Web Search Availability Check"));
            Assert("Fix 2: UNVERIFIED marking", PromptTemplates.GetSystemPrompt(2).Contains("UNVERIFIED"));
            Assert("Fix 4: word count target", PromptTemplates.GetSystemPrompt(2).Contains("1,500-3,000 words"));
            Assert("Fix 3: verification note", PromptTemplates.GetSystemPrompt(3).Contains("Verification note"));
            Assert("Fix 3: legal caveat", PromptTemplates.GetSystemPrompt(3).Contains("training data and may not reflect"));
            Assert("Fix 5: benefits from", PromptTemplates.GetSystemPrompt(4).Contains("benefits from web search"));
            Assert("Fix 6: cost date stamp", PromptTemplates.GetSystemPrompt(5).Contains("approximate as of 2025"));
            Assert("Fix 6: USPTO URL", PromptTemplates.GetSystemPrompt(5).Contains("uspto.gov"));

            try { PromptTemplates.GetSystemPrompt(0); Fail("Stage 0 should throw"); }
            catch (ArgumentOutOfRangeException) { Assert("Stage 0 throws", true); }
            try { PromptTemplates.GetSystemPrompt(7); Fail("Stage 7 should throw"); }
            catch (ArgumentOutOfRangeException) { Assert("Stage 7 throws", true); }
        }
        catch (Exception ex) { Fail($"Crashed: {ex.Message}"); }
    }

    static void TestHtmlRenderer()
    {
        Console.WriteLine("[TEST 4] HTML renderer");
        try
        {
            var md = "# Heading\n\n**Bold** and a table:\n\n| A | B |\n|---|---|\n| 1 | 2 |";
            var full = PatentAnalyzer.Services.HtmlRenderer.RenderToHtml(md);
            Assert("DOCTYPE present", full.Contains("<!DOCTYPE html>"));
            Assert("Heading rendered", full.Contains("<h1"));
            Assert("Table rendered", full.Contains("<table>"));
            Assert("Dark theme CSS", full.Contains("#0D1117"));

            var body = PatentAnalyzer.Services.HtmlRenderer.RenderBodyHtml(md);
            Assert("Body has no DOCTYPE", !body.Contains("<!DOCTYPE"));
            Assert("Body has content", body.Contains("Heading") && body.Length > 50);

            Assert("Empty input renders", PatentAnalyzer.Services.HtmlRenderer.RenderToHtml("").Contains("<!DOCTYPE"));

            var large = new StringBuilder();
            for (int i = 0; i < 200; i++) large.AppendLine($"## Section {i}\n\nText.\n");
            Assert("Large render OK", PatentAnalyzer.Services.HtmlRenderer.RenderToHtml(large.ToString()).Length > 10000);
        }
        catch (Exception ex) { Fail($"Crashed: {ex.Message}"); }
    }

    static void TestReportExporter()
    {
        Console.WriteLine("[TEST 5] Report exporter");
        try
        {
            var testDir = Path.Combine(Path.GetTempPath(), $"PA-Test-{Guid.NewGuid():N}");
            var result = new AnalysisResult
            {
                Input = new InventionInput { Title = "Test / <Special> & Chars" },
                StartedAt = DateTime.Now.AddMinutes(-2), CompletedAt = DateTime.Now,
                FinalReport = "# Report\n\n| Risk | Score |\n|------|-------|\n| §101 | 45 |"
            };
            result.Stages.Add(new StageResult
            {
                StageNumber = 1, StageName = "Technical Intake", Status = StageStatus.Complete,
                OutputText = "Stage 1 output.", Model = "test",
                StartedAt = DateTime.Now.AddMinutes(-2), CompletedAt = DateTime.Now.AddMinutes(-1)
            });

            var saved = ReportExporter.SaveAll(result, testDir);
            var files = Directory.GetFiles(saved);
            Assert("Dir created", Directory.Exists(saved));
            Assert(".md exists", files.Any(f => f.EndsWith(".md") && f.Contains("Report")));
            Assert(".html exists", files.Any(f => f.EndsWith(".html")));
            Assert("Stage file exists", files.Any(f => f.Contains("Stage-01")));
            Assert("XSS-safe title", !File.ReadAllText(files.First(f => f.EndsWith(".html"))).Contains("<title>Test / <Special>"));
            Assert("Sanitized folder", !Path.GetFileName(saved).Contains('<'));
            Directory.Delete(testDir, recursive: true);
        }
        catch (Exception ex) { Fail($"Crashed: {ex.Message}"); }
    }

    static void TestNarrativeBuilder()
    {
        Console.WriteLine("[TEST 6] Narrative builder");
        try
        {
            var full = new InventionInput
            {
                Title = "W", Description = "D", ProblemSolved = "P", HowItWorks = "H",
                AiComponents = "A", ThreeDPrintComponents = "T", WhatIsNovel = "N",
                CurrentAlternatives = "C", WhatIsBuilt = "B", WhatToProtect = "I", AdditionalNotes = "X"
            };
            Assert("All fields present", full.ToNarrative().Contains("Additional Notes"));
            Assert("Bold labels", full.ToNarrative().Contains("**Invention Title:**"));
            Assert("Minimal skips empties", !new InventionInput { Title = "M", Description = "D" }.ToNarrative().Contains("AI"));
            Assert("Empty → empty", string.IsNullOrWhiteSpace(new InventionInput().ToNarrative()));
        }
        catch (Exception ex) { Fail($"Crashed: {ex.Message}"); }
    }

    static void TestEdgeCaseInputs()
    {
        Console.WriteLine("[TEST 7] Edge cases");
        try
        {
            Assert("Unicode", new InventionInput { Title = "智能 🚀", Description = "D" }.ToNarrative().Contains("智能"));
            Assert("100K chars", new InventionInput { Title = "L", Description = new string('A', 100_000) }.ToNarrative().Length > 100_000);
            Assert("Unicode HTML", PatentAnalyzer.Services.HtmlRenderer.RenderToHtml("# 智能 🚀").Contains("智能"));
        }
        catch (Exception ex) { Fail($"Crashed: {ex.Message}"); }
    }

    static async Task TestApiClient()
    {
        Console.WriteLine("[TEST 8] Live API call");
        var settings = ConfigManager.Load();
        if (string.IsNullOrWhiteSpace(settings.ApiKey)) { Console.WriteLine("    SKIPPED — no key"); return; }

        try
        {
            using var client = new AnthropicClient(settings.ApiKey);
            var chunks = 0;
            var sw = Stopwatch.StartNew();
            var result = await client.StreamMessageAsync(
                "Reply with exactly: TEST_OK", "Ping",
                settings.Model, 100, false, 0, _ => chunks++);
            sw.Stop();

            Assert("Got response", !string.IsNullOrWhiteSpace(result.Text));
            Assert("Streaming worked", chunks > 0);
            Assert("Contains TEST_OK", result.Text.Contains("TEST_OK"));
            Assert("Under 30s", sw.ElapsedMilliseconds < 30_000);
            Console.WriteLine($"    {result.Text.Trim()} | {chunks} chunks | {sw.ElapsedMilliseconds}ms");
        }
        catch (Exception ex) { Fail($"API: {ex.Message}"); }
    }

    static async Task TestFullPipeline()
    {
        Console.WriteLine("[TEST 9] Full 6-stage pipeline (several minutes)");
        var settings = ConfigManager.Load();
        if (string.IsNullOrWhiteSpace(settings.ApiKey)) { Console.WriteLine("    SKIPPED — no key"); return; }

        var input = new InventionInput
        {
            Title = "AI Smart Thermostat with Predictive Energy Optimization",
            Description = "Smart thermostat using lightweight ML on ESP32 to predict occupancy and optimize HVAC. Learns from temp, humidity, motion, door sensors plus weather. Reduces energy 15-25%.",
            HowItWorks = "ESP32 4MB PSRAM runs TinyML random forest on 6mo sensor logs. Predicts occupancy 4hrs ahead in 15min intervals. Rule engine to HVAC commands. Weather via WiFi. REST API for mobile app.",
            WhatIsNovel = "On-device occupancy prediction (no cloud). Door sensor + motion decay curves for departure prediction."
        };

        var sw = Stopwatch.StartNew();
        try
        {
            var runner = new PipelineRunner(settings);
            runner.OnStageStart += (n, name) => Console.WriteLine($"    Stage {n}/6: {name}...");
            runner.OnStageComplete += (n, r) =>
                Console.WriteLine($"    Stage {n} done — {r.DurationSeconds:F0}s, {r.OutputText.Length:N0} chars, web:{(r.WebSearchUsed ? "Y" : "N")}");
            runner.OnStatus += s => { if (s.Contains("Searching") || s.Contains("Rate") || s.Contains("Retry")) Console.WriteLine($"      {s}"); };

            var result = await runner.RunAsync(input);
            sw.Stop();

            Assert("Completed", result.CompletedAt != null);
            Assert("6 stages", result.Stages.Count == 6);
            Assert("All complete", result.Stages.All(s => s.Status == StageStatus.Complete));
            Assert("Report non-empty", !string.IsNullOrWhiteSpace(result.FinalReport));
            Assert("Report > 2000 chars", result.FinalReport.Length > 2000);

            for (int i = 1; i <= 6; i++)
                Assert($"Stage {i} output", result.Stages.Any(s => s.StageNumber == i && s.OutputText.Length > 100));

            var rpt = result.FinalReport;
            Assert("Has Executive Summary", rpt.Contains("Executive Summary") || rpt.Contains("executive"));
            Assert("Has Prior Art", rpt.Contains("Prior Art") || rpt.Contains("prior art"));
            Assert("Has §101", rpt.Contains("§101") || rpt.Contains("101"));
            Assert("Has Plain-English Summary", rpt.Contains("Plain-English") || rpt.Contains("Plain English") || rpt.Contains("plain"));
            Assert("Has disclaimer", rpt.Contains("not constitute legal advice") || rpt.Contains("attorney-client"));

            var testDir = Path.Combine(Path.GetTempPath(), $"PA-Pipeline-{Guid.NewGuid():N}");
            var saved = ReportExporter.SaveAll(result, testDir);
            Assert("Export produced files", Directory.GetFiles(saved).Length >= 4);

            Console.WriteLine($"\n    === PIPELINE COMPLETE ===");
            Console.WriteLine($"    Total: {sw.Elapsed.TotalMinutes:F1} min | Report: {result.FinalReport.Length:N0} chars");
            foreach (var s in result.Stages)
                Console.WriteLine($"    Stage {s.StageNumber}: {s.DurationSeconds:F0}s | {s.OutputText.Length:N0} chars | {s.Model} | web:{(s.WebSearchUsed ? "Y" : "N")}");

            Directory.Delete(testDir, recursive: true);
        }
        catch (Exception ex) { sw.Stop(); Fail($"Pipeline at {sw.Elapsed.TotalSeconds:F0}s: {ex.Message}"); }
    }

    static void Assert(string name, bool cond)
    {
        if (cond) { Console.WriteLine($"  PASS: {name}"); _passed++; }
        else { Console.WriteLine($"  FAIL: {name}"); _failed++; _failures.Add(name); }
    }

    static void Fail(string name)
    { Console.WriteLine($"  FAIL: {name}"); _failed++; _failures.Add(name); }
}
