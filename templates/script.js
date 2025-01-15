document.getElementById('detectButton').addEventListener('click', async () => {
    const emailText = document.getElementById('emailInput').value;

    const response = await fetch('http://127.0.0.1:5000/api/detect_spam', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ email_text: emailText })
    });

    const data = await response.json();
    document.getElementById('result').innerText = data.result;
});
