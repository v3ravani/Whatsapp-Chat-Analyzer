# 📊 WhatsApp Chat Analyzer

## 🚀 Overview
WhatsApp Chat Analyzer is a FastAPI-based tool that allows users to upload and analyze WhatsApp chat exports. It provides valuable insights into user interactions, sentiment trends, frequently used words and emojis, response times, and more. The project includes a backend built with FastAPI that processes chat data and returns analytical insights.

## 🛠 Features
- 📂 **Upload WhatsApp Chat Exports** (TXT format)
- 🔍 **Analyze Sentiment** of messages
- ⏳ **Measure Response Times** between users
- 📊 **Find Top Words and Emojis** used
- 📅 **Identify Most Active Days & Hours**
- 📈 **Generate Insights on Conversation Patterns**
- 🌐 **REST API for easy integration**
- 📌 **Top 10 words used**
- 📌 **Top 10 words per user**
- 😊 **Top 5 emojis per user**
- ⏳ **Average response time per user**
- 📊 **Total messages sent by each user**
- ⌛ **Average daily chatting time**
- 📝 **Longest message per user**
- 🔗 **Most common links shared**
- 🚀 **Conversation starters**
- 📈 **Sentiment analysis per user**
- 🤖 **Sarcasm scores (out of 10)**
- 🔥 **Chat energy score (out of 10)**
- 📌 **Most common phrases per user**
- 🚫 **Most ignored messages**
- ❓ **Questions asked per user**

## 🎯 How It Works
1. **Paste your WhatsApp chat export (TXT file) into `chat.txt` in the backend folder.**
2. The backend processes the chat, extracts key insights, and performs sentiment analysis.
3. Run the chat analyzer script to get detailed insights.

## 🏗 Tech Stack
- **Backend:** FastAPI, Uvicorn, Natural Language Toolkit (NLTK), Pandas
- **Deployment:** Uvicorn server

## 📂 Project Structure
```
whatsapp_analyzer/
│── backend/
│   ├── main.py             # FastAPI backend
│   ├── chat_analyzer.py    # Chat processing logic
│   ├── requirements.txt    # Dependencies
│── README.md               # Project documentation
```

## 🔧 Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/whatsapp-chat-analyzer.git
cd whatsapp-chat-analyzer
```

### 2️⃣ Setup the Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
```

### 3️⃣ Run the Backend Server
```bash
uvicorn main:app --reload
```
Server will be available at: `http://127.0.0.1:8000`

### 4️⃣ Run the Chat Analyzer Script
```bash
python chat_analyzer.py
```

## 🔗 API Endpoints
| Method | Endpoint           | Description             |
|--------|-------------------|-------------------------|
| `POST` | `/upload-chat/`   | Upload WhatsApp chat file |
| `GET`  | `/analyze/`       | Get chat insights |

## 🎯 Example API Request
```bash
curl -X POST -F "file=@chat.txt" http://127.0.0.1:8000/upload-chat/
```

## 🛠 Troubleshooting
- **Backend not running?** Make sure Uvicorn is running (`uvicorn main:app --reload`)
- **CORS issue?** Allow CORS in FastAPI with:
  ```python
  from fastapi.middleware.cors import CORSMiddleware
  app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"], allow_credentials=True)
  ```

## 🤝 Contributing
Feel free to fork, contribute, or raise issues. PRs are welcome!

## 📜 License
This project is licensed under the MIT License.

---
✨ Happy Chat Analyzing! ✨

