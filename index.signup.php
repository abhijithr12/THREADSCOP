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

       
        .form-container {
            width: 400px;
            margin: 50px auto;
            background-color: #1c1c1c;
            padding: 20px;
            border-radius: 10px;
        }

        .form-container h2 {
            text-align: center;
            color: #C19A6B;
            margin-bottom: 20px;
        }

        
        .form-container input {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border-radius: 25px;
            border: none;
            font-size: 16px;
            outline: none;
            background-color: #2c2c2c;
            color: white;
        }

        .form-container input::placeholder {
            color: #aaa; 
        }

        
        .form-container button {
            width: 100%;
            padding: 10px;
            border-radius: 25px;
            background-color: #C19A6B;
            border: none;
            color: white;
            font-size: 16px;
            cursor: pointer;
            transition: background-color 0.3s;
        }

        .form-container button:hover {
            background-color: #C19A6B;
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
    </div>

    
    <div class="form-container">
        <h2>Create an Account</h2>
        <form action="index.signup.php" method="POST">
            <input type="text" name="username" placeholder="Username" required>
            <input type="email" name="email" placeholder="Email" required>
            <input type="password" name="password" placeholder="Password" required>
            <button type="submit" name="SignUp">Sign Up</button>
        </form>
    </div>

  
    <div class="footer">
        <p>&copy; 2024 THREADSCOPE. All rights reserved.</p>
    </div>

</body>
</html>
<?php

$conn = mysqli_connect("localhost", "root", "", "website login");


if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}


if (isset($_POST['SignUp'])) {
    $username = mysqli_real_escape_string($conn, $_POST['username']);
    $password = mysqli_real_escape_string($conn, $_POST['password']);

    
    $sql = "SELECT * FROM logindetails WHERE username = '$username'";
    $result = mysqli_query($conn, $sql);

    if ($result) {
        $row = mysqli_fetch_assoc($result);
        if ($row) {
            $resultPassword = $row['password'];
           
            if ($password === $resultPassword) {
               
                header("Location: index2.php");
                exit();
            } else {
                echo "<script>alert('Login unsuccessful: Incorrect password');</script>";
            }
        } else {
            echo "<script>alert('Login unsuccessful: Username not found');</script>";
        }
    } else {
        echo "Error: " . mysqli_error($conn);
    }
}


mysqli_close($conn);
?>
