# Crome-Extension-for-summarizing-the-page-content
This is a gen ai took in the form of a browser extension which will summarize the page content currently on your browser. 

**The files is in the master branch**

#In order to use the extention first clone this repo then follow the folling steps : 

1 -->  chrome://extensions/
2 --> on the developer mode
3 --> select the load unpack
4 --> now upload the extension file which contain the  manifest.json,popup.html,popup.js,icon.png 
6 --> now you are needed to on the Fast Api server by using the command uvicorn main:app --reload --port 8000
5 --> your chrome extention is ready to be used in your extentions icon

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
