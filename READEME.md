# 🤖 AI Resume Critique Tool

An AI-powered resume review tool that helps job seekers improve their resumes instantly with personalized feedback.

## 🔍 Problem

Many job seekers struggle with resume formatting, keyword use, and highlighting relevant skills. They often don't know what recruiters are looking for, and professional resume reviews can be expensive or hard to access.

## 💡 Solution

This tool uses AI (GPT-4) to analyze resumes and provide:
- Grammar and formatting corrections
- Suggestions for missing sections
- Industry-relevant keywords
- General feedback on resume effectiveness

## 🧠 How It Works

1. Upload a resume (PDF format)
2. AI extracts the text from the file
3. GPT-4 reviews the resume and gives personalized suggestions
4. All processing is done using open-source tools (Streamlit, PyMuPDF) and OpenAI’s API

## ⚙️ Tech Stack

- Python
- Streamlit (for UI)
- PyMuPDF (for PDF text extraction)
- OpenAI API (for resume analysis)

## 🚀 How to Run Locally

```bash
git clone https://github.com/your-username/resume-critique-tool.git
cd resume-critique-tool
pip install -r requirements.txt
streamlit run app.py
