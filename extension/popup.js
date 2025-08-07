document.getElementById("summarizeBtn").addEventListener("click", async () => {
  const button = document.getElementById("summarizeBtn");
  const summaryText = document.getElementById("summary");

  button.disabled = true;
  summaryText.textContent = "Summarizing... please wait.";

  try {
    const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
    const currentUrl = tab.url;


    if (!currentUrl.startsWith("http://") && !currentUrl.startsWith("https://")) {
      summaryText.textContent = "Cannot summarize this type of page (e.g., chrome:// or edge://)";
      button.disabled = false;
      return;
    }

    const response = await fetch("http://localhost:8000/summarize", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ url: currentUrl })
    });

    const data = await response.json();
    summaryText.textContent = data.summary || "No summary generated.";
  } catch (err) {
    console.error(err);
    summaryText.textContent = "Error summarizing the page.";
  } finally {
    button.disabled = false;
  }
});
