<?php
 session_start();
   ini_set('session.cache_limiter','public');
  session_cache_limiter(false);

if(isset($_SESSION["details"]))
{  
   $_SESSION['page']="page";
   unset($_SESSION['pages']);
  echo ' <!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Details</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://fonts.googleapis.com/css?family=Open+Sans:400,700" rel="stylesheet">
   <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
   <link rel="stylesheet" href="css/style.css" type="text/css" media="screen"/>
   <link rel="stylesheet" href="css/detail-style.css" type="text/css" media="screen"/>
<script type="text/javascript" src="scripts/details.js">
</script>
</head>
<body class="align">
<img src="tn-police.png" alt="TN police logo" width="200" height="200">
<form align="right" name="form1" method="post" action="index.php">
  <label class="logoutLblPos">
  <input name="submit2" type="submit" class="logout" id="submit2" value="Log Out">
  </label>
</form>
<p><font size="6" color="#ffffff"> TAMIL NADU UNIFORMED SERVICES RECRUITMENT BOARD </font></p>
<p><font size="4" color="#ffffff"> LASER BASED AUTOMATIC RUN TIMING DEVICE </font></p>
  <p><font size="4" color="#ffffff"> Choose the number of tracks from the Dropdown below </font></p>
<div class="navbar">
  <div class="dropdown">
    <button class="dropbtn" background-color="#d44179" onclick="myFunction()">Number of Tracks
      <i class="fa fa-caret-down"></i>
    </button>
    <div class="dropdown-content" id="myDropdown" name="trakc">
      <a href="nextpage/track1.php" value="1" name="track1">1 Track</a>
      <a href="nextpage/track2.php" value="2" name="track2">2 Tracks</a>
      <a href="nextpage/track3.php" value="3" name="track3">3 Tracks</a>
      <a href="nextpage/track4.php" value="4" name="track4">4 Tracks</a>
      <a href="nextpage/track5.php" value="5" name="track5">5 Tracks</a>
      <a href="nextpage/track6.php" value="6" name="track6">6 Tracks</a>
      <a href="nextpage/track7.php" value="7" name="track7">7 Tracks</a>
      <a href="nextpage/track8.php" value="8" name="track8">8 Tracks</a>
      <a href="nextpage/track9.php" value="9" name="track9">9 Tracks</a>
      <a href="nextpage/track10.php" value="10" name="track10">10 Tracks</a>
    </div>
  </div> 
</div>
  </body>
</html>
<footer>
   <p> &copy; Copyright 2017 Anna University. </p>
</footer>';}
else 
  {
    echo '<h1><font color="red">ACCESS DENIED</font></h1>';
    header('location:index.php');
}
?>