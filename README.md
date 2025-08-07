# Crome-Extension-for-summarizing-the-page-content
This is a gen ai took in the form of a browser extension which will summarize the page content currently on your browser. 

**The files is in the master branch**

## 🚀 How to Use the Extension

Follow these steps to install and run the extension locally:

1. Open Chrome and go to: `chrome://extensions/`
2. Enable **Developer Mode** (toggle in the top-right corner).
3. Click on **“Load unpacked”**.
4. Select the folder(Extension) that contains:
   - `manifest.json`
   - `popup.html`
   - `popup.js`
   - `icon.png`
5. Start the FastAPI server by running the following command:
   ```bash
   uvicorn main:app --reload --port 8000
   
Using these methods you can set up the Fast Api server localy and use the Extension to summarize the web page content 

But if you want to skip the process of turning on the Fast API server you can replace the responce fetch url to "https://crome-extension-for-summarizing-the-page-njdi.onrender.com/summarize" which is my hosted server on render.

## 🔧 Tech Stack

**Frontend (Chrome Extension):**
- HTML
- CSS
- JavaScript
- Chrome Extension APIs

**Backend:**
- Python
- FastAPI
- Uvicorn (ASGI server)

 **Gen-AI/LLM**
- LangChain
- Groq
- model="openai/gpt-oss-20b"

**Hosting:**
- 🚀 Render

**Version Control:**
- Git & GitHub

## ⚠️ Disclaimer
- The Extension works for the full formated websides means those pages whose url start's with `https//:`

