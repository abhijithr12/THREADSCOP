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
        }

       
        .header {
            background-color: #C19A6B; 
            padding: 15px;
            text-align: center;
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
            background-color:rgb(209, 117, 4);
            border: none;
            color: white;
            font-size: 16px;
            margin-left: 10px;
            cursor: pointer;
         
        }

       
        .search-bar button:hover {
            background-color:rgb(247, 247, 247)
        }
      
        
        .nav {
            display: flex;
            justify-content: space-around;
            background-color: #1a1a1a;
            padding: 10px;
        }

        .nav a {
            color: #C19A6B;
            text-decoration: none;
            font-size: 18px;
        }

        .nav a:hover {
            color: #C19A6B
        }

        
        .content {
            display: flex;
            justify-content: center;
            padding: 20px;
        }

        .feed {
            width: 60%;
            background-color: #1c1c1c;
            padding: 20px;
            border-radius: 10px;
        }

        .question {
            background-color: #2c2c2c;
            padding: 15px;
            margin-bottom: 20px;
            border-radius: 10px;
        }

        .question h2 {
            color: #C19A6B
        }

        .question p {
            margin-top: 10px;
        }

       
        .sidebar {
            width: 40%;
            padding: 20px;
        }

        .sidebar .card {
            background-color: #1c1c1c;
            padding: 15px;
            border-radius: 10px;
            margin-bottom: 20px;
        }

        .sidebar .card h3 {
            color: #C19A6B
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
        <div class="search-bar">
            <input type="text" placeholder="Search questions...">
            <button>Search</button>
        </div>
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

    <div class="content">
        <div class="feed">
            <div class="question">
                <h2> How do threads improve performance in modern processors?</h2>
                <p>Threads allow multiple tasks to be executed concurrently by breaking up a process into smaller units that can run independently. This parallelism helps in better CPU utilization, reducing idle time and increasing performance, especially in multi-core processors.</p>
            </div>

            <div class="question">
                <h2>What is thread intelligence in computing?</h2>
                <p>Thread intelligence refers to how threads (independent units of execution within a program) are managed and optimized to perform tasks efficiently. This involves intelligently handling resources, ensuring concurrency without conflicts, and maximizing parallel processing capabilities.</p>
            </div>
        </div>

       
        <div class="sidebar">
            <div class="card">
                <h3>Popular Topics</h3>
                <p>Remote Phishing</p>
                <p>Malware attack</p>
                <p>Best Antivirus for Malware</p>
            </div>

            <div class="card">
                <h3>Popular Community</h3>
                
                <p>CYBERSECURITY THREADS <button style="font-size:10px;padding: 10px;
 background-color:blue;color:white;border-radius:15px"><a href="index.community.php"> join </button></p></a>
                <p>CYBER SECURITY  <button style="font-size:10px;padding: 10px;
 background-color:blue;color:white;border-radius:15px"><a href="index.community.php">join </button></p></a>
                <p></p>
            </div>
        </div>
    </div>

    
    <div class="footer">
        <p>&copy; 2024 THREADSCOPE. All rights reserved.</p>
    </div>

</body>
</html>