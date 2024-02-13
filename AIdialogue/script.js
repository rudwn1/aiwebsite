function sendAudio() {
    let audioInput = document.getElementById('audioInput').files[0];
    let formData = new FormData();
    formData.append('audio', audioInput);

    fetch('/asr', { method: 'POST', body: formData })
        .then(response => response.json())
        .then(data => {
            document.getElementById('response').innerText = JSON.stringify(data);
        });
}

function sendText() {
    let textInput = document.getElementById('textInput').value;
    let formData = new FormData();
    formData.append('text', textInput);

    fetch('/generate_text', { method: 'POST', body: formData })
        .then(response => response.json())
        .then(data => {
            document.getElementById('response').innerText = JSON.stringify(data);
        });
}
