<?php
session_start();  

if(isset($_SESSION["myvalue"]))
{
	unset($_SESSION["myvalue"]);
	$_SESSION["details"]="login";
header('location:details.php');
}
else
{
    echo '<h1><font color="red">ACCESS DENIED</font></h1>';
    header('location:index.php');
}
?>