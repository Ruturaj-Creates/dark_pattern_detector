document.getElementById("scanBtn").addEventListener("click", async () => {

    let [tab] = await chrome.tabs.query({
        active: true,
        currentWindow: true
    });

    const response = await fetch("http://127.0.0.1:8000/scan", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            url: tab.url
        })
    });

    const data = await response.json();

    document.getElementById("result").innerHTML = `
        <h3>Risk Score: ${data.risk_score}</h3>
    `;
});