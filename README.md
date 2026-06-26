# 🚀 RankFlow

<div align="center">
  <p><strong>A 100% Free & Open-Source SEO, AEO, and GEO Automation Pipeline</strong></p>
</div>

RankFlow is a completely automated pipeline designed to audit, optimize, and generate AI-ready content for your website. It combines traditional SEO checks with Answer Engine Optimization (AEO) and Generative Engine Optimization (GEO) strategies to ensure your content ranks everywhere.

## ✨ Features

- **🌐 Deep Web Crawling**: Extracts clean Markdown and HTML from any website using `crawl4ai`.
- **📊 SEO Metadata Analysis**: Checks for Title, Description, Canonical, Robots, OpenGraph, and Twitter Card tags.
- **🏗️ Structural Heading Checks**: Validates your H1-H6 structure, identifying jumps or missing headers.
- **🔗 Intelligent Internal Linking**: Suggests semantic internal links using `sentence-transformers` embeddings.
- **🤖 AI Content Rewriting**: Dynamically rewrites paragraphs to be AI-friendly using OpenRouter LLMs.
- **❓ Automated FAQ Generation**: Generates contextual FAQs from your page content.
- **📈 JSON-LD Schema Creation**: Automatically wraps generated FAQs in valid `FAQPage` schema.
- **📉 Visual HTML Reports**: Outputs a beautiful, interactive dashboard with your SEO, AEO, and GEO scores.

---

## 🛠️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/khushi-dutta/RankFlow.git
cd RankFlow
```

### 2. Install dependencies
It is recommended to use a virtual environment.
```bash
pip install -r requirements.txt
```

### 3. Setup the Crawler
Initialize Playwright browsers required by `crawl4ai`:
```bash
crawl4ai-setup
```

### 4. Configure API Keys
Copy the example environment file and add your OpenRouter API key.
```bash
cp .env.example .env
```
Open `.env` and add your `OPENROUTER_API_KEY`. (Get one for free at [OpenRouter](https://openrouter.ai/)).

---

## 🚀 Usage

Run the pipeline against any URL:

```bash
python main.py https://example.com
```

### Output
The pipeline will generate an `output/` directory containing:
1. `report.html` - An interactive dashboard showing your SEO, AEO, and GEO scores alongside detailed audit findings.
2. `[site_name].md` - The raw markdown extracted from the site.
3. `[site_name]_optimized.md` - The final, AI-optimized markdown complete with generated FAQs, schemas, and rewritten content.

---

## 🏗️ Architecture

```text
Website -> Crawl4AI -> Extract HTML + Markdown
    │
    ├─► Metadata Checker
    ├─► Heading Analyzer
    ├─► Readability Analyzer
    ├─► Internal Link Generator
    ├─► FAQ Generator (OpenRouter LLM)
    ├─► Schema Generator
    ├─► Content Rewriter (OpenRouter LLM)
    │
    └─► HTML Report Generation & Markdown Compilation
```

## 📜 License

This project is open-source and free to use.
