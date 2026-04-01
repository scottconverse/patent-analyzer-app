# Contributing to Patent Analyzer

Thank you for your interest in improving Patent Analyzer.

## Prerequisites

- Windows 10/11 (x64)
- .NET 8 SDK
- Visual Studio 2022 (recommended) or VS Code with C# extension

## Setup

1. Clone the repository
2. Open `PatentAnalyzer.sln` in Visual Studio
3. Build the solution (Ctrl+Shift+B)
4. Run the application (F5)

## Project Structure

```
PatentAnalyzer/
  App.xaml              — Application entry point
  MainWindow.xaml       — Main UI (WPF)
  Models/               — Data models
  Services/
    AnthropicClient.cs  — API streaming client
    PipelineRunner.cs   — 6-stage orchestrator
    PromptTemplates.cs  — All embedded prompts
    ReportExporter.cs   — HTML/Markdown export
    HtmlRenderer.cs     — Markdown to HTML
    ConfigManager.cs    — Settings + DPAPI encryption
```

## How to Contribute

### Reporting Issues
Use [GitHub Issues](https://github.com/scottconverse/patent-analyzer-app/issues)

### Submitting Changes
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Build and test locally
5. Submit a pull request

### Important Guidelines

**Prompt Content:** All prompts in `PromptTemplates.cs` are licensed under CC BY-SA 4.0 and must retain all legal disclaimers. See `LICENSE-PROMPTS`.

**Legal Disclaimers:** Never remove or weaken embedded disclaimers. The AI must always be positioned as a research assistant, not a legal advisor.

**API Key Security:** Never commit API keys or credentials. The app uses DPAPI encryption for local storage.

## License

Application code is licensed under MIT. Prompt content is licensed under CC BY-SA 4.0 with UPL disclaimer retention requirements.
