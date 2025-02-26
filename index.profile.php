<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>THREADSCOPE
          User Profile</title>
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

       
        .nav {
            display: flex;
            justify-content: space-between; 
            align-items: center;
            background-color: #1a1a1a;
            padding: 10px;
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

        
        .profile {
            display: flex;
            justify-content: center;
            padding: 20px;
        }

        .profile-info {
            width: 60%;
            background-color: #1c1c1c;
            padding: 20px;
            border-radius: 10px;
            margin-right: 20px;
        }

        .profile-info h2 {
            color: #C19A6B;
        }

        .profile-info p {
            margin-top: 10px;
        }

        
        .activity-feed {
            width: 35%;
            background-color: #1c1c1c;
            padding: 20px;
            border-radius: 10px;
        }

        .activity-feed h3 {
            color: #C19A6B;
        }

        .activity {
            background-color: #2c2c2c;
            padding: 15px;
            margin-bottom: 15px;
            border-radius: 10px;
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
        <h1 align:centre>THREADSCOPE</h1>
    </div>

   
    <div class="nav">
        <div>
            <a href="index2.php">Home</a>
            <a href="chatbot.php">ChatBot</a>
            <a href="index2.about.php">About</a>
            <a href="index.community.php">Commmunity</a>
            <a href="#">Answer</a>
            <a href="index.ai.php">AI Feature</a>
            <a href="#">Community</a>
            <a href="#">Answer</a>
            
        </div>
    </div>
     <div>
          <h2><centre>User Profile</centre></h2>
    </div>
    
    <div class="profile">
        <div class="profile-info">
            <h2>Profile Information</h2>
            <p><strong>Name:</strong> abhi1</p>
            <p><strong>Email:</strong> apppozx123@gmail.com </p>
            <p><strong>Bio:</strong> Tech enthusiast and software developer. Always eager to learn new technologies.</p>
            <p><strong>Joined:</strong> February 2025</p>
        </div>

       
        <div class="activity-feed">
            <h3>Your Activity</h3>
            <div class="activity">
                <p><strong>Answered:</strong> How do threads improve performance in modern processors?</p>
            </div>
            <div class="activity">
                <p><strong>Asked:</strong> What is thread intelligence in computing?</p>
            </div>
            <div class="activity">
                <p><strong>Commented:</strong> Great insights on malware attacks!</p>
            </div>
        </div>
    </div>

    
    <div class="footer">
        <p>&copy; 2024 THREADSCOPE. All rights reserved.</p>
    </div>

</body>
</html>
