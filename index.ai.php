<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Malware Detection Interface</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: Arial, sans-serif;
            background-color: #121212;
            color: #ffffff;
            text-align: center;
            padding: 20px;
        }
        .header {
            background-color: #C19A6B; 
            padding: 15px;
            text-align: center;
        }
        h1 {
            color: #eaedf0;
            margin-bottom: 20px;
        }
        .nav a {
            color: #C19A6B;
            text-decoration: none;
            font-size: 18px;
            margin-right: 15px; /* Add spacing between links */
        }

        .nav a:hover {
            color: #C19A6B;
        }

        .card {
            background-color: #1c1c1c;
            padding: 20px;
            border-radius: 15px;
            margin-bottom: 20px;
        }

        input[type="text"], input[type="file"] {
            width: 60%;
            padding: 10px;
            margin: 10px 0;
            border-radius: 25px;
            border: none;
            font-size: 16px;
            outline: none;
        }

        button {
            padding: 10px 20px;
            border-radius: 25px;
            background-color: #C19A6B;
            border: none;
            color: white;
            font-size: 16px;
            cursor: pointer;
            margin-top: 10px;
        }

        button:hover {
            background-color: #C19A6B;
        }

        .result {
            font-size: 18px;
            margin-top: 20px;
        }

        .alert {
            color: #e53935;
        }

        .safe {
            color: #4caf50;
        }
    </style>
</head>
<body>
<div class="header">
    <h1>THREADSCOPE</h1>
    <h3> AI Malware Detection</h3>
</div>   
<div class="nav">
    <a href="index2.php">Home</a>
    <a href="index2.about.php">About</a>
        <a href="index.community.php">Commmunity</a>
        <a href="#">Answer</a>
        <a href="index.ai.php">AI Feature</a>
        <a href="index.profile.php">Profile</a>
        <a href="chatbot.php">ChatBot</a>
    
</div>

    
    <div class="card">
        <h2>Infectious Sites Tracker</h2>
        <p>You have visited <span id="infectious-count">0</span> infectious sites.</p>
    </div>

    
    <div class="card">
        <h2>Check for Malware</h2>
        <input type="text" id="url-input" placeholder="Enter URL to check...">
        <button onclick="checkInfectious()">Check URL</button>
        <div id="result" class="result"></div>
    </div>

    
    

    <div class="card">
        <h2>Upload a Suspicious File for Analysis</h2>
        <input type="file" id="file-upload">
        <button onclick="analyzeFile()">Analyze File</button>
        <div id="file-result" class="result"></div>
    </div>

    <script>
        let infectiousCount = 0;  

    function checkInfectious() {
       const url = document.getElementById('url-input').value;
       const resultDiv = document.getElementById('result');

       fetch("http://127.0.0.1:5000/predict", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ url: url })
        })
        .then(response => response.json())
        .then(data => {
           if (data.status === "malicious") {
               resultDiv.innerHTML = `<span class="alert">⚠ The URL is malicious! Proceed with caution!</span><br>
                                  <strong>Domain IP Address:</strong> ${data.ip_address}`;
            } else {
                resultDiv.innerHTML = `<span class="safe">✅ The URL is safe to visit.</span><br>
                                   <strong>Domain IP Address:</strong> ${data.ip_address}`;
            }
        })
        .catch(error => {
            resultDiv.innerHTML = '<span class="alert">Error checking the URL. Try again later.</span>';
        });
    }
  
        function analyzeFile() {
            const fileInput = document.getElementById('file-upload');
            const fileResultDiv = document.getElementById('file-result');

           
            if (!fileInput.files.length) {
                fileResultDiv.innerHTML = `<span class="alert">No file uploaded for analysis!</span>`;
                return;
            }

            const fileName = fileInput.files[0].name;
            
            const dangerousFiles = ['virus.exe', 'malware.docx'];  

            if (dangerousFiles.includes(fileName.toLowerCase())) {
                fileResultDiv.innerHTML = `<span class="alert">The file '${fileName}' contains malware! Do not open!</span>`;
            } else {
                fileResultDiv.innerHTML = `<span class="safe">The file '${fileName}' appears to be safe.</span>`;
            }
        }
    </script>

</body>
</html>
