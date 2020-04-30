<?php

require "init.php";
$name=$_POST['name'];
$trackno=$_POST['track'];
$names=$_POST['names'];
$tracknos=$_POST['tracks'];
$namess=$_POST['namess'];
$tracknoss=$_POST['trackss'];
$sql="INSERT INTO details (name,trackno) VALUES ('$name','$trackno');";
mysqli_query($con,$sql);
$sql="INSERT INTO details (name,trackno) VALUES ('$names','$tracknos');";
mysqli_query($con,$sql);
$sql="INSERT INTO details (name,trackno) VALUES ('$namess','$tracknoss');";
mysqli_query($con,$sql);
$sql="DELETE FROM tracks;";
mysqli_query($con,$sql);
$sql="INSERT INTO tracks (track) VALUES ('3');";
mysqli_query($con,$sql);
mysqli_close($con);
session_start();
unset($_SESSION['page']);
$_SESSION['details']="login";
if( isset($_SESSION['pages']))
{
  echo '<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Details</title>
    <script type="text/javascript">
    function validateForm() {
     <?php
       session_start();
       $_SESSION["myvalue"]="admin";
       unset($_SESSION["page"]);
       unset($_SESSION["pages"]);
     ?>
     } 
  </script>
  <style>
    .align {
  -webkit-box-align: center;
      -ms-flex-align: center;
          align-items: center;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-orient: vertical;
  -webkit-box-direction: normal;
      -ms-flex-direction: column;
          flex-direction: column;
  -webkit-box-pack: center;
      -ms-flex-pack: center;
          justify-content: center;
}
.colur{
      background-color: #d44179;
      color: #ffffff;
      padding: 12px 20px;
}
  .container div {
    display: inline-block;
     padding: 16px;
    }
    .logoutLblPos{
   position:fixed;
   right:75px;
   top:50px;
   background-color: #d44179;
   color: white;
}
.logout{
         background-color: #d44179;   
         padding: 16px 16px;
         color: white;
}
  </style>
</head>
<body>
<div id="container">
<img src="tn-police.png" alt="TN police logo" width="200" height="200" align="left">
 <br><br><br><br>
 <p><font size="6" color="#000000"> TAMIL NADU UNIFORMED SERVICES RECRUITMENT BOARD </font></p>
</div>
<form align="right" name="form1" method="post" action="/login/index.php">
  <label class="logoutLblPos">
  <input name="submit2" type="submit" class="logout" id="submit2" value="Log Out">
  </label>
</form>
<br><br>
<div class="align">
<p><font size="5" color="#000000"> LASER BASED AUTOMATIC RUN TIMING DEVICE </font></p>
 <h1>Registration successful</h1>
<h2>Now Click on the StartRace batch file to start the race</h2>
<form method="post" action="/login/details.php" onsubmit="return validateForm()">
  <input name="home" type="submit" class="colur" id="submit3" value="To start next race,Click here">
  </form>
  </div>
  </form>
  </div> 
<footer>
   <p> &copy; Copyright 2017 Anna University. </p>
</footer>
</div>
  </body>
</html>';
}
else {
  echo '<h1><font color="red">ACCESS DENIED</font></h1>';
header('location:/login/index.php');
}
?>