"""Generate a professionally formatted PDF from the Patent Analyzer README."""
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, HRFlowable
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER

# Colors
DARK_BLUE = HexColor("#1a237e")
MED_BLUE = HexColor("#283593")
LIGHT_BLUE = HexColor("#e8eaf6")
HEADER_BG = HexColor("#1a237e")
ROW_ALT = HexColor("#f5f5f5")
WHITE = HexColor("#ffffff")
BLACK = HexColor("#000000")
GRAY = HexColor("#666666")
LIGHT_GRAY = HexColor("#e0e0e0")

def build_pdf():
    doc = SimpleDocTemplate(
        r"C:\Users\scott\OneDrive\Desktop\Claude\patent-analyzer-app\PatentAnalyzer-README.pdf",
        pagesize=letter,
        topMargin=0.75*inch,
        bottomMargin=0.75*inch,
        leftMargin=0.85*inch,
        rightMargin=0.85*inch,
    )

    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle("CustomTitle", parent=styles["Title"],
        fontSize=28, textColor=DARK_BLUE, spaceAfter=6, fontName="Helvetica-Bold")

    subtitle_style = ParagraphStyle("Subtitle", parent=styles["Normal"],
        fontSize=13, textColor=GRAY, spaceAfter=20, fontName="Helvetica-Oblique")

    h1 = ParagraphStyle("H1", parent=styles["Heading1"],
        fontSize=18, textColor=DARK_BLUE, spaceBefore=20, spaceAfter=10,
        fontName="Helvetica-Bold", borderWidth=0, borderPadding=0)

    h2 = ParagraphStyle("H2", parent=styles["Heading2"],
        fontSize=14, textColor=MED_BLUE, spaceBefore=14, spaceAfter=8,
        fontName="Helvetica-Bold")

    h3 = ParagraphStyle("H3", parent=styles["Heading3"],
        fontSize=12, textColor=MED_BLUE, spaceBefore=10, spaceAfter=6,
        fontName="Helvetica-Bold")

    body = ParagraphStyle("Body", parent=styles["Normal"],
        fontSize=10, leading=14, spaceAfter=6, fontName="Helvetica")

    body_bold = ParagraphStyle("BodyBold", parent=body,
        fontName="Helvetica-Bold")

    bullet = ParagraphStyle("Bullet", parent=body,
        leftIndent=20, bulletIndent=8, spaceBefore=2, spaceAfter=2)

    code_style = ParagraphStyle("Code", parent=body,
        fontName="Courier", fontSize=9, leading=12,
        backColor=HexColor("#f4f4f4"), leftIndent=12, rightIndent=12,
        spaceBefore=4, spaceAfter=4)

    tip_style = ParagraphStyle("Tip", parent=body,
        backColor=LIGHT_BLUE, leftIndent=12, rightIndent=12,
        spaceBefore=6, spaceAfter=6, borderPadding=8)

    disclaimer_style = ParagraphStyle("Disclaimer", parent=body,
        fontSize=9, leading=12, textColor=GRAY, fontName="Helvetica-Oblique")

    footer_style = ParagraphStyle("Footer", parent=body,
        fontSize=9, textColor=GRAY, fontName="Helvetica-Oblique", alignment=TA_CENTER)

    story = []

    def hr():
        story.append(Spacer(1, 6))
        story.append(HRFlowable(width="100%", thickness=1, color=LIGHT_GRAY))
        story.append(Spacer(1, 6))

    def make_table(headers, rows, col_widths=None):
        data = [headers] + rows
        t = Table(data, colWidths=col_widths, repeatRows=1)
        style_cmds = [
            ("BACKGROUND", (0, 0), (-1, 0), HEADER_BG),
            ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("FONTSIZE", (0, 0), (-1, 0), 10),
            ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
            ("FONTSIZE", (0, 1), (-1, -1), 9),
            ("LEADING", (0, 0), (-1, -1), 13),
            ("ALIGN", (0, 0), (-1, -1), "LEFT"),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("GRID", (0, 0), (-1, -1), 0.5, LIGHT_GRAY),
            ("TOPPADDING", (0, 0), (-1, -1), 6),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
            ("LEFTPADDING", (0, 0), (-1, -1), 8),
            ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ]
        for i in range(1, len(data)):
            if i % 2 == 0:
                style_cmds.append(("BACKGROUND", (0, i), (-1, i), ROW_ALT))
        t.setStyle(TableStyle(style_cmds))
        return t

    # ===== TITLE =====
    story.append(Spacer(1, 40))
    story.append(Paragraph("Patent Analyzer", title_style))
    story.append(Paragraph("AI-Powered Patent Feasibility Analysis Tool for Inventors \u2014 v1.2.0", subtitle_style))
    story.append(Paragraph(
        "A standalone Windows desktop application that takes an invention idea and runs a comprehensive "
        "6-stage patent analysis pipeline using the Anthropic Claude API. Produces a professional report "
        "covering prior art, patentability assessment, and IP strategy — with special depth on AI/ML and "
        "3D printing inventions.", body))
    hr()

    # ===== WHAT IT DOES =====
    story.append(Paragraph("What It Does", h1))
    story.append(Paragraph(
        "You describe your invention. The app runs 6 analysis stages automatically, one after another, "
        "streaming results in real time:", body))
    story.append(Spacer(1, 6))

    story.append(make_table(
        ["Stage", "Name", "What It Does"],
        [
            ["1", "Technical Intake", "Restates your idea in precise patent-ready technical language"],
            ["2", "Prior Art Search", "Searches patents, papers, products, and GitHub for existing work (uses web search)"],
            ["3", "Patentability Analysis", "Full \u00a7101/\u00a7102/\u00a7103/\u00a7112 analysis with common examiner concerns in this technology area"],
            ["4", "Deep Dive Analysis", "Specialized deep analysis of the invention\u2019s most patentable and riskiest elements"],
            ["5", "IP Strategy", "Filing landscape assessment, cost estimates, claim directions, trade secret boundaries"],
            ["6", "Final Report", "Assembles everything into one comprehensive patent analysis report"],
        ],
        col_widths=[0.5*inch, 1.4*inch, 4.6*inch]
    ))
    story.append(Spacer(1, 6))
    story.append(Paragraph(
        "<b>Output:</b> A comprehensive Markdown + HTML report saved automatically, plus individual stage outputs.", body))
    hr()

    # ===== QUICK START =====
    story.append(Paragraph("Quick Start", h1))
    story.append(Paragraph("Prerequisites", h2))
    story.append(Paragraph("\u2022  <b>Windows 10/11</b> (64-bit)", bullet))
    story.append(Paragraph("\u2022  <b>.NET 8 SDK</b> \u2014 https://dotnet.microsoft.com/download/dotnet/8.0", bullet))
    story.append(Paragraph("\u2022  <b>Anthropic API Key</b> \u2014 https://console.anthropic.com/", bullet))

    story.append(Paragraph("Build &amp; Run", h2))
    story.append(Paragraph("cd PatentAnalyzer", code_style))
    story.append(Paragraph("dotnet build", code_style))
    story.append(Paragraph("dotnet run --project PatentAnalyzer", code_style))

    story.append(Paragraph("First Launch", h2))
    story.append(Paragraph("1.  The app will open a Settings dialog on first run", bullet))
    story.append(Paragraph("2.  Enter your Anthropic API key", bullet))
    story.append(Paragraph("3.  Choose your model (Haiku is the default and works great)", bullet))
    story.append(Paragraph("4.  Click <b>Save Settings</b>", bullet))
    story.append(Paragraph("5.  Describe your invention in the input form", bullet))
    story.append(Paragraph("6.  Click <b>Run Full Analysis</b>", bullet))
    story.append(Paragraph("7.  Watch the analysis stream in real time across all 6 stages", bullet))
    story.append(Paragraph("8.  Find your report auto-saved in <font face='Courier'>Documents\\PatentAnalyzer\\output\\</font>", bullet))
    hr()

    # ===== PUBLISH =====
    story.append(Paragraph("Publish as Standalone .exe", h1))
    story.append(Paragraph("To create a single-file executable that runs without .NET installed:", body))
    story.append(Paragraph("dotnet publish -c Release -r win-x64 --self-contained true -p:PublishSingleFile=true", code_style))
    story.append(Paragraph("The executable will be in:", body))
    story.append(Paragraph("PatentAnalyzer\\bin\\Release\\net8.0-windows\\win-x64\\publish\\PatentAnalyzer.exe", code_style))
    hr()

    # ===== PROJECT STRUCTURE =====
    story.append(Paragraph("Project Structure", h1))
    struct_lines = [
        "PatentAnalyzer/",
        "+-- PatentAnalyzer.sln",
        "+-- README.md",
        "+-- PatentAnalyzer/",
        "    +-- PatentAnalyzer.csproj",
        "    +-- App.xaml / App.xaml.cs",
        "    +-- MainWindow.xaml",
        "    +-- MainWindow.xaml.cs",
        "    +-- Models/",
        "    |   +-- AnalysisModels.cs",
        "    +-- Services/",
        "        +-- AnthropicClient.cs",
        "        +-- PipelineRunner.cs",
        "        +-- PromptTemplates.cs",
        "        +-- ReportExporter.cs",
        "        +-- ConfigManager.cs",
    ]
    for line in struct_lines:
        story.append(Paragraph(line, code_style))
    hr()

    # ===== CONFIGURATION =====
    story.append(Paragraph("Configuration", h1))
    story.append(Paragraph("Settings are saved to <font face='Courier'>config.json</font> next to the executable:", body))
    story.append(Spacer(1, 6))
    story.append(make_table(
        ["Setting", "Default", "Description"],
        [
            ["apiKey", "(none)", "Your Anthropic API key"],
            ["model", "claude-haiku-4-5-20251001", "Model for analysis stages"],
            ["researchModel", "(empty)", "Optional cheaper model for prior art search (Stage 2)"],
            ["outputDirectory", "Documents\\PatentAnalyzer\\output", "Where reports are saved"],
            ["interStageDelaySeconds", "5", "Pause between stages (rate limit protection)"],
            ["maxTokens", "32000", "Max output tokens per stage"],
        ],
        col_widths=[1.8*inch, 2.2*inch, 2.5*inch]
    ))

    story.append(Paragraph("Model Recommendations", h2))
    story.append(Spacer(1, 4))
    story.append(make_table(
        ["Model", "Best For", "Typical Cost per Run"],
        [
            ["claude-haiku-4-5-20251001", "Default \u2014 fast, affordable, tuned for this app", "~$0.75\u20131.50"],
            ["claude-sonnet-4-20250514", "Alternative if you want to experiment", "~$3\u20136"],
            ["claude-opus-4-20250514", "Maximum quality (expensive)", "~$10\u201320"],
        ],
        col_widths=[2.3*inch, 2.7*inch, 1.5*inch]
    ))
    story.append(Spacer(1, 6))
    story.append(Paragraph(
        "<b>Tip:</b> Haiku is the recommended model. The app\u2019s prompts are tuned specifically for it. "
        "A full 6-stage analysis typically costs $0.75\u2013$1.50 depending on invention complexity and web search depth.",
        tip_style))
    hr()

    # ===== OUTPUT FILES =====
    story.append(Paragraph("Output Files", h1))
    story.append(Paragraph("Each analysis creates a timestamped folder in your output directory:", body))
    output_lines = [
        "2026-03-17_1430_My-Invention/",
        "+-- Patent-Analysis-Report.md",
        "+-- Patent-Analysis-Report.html",
        "+-- Stage-01_Technical-Intake.md",
        "+-- Stage-02_Prior-Art-Search.md",
        "+-- Stage-03_Patentability-Analysis.md",
        "+-- Stage-04_Deep-Dive-Analysis.md",
        "+-- Stage-05_IP-Strategy.md",
        "+-- Stage-06_Comprehensive-Report.md",
        "+-- analysis-summary.md",
    ]
    for line in output_lines:
        story.append(Paragraph(line, code_style))
    story.append(Spacer(1, 4))
    story.append(Paragraph("The HTML report is styled for professional presentation and printing.", body))
    hr()

    # ===== WHAT THE ANALYSIS COVERS =====
    story.append(Paragraph("What the Analysis Covers", h1))

    story.append(Paragraph("For All Inventions", h2))
    for item in [
        "Technical restatement in patent-ready language",
        "Prior art search across patents, papers, products, and open source",
        "Full patentability assessment (\u00a7101, \u00a7102, \u00a7103, \u00a7112)",
        "Common examiner concerns analysis",
        "Filing landscape assessment (provisional vs. non-provisional, timing, costs)",
        "Claim direction recommendations",
        "Documentation checklist",
    ]:
        story.append(Paragraph(f"\u2022  {item}", bullet))

    story.append(Paragraph("For AI / ML Inventions (Special Depth)", h2))
    for item in [
        "Patent zone classification (strong vs. red-flag categories)",
        "Alice/Mayo \u00a7101 deep analysis specific to AI",
        "Current USPTO AI guidance and Federal Circuit decisions",
        "AI claim framing strategy (system vs. method vs. CRM)",
        "Trade secret vs. patent boundary analysis for algorithms",
    ]:
        story.append(Paragraph(f"\u2022  {item}", bullet))

    story.append(Paragraph("For 3D Printing Inventions (Special Depth)", h2))
    for item in [
        "Design patent vs. utility patent analysis",
        "Category classification (geometry, process, material, software, post-processing)",
        "3D printing patent landscape search (Stratasys, 3D Systems, HP, etc.)",
        "Design patent claiming strategy (broken/solid lines, breadth)",
        "Combined AI + 3D printing opportunities",
    ]:
        story.append(Paragraph(f"\u2022  {item}", bullet))
    hr()

    # ===== DEPENDENCIES =====
    story.append(Paragraph("Dependencies", h1))
    story.append(make_table(
        ["Package", "Version", "Purpose"],
        [
            ["System.Text.Json", "8.0.5", "JSON serialization for API + config"],
            ["Markdig", "0.37.0", "Markdown \u2192 HTML conversion for reports"],
        ],
        col_widths=[2*inch, 1*inch, 3.5*inch]
    ))
    story.append(Spacer(1, 4))
    story.append(Paragraph(
        "No Anthropic SDK dependency \u2014 uses raw HttpClient with SSE streaming for maximum "
        "compatibility and transparency.", body))
    hr()

    # ===== BUILDING FROM SOURCE =====
    story.append(Paragraph("Building from Source", h1))
    story.append(Paragraph("Requirements", h2))
    story.append(Paragraph("\u2022  .NET 8 SDK", bullet))
    story.append(Paragraph("\u2022  Visual Studio 2022+ (optional) or VS Code with C# extension", bullet))
    story.append(Paragraph("\u2022  Windows 10/11", bullet))
    story.append(Paragraph("Steps", h2))
    story.append(Paragraph("dotnet restore", code_style))
    story.append(Paragraph("dotnet build", code_style))
    story.append(Paragraph("dotnet run --project PatentAnalyzer", code_style))
    story.append(Paragraph("dotnet publish -c Release -r win-x64 --self-contained true -p:PublishSingleFile=true", code_style))
    hr()

    # ===== TROUBLESHOOTING =====
    story.append(Paragraph("Troubleshooting", h1))
    story.append(make_table(
        ["Problem", "Solution"],
        [
            ['"API key is invalid"', "Check your key at console.anthropic.com"],
            ["Rate limit errors", "The app retries automatically (3 attempts). Increase inter-stage delay in settings."],
            ["Build errors", "Make sure you have .NET 8 SDK: dotnet --version should show 8.x"],
            ["App won\u2019t start", "Run from command line to see errors: dotnet run --project PatentAnalyzer"],
            ["Reports not saving", "Check output directory exists and you have write permission"],
        ],
        col_widths=[2*inch, 4.5*inch]
    ))
    hr()

    # ===== LEGAL DISCLAIMER =====
    story.append(Paragraph("Legal Disclaimer", h1))
    story.append(Paragraph(
        "This tool provides <b>AI-powered patent research support</b>, not legal advice. "
        "The author of this tool is not a lawyer. The AI system that generates the analysis is not a lawyer. The analysis:", body))
    for item in [
        "Does <b>not</b> create an attorney-client relationship",
        "Does <b>not</b> constitute a formal patentability or freedom-to-operate opinion",
        "Should <b>not</b> be relied upon as a substitute for engagement with a registered patent attorney",
        "Is intended to help inventors understand the patent landscape before investing in formal legal work",
    ]:
        story.append(Paragraph(f"\u2022  {item}", bullet))
    story.append(Spacer(1, 8))
    story.append(Paragraph("<b>Always consult a registered patent attorney before filing.</b>", body_bold))
    story.append(Spacer(1, 20))
    hr()
    story.append(Paragraph(
        "Built with the Anthropic Claude API. Analysis quality depends on the model selected and "
        "the detail of your invention description.", footer_style))

    doc.build(story)
    print("PDF generated successfully!")

if __name__ == "__main__":
    build_pdf()
