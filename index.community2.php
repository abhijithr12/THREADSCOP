<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>THREADSCOPE Community</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #121212;
            color: #ffffff;
            text-align: center;
        }

        .container {
            width: 50%;
            margin: 20px auto;
            background-color: #1c1c1c;
            padding: 20px;
            border-radius: 10px;
        }

        input, textarea, button {
            width: 100%;
            margin-top: 10px;
            padding: 10px;
            border: none;
            border-radius: 5px;
            font-size: 16px;
        }

        button {
            background-color: #C19A6B;
            color: white;
            cursor: pointer;
        }

        button:hover {
            background-color: #a0744e;
        }

        .post {
            background-color: #2c2c2c;
            padding: 15px;
            margin: 10px 0;
            border-radius: 5px;
            text-align: left;
        }
    </style>
</head>
<body>

    <h1>THREADSCOPE Community</h1>
    <div class="container">
        <h2>Create a Post</h2>
        <input type="text" id="post-title" placeholder="Title">
        <textarea id="post-content" rows="4" placeholder="Write something..."></textarea>
        <button onclick="publishPost()">Publish</button>
    </div>

    <div class="container">
        <h2>Community Posts</h2>
        <div id="posts"></div>
    </div>

    <script>
        function fetchPosts() {
            fetch("http://127.0.0.1:5000/posts")
                .then(response => response.json())
                .then(data => {
                    document.getElementById("posts").innerHTML = "";
                    data.forEach(post => {
                        document.getElementById("posts").innerHTML += `
                            <div class="post">
                                <h3>${post.title}</h3>
                                <p>${post.content}</p>
                                <small>Posted on: ${post.date_posted}</small>
                            </div>
                        `;
                    });
                })
                .catch(error => {
                    console.error("Error fetching posts:", error);
                    alert("Failed to load posts. Please try again later.");
                });
        }

        function publishPost() {
            const title = document.getElementById("post-title").value.trim();
            const content = document.getElementById("post-content").value.trim();
            const user_id = 1;  

            if (!title || !content) {
                alert("Please enter both title and content.");
                return;
            }

            fetch("http://127.0.0.1:5000/posts", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ title, content, user_id }) 
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error("Failed to publish post.");
                }
                return response.json();
            })
            .then(data => {
                alert("Post published successfully!");
                document.getElementById("post-title").value = "";
                document.getElementById("post-content").value = "";
                fetchPosts();
            })
            .catch(error => {
                console.error("Error publishing post:", error);
                alert("Failed to publish post. Please try again.");
            });
        }

        
        fetchPosts();
    </script>

</body>
</html>

