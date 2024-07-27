document.getElementById('uploadForm').addEventListener('submit', function (e) {
    e.preventDefault();
    
    var fileInput = document.getElementById('fileInput');
    var file = fileInput.files[0];
    var reader = new FileReader();
    
    reader.onload = function (event) {
        var base64Image = event.target.result.split(',')[1];
        
        fetch('https://mdjyvs39bf.execute-api.us-east-1.amazonaws.com/prod/analyze', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ body: base64Image })
        })
        .then(response => response.json())
        .then(data => {
            displayResults(data);
        })
        .catch(error => {
            console.error('Error:', error);
            document.getElementById('result').innerHTML = 'An error occurred while analyzing the image.';
        });
    };
    
    reader.readAsDataURL(file);
});

function displayResults(data) {
    var resultDiv = document.getElementById('result');
    var html = '<h2>Image Analysis Results:</h2>';
    
    if (data.Labels && data.Labels.length > 0) {
        html += '<ul>';
        data.Labels.forEach(label => {
            html += `<li>${label.Name} (Confidence: ${label.Confidence.toFixed(2)}%)</li>`;
        });
        html += '</ul>';
    } else {
        html += '<p>No labels found in the image.</p>';
    }
    
    resultDiv.innerHTML = html;
}
