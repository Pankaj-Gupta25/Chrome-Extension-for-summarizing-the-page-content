🧠 Chrome Extension for Summarizing Page Content
This is a GenAI-powered Chrome extension that summarizes the content of the current web page you're viewing.

📁 Branch Information
All the required files are in the master branch.

🚀 How to Use the Extension
Follow the steps below to install and use the extension:

Clone the Repository

bash
Copy
Edit
git clone https://github.com/your-username/Crome-Extension-for-summarizing-the-page-content.git
cd Crome-Extension-for-summarizing-the-page-content
Start the FastAPI Server

Navigate to the directory where main.py is located.

Run the following command to start the server:

bash
Copy
Edit
uvicorn main:app --reload --port 8000
Open the Chrome Extensions Page

In Chrome, go to:

arduino
Copy
Edit
chrome://extensions/
Enable Developer Mode

Turn on the Developer Mode toggle in the top right.

Load the Unpacked Extension

Click on “Load unpacked”

Select the folder that contains the following files:

manifest.json

popup.html

popup.js

icon.png

You're Ready to Go!

The extension icon will appear in the Chrome toolbar.

Click it to summarize the current page content.

⚠️ Important Notes
Ensure the FastAPI server is running on http://localhost:8000 before using the extension.

If you make changes to the code, remember to reload the extension from chrome://extensions/. 

If you want to skip the task of turn on the Fast Api server then in the popup.json replace the

 const response = await fetch("http://localhost:8000/summarize" 

 with : const response = await fetch("https://crome-extension-for-summarizing-the-page-njdi.onrender.com/summarize" 

 this is a server hosted on the render 

with 
