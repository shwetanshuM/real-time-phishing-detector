const button = document.getElementById('checkBtn');
const result = document.getElementById('result');

button.addEventListener('click', async () => {

    const tabs = await chrome.tabs.query({
        active: true,
        currentWindow: true
    });

    const currentUrl = tabs[0].url;

    result.innerHTML = "Checking...";

    try {

        const response = await fetch('http://127.0.0.1:5000/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                url: currentUrl
            })
        });

        const data = await response.json();

        if(data.prediction === 'Phishing') {
            result.style.color = 'red';
        }
        else {
            result.style.color = 'lightgreen';
        }

        result.innerHTML = `
            ${data.prediction}<br>
            Confidence: ${(data.confidence * 100).toFixed(2)}%
        `;

    }
    catch(error) {
        result.innerHTML = 'Backend server not running';
        result.style.color = 'orange';
    }
});