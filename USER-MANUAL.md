# Patent Analyzer User Manual

Version 1.2.0 — April 2026

---

## 1. What Is Patent Analyzer?

Patent Analyzer is a free Windows application that helps you research whether your invention idea might be worth patenting. You describe your idea in plain English, press one button, and the app produces a detailed research report covering what similar inventions already exist, how strong your idea looks from a patent perspective, and what steps you might consider next.

The app uses artificial intelligence (specifically, Anthropic's Claude AI) to analyze your idea across six stages and assemble the results into a professional report. The entire process is automated — you do not need to copy and paste between windows or understand patent law terminology.

**Important:** Patent Analyzer is a research tool, not a lawyer. It does not provide legal advice and does not replace a patent attorney. Think of it as a way to organize your thinking and gather preliminary research before you consult with a professional. Every report the app generates includes disclaimers making this clear.

---

## 2. What You Need

### A Windows Computer
- Windows 10 or Windows 11 (64-bit)
- The WebView2 Runtime (this is already installed on nearly all modern Windows computers — see Troubleshooting if you encounter issues)

### An Anthropic API Key
An API key is like a password that lets the app communicate with Anthropic's AI service. Here is how to get one:

1. Go to [console.anthropic.com](https://console.anthropic.com/)
2. Create a free account (you will need an email address)
3. Add a payment method — the AI charges a small fee per analysis (typically under $1.50)
4. Go to the API Keys section and click "Create Key"
5. Copy the key — it starts with `sk-ant-` and is a long string of letters and numbers
6. Keep this key private. Do not share it with anyone.

**Cost:** A typical 6-stage analysis costs between $0.75 and $1.50 in API fees, depending on how detailed your invention description is. You are billed directly by Anthropic, not by Patent Analyzer.

---

## 3. Downloading and Running the App

1. Go to the [Patent Analyzer releases page](https://github.com/scottconverse/patent-analyzer-app/releases) on GitHub
2. Download `PatentAnalyzer.exe` from the latest release
3. Save it anywhere you like — your Desktop, Documents folder, wherever is convenient
4. Double-click the file to run it

There is no installer. The app is a single file that runs directly. Windows may show a security warning the first time you run it because the file was downloaded from the internet — click "More info" and then "Run anyway" to proceed.

---

## 4. First Launch Setup

When you open Patent Analyzer for the first time, you need to enter your API key.

1. Click the **Settings** tab at the top of the window
2. Paste your Anthropic API key into the API Key field
3. **Model:** Leave this set to the default (Haiku) unless you have a reason to change it. Haiku is fast, affordable, and produces good results.
4. Click **Save Settings**

Your API key is encrypted on your computer using Windows security features (DPAPI). It is never stored as plain text and never sent anywhere except to Anthropic's servers during analysis.

### Model Options
- **Haiku** (default) — Fast and affordable. About $0.75-$1.50 per analysis. Recommended for most users.
- **Sonnet** — Higher quality analysis. About $3-$6 per analysis.
- **Opus** — Maximum quality. About $10-$20 per analysis.

---

## 5. Describing Your Invention

Switch to the **Analysis** tab and type or paste your invention description into the text box. Here are some tips for getting the best results:

**Do include:**
- What your invention does and the problem it solves
- How it works — describe the key components or steps
- What makes it different from existing solutions
- The technology area (software, mechanical, chemical, etc.)
- Any specific materials, algorithms, or processes involved

**Do not worry about:**
- Using legal or patent terminology — plain English is fine
- Perfect grammar or formatting — the AI will interpret your meaning
- Being too detailed — more detail generally produces better results

**Example of a good description:**
"I invented a smart garden watering system that uses soil moisture sensors and weather forecast data to automatically adjust how much water each plant zone gets. It has a phone app that shows real-time soil moisture levels and lets you set watering schedules. The key innovation is the machine learning algorithm that learns each plant zone's water needs over time and reduces water usage by up to 40% compared to traditional timer-based systems."

---

## 6. Running the Analysis

1. After entering your invention description, click **Run Full Analysis**
2. The app will run six analysis stages automatically, one after another
3. You can watch the results stream in real time as each stage progresses

### What Each Stage Does

| Stage | Name | What Happens |
|-------|------|-------------|
| 1 | **Technical Intake** | Restates your invention in precise technical language and identifies the key components and inventive concepts |
| 2 | **Prior Art Search** | Searches for existing patents, research papers, and products that are similar to your invention |
| 3 | **Patentability Analysis** | Evaluates your invention against the main legal requirements for patents, and identifies common examiner concerns in this technology area |
| 4 | **Deep Dive Analysis** | Provides specialized analysis for your specific technology area (AI, software, 3D printing, etc.) |
| 5 | **IP Strategy** | Assesses the filing landscape and provides cost estimates, suggested next steps, and notes on potential blocking IP to discuss with counsel |
| 6 | **Final Report** | Combines everything into one comprehensive report with an overall landscape assessment |

### How Long Does It Take?
A full analysis typically takes 5 to 15 minutes, depending on your internet connection and how complex your invention is. You can watch the progress in real time.

### Can I Stop It?
Yes. You can close the window at any time and the analysis will stop cleanly. Any stages that completed before you stopped will still be saved.

---

## 7. Understanding the Results

When the analysis is complete, you will see the final report in the main window. Here is what the key sections and labels mean:

### Assessment Labels

| Label | What It Means |
|-------|--------------|
| **LANDSCAPE FAVORS FILING** | The research suggests your invention has strong potential. Prior art is limited and the idea appears novel. Consider consulting a patent attorney. |
| **LANDSCAPE LEANS TOWARD FILING** | The research is generally positive, but there are some concerns to address. A patent attorney can help you evaluate the risks. |
| **MIXED LANDSCAPE** | There are both positive and negative indicators. Professional guidance is recommended to determine whether filing makes sense. |
| **LANDSCAPE SUGGESTS CAUTION** | Significant concerns were identified — substantial prior art, legal hurdles, or other challenges. Discuss with a patent attorney before investing in a filing. |

### Key Report Sections

- **Filing Landscape Assessment** — The overall recommendation on whether the patent landscape looks favorable for your invention
- **Overall Landscape Assessment** — A plain-English summary of the entire analysis that anyone can understand
- **Common Examiner Concerns in This Technology Area** — Potential objections a patent examiner might raise, so you and your attorney can prepare responses
- **Potential Blocking IP to Discuss with Counsel** — Existing patents or intellectual property that could affect your ability to make or sell your invention, flagged for discussion with an attorney

### Important Reminder
Every section of the report includes a disclaimer reminding you that this is AI-generated research, not legal advice. The AI is a research assistant — it can help you organize information and identify potential issues, but it cannot replace the judgment of a qualified patent attorney.

---

## 8. Exporting Your Report

Reports are saved automatically when the analysis completes. You can find them in:

**Documents > PatentAnalyzer > output**

Each analysis creates a folder with a timestamp and your invention name. Inside you will find:

- **Patent-Analysis-Report.md** — The full report in Markdown format (a plain text format that can be opened in any text editor)
- **Patent-Analysis-Report.html** — The full report as a styled web page (open in any browser, looks professional, good for printing)
- **Individual stage files** — Each of the six stages saved separately

The HTML report is formatted for professional presentation. You can print it directly from your browser or save it as a PDF using your browser's "Print to PDF" feature.

---

## 9. What to Do Next

Patent Analyzer gives you a research starting point, not a final answer. Here is what to do with your results:

1. **Read the full report** — Pay special attention to the prior art findings and the common examiner concerns
2. **Take it to a patent attorney** — Share the report with a registered patent attorney. They can verify the findings, conduct a professional prior art search, and advise you on whether to file
3. **Prepare your documentation** — The report includes a documentation checklist. Start gathering technical documents, drawings, and development records
4. **Consider timing** — If you plan to file, earlier is generally better. Public disclosure of your invention can affect your ability to patent it

### Finding a Patent Attorney
- The USPTO maintains a searchable directory of registered patent attorneys at [USPTO Patent Attorney Search](https://oedci.uspto.gov/OEDCI/)
- Look for an attorney who specializes in your technology area
- Many patent attorneys offer a free initial consultation

---

## 10. Troubleshooting

### "API key is invalid"
- Double-check your API key at [console.anthropic.com](https://console.anthropic.com/)
- Make sure you copied the entire key (it starts with `sk-ant-`)
- If you moved the app to a new computer, you will need to re-enter your key in Settings

### "WebView2 Runtime Required"
The app needs the Microsoft Edge WebView2 Runtime to display results. This component is pre-installed on most Windows 10 and 11 computers. If you see this error:
- Run Windows Update to install the latest system components
- Or download WebView2 directly from [Microsoft](https://developer.microsoft.com/en-us/microsoft-edge/webview2/)

### Analysis Stops with a Rate Limit Error
This means Anthropic's servers are temporarily limiting requests. The app will retry automatically (up to 3 times with increasing wait periods). If it keeps happening, try increasing the "Inter-stage delay" in Settings.

### The App Will Not Start
- Make sure you are running Windows 10 or 11 (64-bit)
- Try right-clicking the file and selecting "Run as administrator"
- If Windows blocks the file, right-click it, select Properties, and check "Unblock" at the bottom of the General tab

### Reports Are Not Saving
- Check the output directory in Settings — make sure the folder exists and you have permission to write to it
- The default location is your Documents folder under PatentAnalyzer > output

### Settings Were Lost After Updating
Version 1.1 moved settings to a new location. If you are upgrading from version 1.0, your settings should migrate automatically. If they do not, re-enter your API key in the Settings tab.

---

## 11. Glossary

**API (Application Programming Interface):** A way for one piece of software to communicate with another. Patent Analyzer uses the Anthropic API to send your invention description to the Claude AI and receive the analysis results.

**API Key:** A unique code that identifies you when using an API. Think of it as a password for the service. Your API key is tied to your Anthropic account and billing.

**DPAPI (Data Protection API):** A Windows security feature that encrypts data so only your Windows account can read it. Patent Analyzer uses this to protect your API key.

**Intellectual Property (IP):** Creations of the mind — inventions, designs, brand names — that can be legally protected through patents, trademarks, copyrights, or trade secrets.

**Patent:** A legal right granted by the government that gives an inventor exclusive rights to make, use, and sell their invention for a limited time (usually 20 years). In exchange, the inventor publicly discloses how the invention works.

**Patentability:** Whether an invention meets the legal requirements to receive a patent. The main requirements are that the invention must be novel (new), non-obvious (not an obvious combination of existing ideas), and useful.

**Prior Art:** Any existing evidence that your invention or something similar was already known before your patent application. This includes existing patents, published research, commercial products, and public demonstrations.

**Provisional Patent Application:** A simplified, lower-cost patent application that establishes an early filing date. It gives you 12 months to file a full (non-provisional) patent application. Often used to secure a date while refining the invention.

**Trade Secret:** An alternative to patenting where you keep your invention confidential rather than disclosing it publicly. Suitable for processes or methods that competitors cannot easily reverse-engineer.

**WebView2:** A component from Microsoft that allows desktop applications to display web content. Patent Analyzer uses it to show your formatted report.

---

*Patent Analyzer is an open-source research tool, not a legal service. All AI-generated analysis is for informational purposes only. Consult a registered patent attorney before making filing decisions.*
