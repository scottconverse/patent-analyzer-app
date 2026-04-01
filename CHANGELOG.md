# Changelog

All notable changes to Patent Analyzer will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.2.0] - 2026-04-01

### Changed
- All 6 embedded stage prompts now position the AI as an "AI-powered research assistant" rather than a "patent attorney" or "patent strategist"
- Every stage output now begins with a mandatory disclaimer identifying the output as AI-generated research, not legal advice
- Section titles softened to reflect landscape analysis rather than legal directives:
  - "File or Don't File" is now "Filing Landscape Assessment"
  - "Bottom-Line Recommendation" is now "Overall Landscape Assessment"
  - "Examiner Rejection Simulation" is now "Common Examiner Concerns in This Technology Area"
  - "Freedom-to-Operate Flag" is now "Potential Blocking IP to Discuss with Counsel"
- Assessment labels updated (e.g., "FILE NOW" is now "LANDSCAPE FAVORS FILING")
- Stage 3 now uses Research Findings / Analysis Notes structure
- Conclusions include scope qualifiers acknowledging search limitations
- Stage 6 closing disclaimer expanded

### Added
- Disclaimer footer automatically appended to all HTML and Markdown exports
- LICENSE-PROMPTS file (CC BY-SA 4.0 for embedded prompt content)
- LEGAL_NOTICE.md with comprehensive legal notice
- Section 5.5 (AI Limitations) in Terms of Service
- Active hedging language in analytical conclusions

## [1.1.0] - 2026-03-15

### Added
- WebView2 rendering (replaces legacy IE WebBrowser control)
- Encrypted API key storage using Windows DPAPI
- Config moved to %LocalAppData% (survives single-file publish)
- DPI awareness for high-resolution displays
- Graceful shutdown with pipeline cancellation
- Input validation (warns on 50K+ character input)
- Accessibility improvements (automation properties for screen readers)
- API key masking (PasswordBox)
- 7 prompt reliability fixes from stress test audit

## [1.0.0] - 2026-02-01

### Added
- Initial release: 6-stage patent landscape analysis desktop application
- Real-time streaming output via SSE
- Markdown + styled HTML report export
- Configurable model selection and cost tracking
- Single-file self-contained executable (no .NET runtime required)
