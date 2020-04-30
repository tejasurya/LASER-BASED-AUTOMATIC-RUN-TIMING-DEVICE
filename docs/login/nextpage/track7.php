<?php
 session_start();
if(isset($_SESSION['page']))
{
    $_SESSION['pages'] = "nextpage";
    unset($_SESSION["details"]);
      echo ' <!DOCTYPE html>
<html> 
<head>
    <meta charset="utf-8">
    <title>Register</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://fonts.googleapis.com/css?family=Open+Sans:400,700" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
   <link rel="stylesheet" href="css/style.css" type="text/css" media="screen"/>
   <link rel="stylesheet" href="css/detail-style.css" type="text/css" media="screen"/>
   <style>
input[type=text], input[type=password] {
    width: 50%;
    padding: 12px 20px;
    margin:0 auto;
    width:500px;
    display: inline-block;
    border: 1px solid #ccc;
    box-sizing: border-box;
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
button {
    background-color: #d44179;
    color: white;
    padding: 14px 20px;
    margin:0 auto;
    width:200px;
    text-align:center;
    border: none;
    cursor: pointer;
}
.container {
    padding: 16px;
}
@media screen and (max-width: 300px) {
    .signupbtn {
       width: 100%;
       align: center;
    }
  .container div {
    display: inline-block;
    }
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
<p><font size="4" color="#000000"> LASER BASED AUTOMATIC RUN TIMING DEVICE </font></p>
<form action="trackssssss.php"  method="post" style="border:1px solid #ccc">
  <div class="container">
    <label><b>First Athlete</b></label>
    <br><input type="text" placeholder="Enter name" name="name" required>
    <br><label><b>Track number</b></label>
    <br><input type="text" placeholder="track number" value="1" name="track" readonly>    
    <br><label><b>Second Athlete</b></label>
    <br><input type="text" placeholder="Enter name" name="names" required>
    <br><label><b>Track number</b></label>
    <br><input type="text" placeholder="track number" value="2" name="tracks" readonly>    
     <br><label><b>Third Athlete</b></label>
    <br><input type="text" placeholder="Enter name" name="namess" required>
    <br><label><b>Track number</b></label>
    <br><input type="text" placeholder="track number" value="3" name="trackss" readonly>
    <br><label><b>Fourth Athlete</b></label>
    <br><input type="text" placeholder="Enter name" name="namesss" required>
    <br><label><b>Track number</b></label>
    <br><input type="text" placeholder="track number" value="4" name="tracksss" readonly>
     <br><label><b>Fifth Athlete</b></label>
    <br><input type="text" placeholder="Enter name" name="namessss" required>
    <br><label><b>Track number</b></label>
    <br><input type="text" placeholder="track number" value="5" name="trackssss" readonly>
     <br><label><b>Sixth Athlete</b></label>
    <br><input type="text" placeholder="Enter name" name="namesssss" required>
    <br><label><b>Track number</b></label>
    <br><input type="text" placeholder="track number" value="6" name="tracksssss" readonly>
     <br><label><b>Seventh Athlete</b></label>
    <br><input type="text" placeholder="Enter name" name="namessssss" required>
    <br><label><b>Track number</b></label>
    <br><input type="text" placeholder="track number" value="7" name="trackssssss" readonly>
     <div class="align">
      <br>
      <br>
      <br>
      <button type="submit" class="signupbtn">Save</button>
      </div></div>
    </div>
<footer>
   <p> &copy; Copyright 2017 Anna University. </p>
</footer>
</form>
</body>
</html>';}
else {
  echo '<h1><font color="red">ACCESS DENIED</font></h1>';
header('location:/login/index.php');
}
?>