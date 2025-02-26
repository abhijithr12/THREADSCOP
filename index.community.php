<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Community Interface</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: Arial, sans-serif;
            background-color: #1d1d1d; 
            color: #f0f0f0; 
        }

        .header {
            background-color: #C19A6B;
            padding: 15px;
            text-align: center;
        }

        h1 {
            text-align: center;
            font-size: 32px;
            margin-bottom: 20px;
        }

        .container {
            max-width: 900px;
            margin: 0 auto;
            padding: 20px;
        }

        .nav {
            display: flex;
            justify-content: space-between;
            background-color: #2c2c2c;
            padding: 15px;
            border-radius: 8px;
        }

        .nav a {
            color: #C19A6B;
            text-decoration: none;
            font-size: 18px;
            margin-right: 15px;
        }

        .nav a:hover {
            color: #C19A6B;
        }

        .nav button {
            padding: 10px 20px;
            border-radius: 25px;
            background-color: #C19A6B;
            border: none;
            color: white;
            cursor: pointer;
        }

        .nav button:hover {
            background-color: #a0744e;
        }

        .community-section {
            margin-top: 20px;
        }

        .community-section h2 {
            color: #C19A6B;
            margin-bottom: 10px;
            font-size: 24px;
        }

        .community-post {
            background-color: #333333;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 20px;
        }

        .community-post h3 {
            color: #C19A6B;
            margin-bottom: 10px;
        }

        .community-post p {
            margin-bottom: 10px;
        }

        .community-post a {
            color: #C19A6B;
            text-decoration: underline;
        }

        .community-post a:hover {
            color: #a0744e;
        }

        .popular-threads {
            background-color: #2c2c2c;
            padding: 20px;
            border-radius: 8px;
        }

        .popular-threads h3 {
            color: #C19A6B;
            margin-bottom: 15px;
        }

        .popular-threads ul {
            list-style: none;
        }

        .popular-threads ul li {
            margin-bottom: 10px;
        }

        .popular-threads ul li a {
            color: #C19A6B;
            text-decoration: none;
        }

        .popular-threads ul li a:hover {
            color: #a0744e;
        }

        .footer {
            text-align: center;
            padding: 15px;
            background-color: #C19A6B;
            margin-top: 20px;
            color: white;
        }
    </style>
</head>
<body>

    <div class="header">
        <h1>THREADSCOPE</h1>
        <h3><center>COMMUNITY</center></h3>
    </div>
        
    <div class="container">
        <div class="nav">
            <div>
                <a href="index2.php">Home</a>
                <a href="#">Discussion</a>
                <a href="#">Ask a Question</a>
            </div>
            <a href="index.community2.php"><button>Start a New Community</button></a>
        </div>

        <!-- Latest Discussions -->
        <div class="community-section">
            <h2>Latest Discussions</h2>
            <div id="latest-discussions">
                <p>Loading discussions...</p>
            </div>
        </div>

        <!-- Popular Threads -->
        <div class="popular-threads">
            <h3>Popular Threads</h3>
            <ul>
                <li><a href="#">How AI Improves Threat Intelligence Sharing Platforms</a></li>
                <li><a href="#">Best Practices for AI-Based Phishing Detection</a></li>
                <li><a href="#">Tools for Detecting Malware with AI</a></li>
                <li><a href="#">Preventing Social Engineering Attacks with AI</a></li>
            </ul>
        </div>
    </div>

    <div class="footer">
        <p>&copy; 2024 AI Malware Detection Community. All rights reserved.</p>
    </div>

    <script>
        function fetchPosts() {
            fetch("http://127.0.0.1:5000/posts")
                .then(response => response.json())
                .then(data => {
                    const discussionsContainer = document.getElementById("latest-discussions");
                    discussionsContainer.innerHTML = "";

                    if (data.length === 0) {
                        discussionsContainer.innerHTML = "<p>No discussions yet. Be the first to start one!</p>";
                        return;
                    }

                    
                    data.slice(0, 3).forEach(post => {
                        discussionsContainer.innerHTML += `
                            <div class="community-post">
                                <h3>${post.title}</h3>
                                <p>${post.content.substring(0, 100)}...</p>
                                <a href="index.community2.php">Join the discussion</a>
                            </div>
                        `;
                    });
                })
                .catch(error => {
                    console.error("Error fetching posts:", error);
                    document.getElementById("latest-discussions").innerHTML = "<p>Failed to load discussions.</p>";
                });
        }

      
        fetchPosts();
    </script>

</body>
</html>
