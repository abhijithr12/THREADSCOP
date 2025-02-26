<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>THREADSCOPE</title>
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
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        .header {
            background-color: #C19A6B; 
            padding: 15px;
            text-align: center;
            width: 100%;
        }

        .header h1 {
            color: white;
            font-size: 32px;
            margin-bottom: 10px;
        }

        .search-bar {
            display: flex;
            justify-content: center;
            margin-top: 10px;
        }

        .search-bar input {
            width: 70%;
            padding: 10px;
            border-radius: 25px;
            border: none;
            font-size: 16px;
            outline: none;
        }

        .search-bar button {
            padding: 10px;
            border-radius: 25px;
            background-color: rgb(209, 117, 4);
            border: none;
            color: white;
            font-size: 16px;
            margin-left: 10px;
            cursor: pointer;
        }

        .search-bar button:hover {
            background-color: rgb(247, 247, 247);
        }

        .nav {
            display: flex;
            justify-content: space-around;
            background-color: #1a1a1a;
            padding: 10px;
            width: 100%;
        }

        .nav a {
            color: #C19A6B;
            text-decoration: none;
            font-size: 18px;
        }

        .nav a:hover {
            color: #C19A6B;
        }

        .chat-container {
            margin-top: 30px;
            width: 50%;
            background-color: #1c1c1c;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
        }

        #chat-box {
            height: 300px;
            overflow-y: auto;
            background: #2c2c2c;
            padding: 10px;
            border-radius: 10px;
            margin-bottom: 10px;
        }

        input {
            width: 80%;
            padding: 10px;
            border-radius: 5px;
            border: none;
            margin-top: 10px;
        }

        button {
            padding: 10px;
            background-color: rgb(209, 117, 4);
            border: none;
            color: white;
            font-size: 16px;
            cursor: pointer;
            border-radius: 5px;
        }

        button:hover {
            background-color: rgb(247, 247, 247);
            color: black;
        }

        .footer {
            text-align: center;
            padding: 15px;
            background-color: #C19A6B;
            margin-top: 20px;
            color: white;
            width: 100%;
        }
    </style>
</head>
<body>

    <div class="header">
        <h1>THREADSCOPE</h1>
        <div class="search-bar">
            <input type="text" placeholder="Search questions...">
            <button>Search</button>
        </div>
    </div>

    <div class="nav">
        <a href="index2.php">Home</a>
        <a href="index2.about.php">About</a>
        <a href="index.community.php">Community</a>
        <a href="#">Answer</a>
        <a href="index.ai.php">AI Feature</a>
        <a href="index.profile.php">Profile</a>
    </div>

    <div class="chat-container">
        <h1>SUNI MWON BOT</h1>
        <div id="chat-box"></div>
        <input type="text" id="user-input" placeholder="Type a message...">
        <button onclick="sendMessage()">Send</button>
    </div>

    <script>
        function sendMessage() {
            const userMessage = document.getElementById("user-input").value.trim();
            if (userMessage === "") return;

            fetch("http://127.0.0.1:5000/chat", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ message: userMessage })
            })
            .then(response => response.json())
            .then(data => {
                document.getElementById("chat-box").innerHTML += 
                    `<p><strong>You:</strong> ${userMessage}</p>
                     <p><strong>Bot:</strong> ${data.reply}</p>`;
            })
            .catch(error => {
                console.error("Error:", error);
                document.getElementById("chat-box").innerHTML += "<p>Failed to contact AI server.</p>";
            });

            document.getElementById("user-input").value = "";
        }
    </script>

    <div class="footer">
        <p>&copy; 2025 THREADSCOPE. All rights reserved.</p>
    </div>

</body>
</html>
