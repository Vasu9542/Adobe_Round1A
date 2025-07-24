# 🧠 Adobe India Hackathon 2025 – Round 1A Submission

## 🔍 Challenge: Understand Your Document

The goal of Round 1A is to extract a **structured outline** from a given PDF, identifying:
- 📌 Title
- 📑 Headings of types: H1, H2, H3
- 🗂️ Page number for each heading

This enables downstream tasks like semantic search and document summarization.

---

## 🛠️ Tech Stack

- 🐍 Python 3.10
- 📄 PyMuPDF (`fitz`) for PDF parsing
- 🐳 Docker for containerization

---

## 🧩 Approach

We developed a rule-based system that:
1. **Analyzes font sizes** across the document to estimate heading levels.
2. Identifies **bold and large text** as potential H1 candidates.
3. Filters out irrelevant or noisy content (e.g., emails, links, small text).
4. Assigns heading levels (H1 > H2 > H3) based on relative font size.
5. Extracts a single **document title** (first bold H1 on page 1).

---

## 📁 Folder Structure

Adobe_Round1A/
├── app/
│ ├── extractor.py # core heading extraction logic
│ └── init.py
├── input/ # place PDFs here (e.g. sample.pdf)
├── output/ # .json output is saved here
├── run.py # runner script
├── requirements.txt # Python dependencies
├── Dockerfile # for containerized execution
└── README.md # this file
