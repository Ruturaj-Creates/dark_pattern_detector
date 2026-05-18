document.getElementById("scanBtn").addEventListener("click", async () => {

    try {

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

        let patternsHTML = "";

        data.patterns.forEach(pattern => {

            patternsHTML += `
                <div style="
                    margin-top: 15px;
                    padding: 10px;
                    border: 1px solid #ddd;
                    border-radius: 8px;
                ">
                    <h4 style="margin: 0 0 8px 0;">
                        ${pattern.type.toUpperCase()}
                    </h4>

                    <p style="margin: 5px 0;">
                        Severity:
                        <strong>${pattern.severity}</strong>
                    </p>

                    <ul>
                        ${pattern.matches
                            .map(match => `<li>${match}</li>`)
                            .join("")}
                    </ul>
                </div>
            `;
        });

        let riskColor = "green";

        if (data.risk_score >= 50) {
            riskColor = "red";
        }
        else if (data.risk_score >= 20) {
            riskColor = "orange";
        }

        document.getElementById("result").innerHTML = `
            <div style="
                margin-top: 15px;
                padding: 10px;
                border-radius: 8px;
                background: #f5f5f5;
            ">

                <h3 style="
                    color:${riskColor};
                    margin-bottom: 10px;
                ">
                    Risk Score: ${data.risk_score}
                </h3>

                <p><strong>Scanned URL:</strong></p>

                <p style="
                    word-break: break-all;
                    font-size: 12px;
                ">
                    ${data.url}
                </p>

                ${patternsHTML}

            </div>
        `;

    } catch (error) {

        document.getElementById("result").innerHTML = `
            <p style="color:red;">
                Error scanning website.
            </p>
        `;

        console.error(error);
    }

});