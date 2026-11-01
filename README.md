# AI Sentiment Analyzer

A full-stack web application built with **Flask**, **HTML/CSS**, and **Hugging Face Transformers** that performs real-time local sentiment analysis on text input without relying on paid cloud APIs.

## 🚀 Features
- **Local Inference:** Runs Hugging Face's pre-trained model (`distilbert-base-uncased-finetuned-sst-2-english`) directly via PyTorch and transformers.
- **Cost-Free Execution:** Completely bypasses cloud API rate limits and credit costs.
- **Probabilistic Confidence Scores:** Classifies text into `POSITIVE` or `NEGATIVE` polarities with exact confidence percentages.
- **Responsive Web UI:** Clean, modern interface utilizing asynchronous JavaScript (`fetch`) for non-blocking processing.

---

## 🛠️ Tech Stack
- **Backend:** Python, Flask, PyTorch, Hugging Face Transformers
- **Frontend:** HTML5, CSS3, JavaScript (Fetch API)

---

## ⚙️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Karan49557/ai-sentiment-analyzer.git](https://github.com/Karan49557/ai-sentiment-analyzer.git)
   cd ai-sentiment-analyzer
