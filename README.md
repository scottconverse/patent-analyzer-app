# Patent Analyzer

**AI-Powered Patent Feasibility Analysis Tool for Inventors**

**Version 1.1.0** — March 2026

A standalone Windows desktop application that takes an invention idea and runs a comprehensive 6-stage patent analysis pipeline using the Anthropic Claude API. Produces a professional report covering prior art, patentability assessment, and IP strategy — with special depth on AI/ML and 3D printing inventions.

---

## What It Does

You describe your invention. The app runs 6 analysis stages automatically, one after another, streaming results in real time:

| Stage | Name | What It Does |
|-------|------|-------------|
| 1 | **Technical Intake** | Restates your idea in precise patent-ready technical language |
| 2 | **Prior Art Search** | Searches patents, papers, products, and GitHub for existing work (uses web search) |
| 3 | **Patentability Analysis** | Full §101/§102/§103/§112 analysis with examiner rejection simulation |
| 4 | **Deep Dive Analysis** | Specialized deep analysis of the invention's most patentable and riskiest elements |
| 5 | **IP Strategy** | Filing recommendations, cost estimates, claim directions, trade secret boundaries |
| 6 | **Final Report** | Assembles everything into one comprehensive patent analysis report |

**Output:** A comprehensive Markdown + HTML report saved automatically, plus individual stage outputs.

---

## Quick Start

### Prerequisites

- **Windows 10/11** (64-bit)
- **Anthropic API Key** — [Get one here](https://console.anthropic.com/)

That's it. The app is a self-contained single-file executable — no .NET runtime or SDK installation required.

### Download & Run

1. Download `PatentAnalyzer.exe` from the [latest release](https://github.com/scottconverse/patent-analyzer-app/releases)
2. Run it — no installer needed

### First Launch

1. Enter your Anthropic API key in the Settings tab
2. Choose your model (Haiku is the default and works great)
3. Click **Save Settings**
4. Describe your invention in the Analysis tab
5. Click **Run Full Analysis**
6. Watch the analysis stream in real time across all 6 stages
8. Find your report auto-saved in `Documents\PatentAnalyzer\output\`

---

## Publish as Standalone .exe

To create a single-file executable that runs without .NET installed:

```bash
dotnet publish -c Release -r win-x64 --self-contained true -p:PublishSingleFile=true
```

The executable will be in:
```
PatentAnalyzer\bin\Release\net8.0-windows\win-x64\publish\PatentAnalyzer.exe
```

---

## Project Structure

```
PatentAnalyzer/
├── PatentAnalyzer.sln              # Visual Studio solution file
├── README.md                       # This file
├── LICENSE                         # MIT License
│
└── PatentAnalyzer/                 # Main project
    ├── PatentAnalyzer.csproj       # Project file (.NET 8, WPF)
    ├── app.manifest                # DPI awareness, UAC, Windows compatibility
    ├── App.xaml / App.xaml.cs      # Application entry point, theme resources
    ├── MainWindow.xaml             # Main UI layout (XAML + WebView2)
    ├── MainWindow.xaml.cs          # UI logic, event handlers, pipeline orchestration
    │
    ├── Models/
    │   └── AnalysisModels.cs       # Data models: InventionInput, StageResult,
    │                               #   AnalysisResult, AppSettings
    │
    └── Services/
        ├── AnthropicClient.cs      # HTTP client for Anthropic Messages API
        │                           #   with SSE streaming + retry logic
        ├── PipelineRunner.cs       # 6-stage pipeline orchestrator with
        │                           #   callbacks for progress/streaming
        ├── PromptTemplates.cs      # All system prompts for each stage
        │                           #   (derived from patent-attorney skill)
        ├── ReportExporter.cs       # Saves reports as Markdown + styled HTML
        ├── HtmlRenderer.cs         # Markdown → styled HTML for WebView2
        └── ConfigManager.cs        # Config persistence + DPAPI key encryption
```

---

## Configuration

Settings are saved to `%LocalAppData%\PatentAnalyzer\config.json`. Your API key is encrypted at rest using Windows DPAPI — it is never stored in plaintext.

| Setting | Default | Description |
|---------|---------|-------------|
| `apiKey` | (none) | Your Anthropic API key |
| `model` | `claude-haiku-4-5-20251001` | Model for analysis stages |
| `researchModel` | (empty) | Optional cheaper model for prior art search (Stage 2) |
| `outputDirectory` | `Documents\PatentAnalyzer\output` | Where reports are saved |
| `interStageDelaySeconds` | `5` | Pause between stages (rate limit protection) |
| `maxTokens` | `32000` | Max output tokens per stage |

### Model Recommendations

| Model | Best For | Typical Cost per Full Analysis |
|-------|----------|-------------------------------|
| **claude-haiku-4-5-20251001** | Default — fast, affordable, tuned for this app | ~$0.75-1.50 |
| **claude-sonnet-4-20250514** | Alternative if you want to experiment | ~$3-6 |
| **claude-opus-4-20250514** | Maximum quality (expensive) | ~$10-20 |

**Tip:** Haiku is the recommended model. The app's prompts are tuned specifically for it. A full 6-stage analysis typically costs $0.75–$1.50 depending on invention complexity and web search depth.

---

## Output Files

Each analysis creates a timestamped folder in your output directory:

```
2026-03-17_1430_My-Invention/
├── 2026-03-17_1430_Patent-Analysis-Report.md     # Final report (Markdown)
├── 2026-03-17_1430_Patent-Analysis-Report.html   # Final report (styled HTML — printable)
├── 2026-03-17_1430_Stage-01_Technical-Intake.md
├── 2026-03-17_1430_Stage-02_Prior-Art-Search.md
├── 2026-03-17_1430_Stage-03_Patentability-Analysis.md
├── 2026-03-17_1430_Stage-04_Deep-Dive-Analysis.md
├── 2026-03-17_1430_Stage-05_IP-Strategy.md
├── 2026-03-17_1430_Stage-06_Comprehensive-Report.md
└── 2026-03-17_1430_analysis-summary.md           # Metadata and timing
```

The HTML report is styled for professional presentation and printing.

---

## What the Analysis Covers

### For All Inventions
- Technical restatement in patent-ready language
- Prior art search across patents, papers, products, and open source
- Full patentability assessment (§101, §102, §103, §112)
- Examiner rejection simulation
- Filing strategy (provisional vs. non-provisional, timing, costs)
- Claim direction recommendations
- Documentation checklist

### For AI / ML Inventions (Special Depth)
- Patent zone classification (strong vs. red-flag categories)
- Alice/Mayo §101 deep analysis specific to AI
- Current USPTO AI guidance and Federal Circuit decisions
- AI claim framing strategy (system vs. method vs. CRM)
- Trade secret vs. patent boundary analysis for algorithms

### For 3D Printing Inventions (Special Depth)
- Design patent vs. utility patent analysis
- Category classification (geometry, process, material, software, post-processing)
- 3D printing patent landscape search (Stratasys, 3D Systems, HP, etc.)
- Design patent claiming strategy (broken/solid lines, breadth)
- Combined AI + 3D printing opportunities

---

## What's New in v1.1

- **WebView2 rendering** — Replaced the legacy IE WebBrowser control with Microsoft Edge WebView2. Modern CSS, proper table rendering, no memory leaks.
- **Encrypted API key** — Your Anthropic API key is now encrypted at rest using Windows DPAPI. Never stored in plaintext.
- **Config moved to AppData** — Settings saved to `%LocalAppData%\PatentAnalyzer\` instead of next to the exe. Survives single-file publish. Auto-migrates from v1.0.
- **DPI awareness** — Per-monitor DPI scaling via `app.manifest`. Crisp rendering on high-DPI displays.
- **Graceful shutdown** — Closing the window mid-analysis now cancels the pipeline and cleans up all resources.
- **Input validation** — Warns on extremely long input (50K+ characters) that could exceed API limits.
- **Accessibility** — All input fields have `AutomationProperties.Name` for screen readers.
- **API key masking** — Settings dialog uses a PasswordBox instead of a plain text field.
- **Prompt improvements** — All 7 reliability fixes from the prompt system audit ported to the embedded prompts (web search fallback, URL verification, legal caveats, cost date stamps, input threshold, truncation safeguards).

---

## Legal Disclaimer

This tool provides **strategic patent-analysis support**, not legal advice. The analysis:

- Does **not** create an attorney-client relationship
- Does **not** constitute a formal patentability or freedom-to-operate opinion
- Should **not** be relied upon as a substitute for engagement with a registered patent attorney
- Is intended to help inventors understand the patent landscape before investing in formal legal work

**Always consult a registered patent attorney before filing.**

---

## Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| `Microsoft.Web.WebView2` | 1.0.3856.49 | Chromium-based HTML rendering for output and reports |
| `System.Text.Json` | 8.0.5 | JSON serialization for API + config |
| `Markdig` | 0.37.0 | Markdown → HTML conversion for reports |

No Anthropic SDK dependency — uses raw `HttpClient` with SSE streaming for maximum compatibility and transparency. The WebView2 runtime is pre-installed on Windows 10 (April 2021+) and Windows 11.

---

## Building from Source

### Requirements
- .NET 8 SDK
- Visual Studio 2022+ (optional, for XAML designer) or VS Code with C# extension
- Windows 10/11

### Steps

```bash
# 1. Open solution in Visual Studio
#    File → Open → PatentAnalyzer.sln

# 2. Or build from command line
dotnet restore
dotnet build

# 3. Run
dotnet run --project PatentAnalyzer

# 4. Publish standalone .exe
dotnet publish -c Release -r win-x64 --self-contained true -p:PublishSingleFile=true
```

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| "API key is invalid" | Check your key at console.anthropic.com. The app encrypts your key — if you moved the app to a new machine, re-enter the key in Settings. |
| "WebView2 Runtime Required" | The app needs the Edge WebView2 Runtime. It's pre-installed on most Windows 10/11 systems. If missing, run Windows Update or download from [Microsoft](https://developer.microsoft.com/en-us/microsoft-edge/webview2/). |
| Rate limit errors | The app retries automatically (3 attempts with progressive backoff). Increase inter-stage delay in Settings if needed. |
| Build errors | Make sure you have .NET 8 SDK: `dotnet --version` should show 8.x |
| App won't start | Run from command line to see errors: `dotnet run --project PatentAnalyzer` |
| Reports not saving | Check output directory in Settings exists and you have write permission. Default: `Documents\PatentAnalyzer\output\` |
| Settings lost after update | v1.1 moved config to `%LocalAppData%\PatentAnalyzer\`. Settings from v1.0 are migrated automatically on first launch. |

---

*Built with the Anthropic Claude API and Microsoft WebView2. Analysis quality depends on the model selected and the detail of your invention description. v1.1.0 — March 2026.*
