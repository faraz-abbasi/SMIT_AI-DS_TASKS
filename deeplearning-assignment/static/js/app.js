const video = document.getElementById('video');
const canvas = document.getElementById('canvas');
const personName = document.getElementById('personName');
const confScore = document.getElementById('confScore');

// Start Webcam
if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
    navigator.mediaDevices.getUserMedia({ video: true })
        .then(stream => video.srcObject = stream)
        .catch(err => console.error("Camera error:", err));
}

function capture() {
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    canvas.getContext('2d').drawImage(video, 0, 0);
    
    const imageData = canvas.toDataURL('image/jpeg');
    
    personName.textContent = "Analyzing...";
    
    fetch('/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ image: imageData })
    })
    .then(res => res.json())
    .then(data => {
        if (data.error) {
            alert(data.error);
        } else {
            // Updated variable name
            personName.textContent = data.predicted_person;
            confScore.textContent = data.confidence;
        }
    })
    .catch(err => console.error("Error:", err));
}