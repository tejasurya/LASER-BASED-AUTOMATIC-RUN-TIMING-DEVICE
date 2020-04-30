 <head>
    <meta charset="utf-8">
    <title>Details</title>
    <link rel="stylesheet" href="css/common_v1.css" type="text/css" media="screen" />
   <link rel="stylesheet" href="css/stopwatch_v1.css" type="text/css" media="screen" />
    <script type="text/javascript">
var i=0;
function myFunction() {
    document.getElementById('splitButton').style.visibility = 'hidden';
    var table = document.getElementById('savedTimeTable');
    var row = table.insertRow(i+1);
    var cell3 = row.insertCell(0);
    var cell2 = row.insertCell(1);
    i++;
    var label = document.createElement("input");
    label.setAttribute("id","sdisconnect"+i);
    label.setAttribute("type", "text");
    label.setAttribute("style", "width:600px");
    cell2.appendChild(label);

    var element = document.createElement("input");
    element.setAttribute("type", "text");
    element.setAttribute("id", "sconnect"+i);
    element.setAttribute("style", "width:600px");
    cell3.appendChild(element);
}
var j=0;
function myFunction1() {
    document.getElementById('splitButton1').style.visibility = 'hidden';
    var table = document.getElementById('savedTimeTable1');
    var row = table.insertRow(j+1);
    var cell3 = row.insertCell(0);
    var cell2 = row.insertCell(1);
    j++;
    var label = document.createElement("input");
    label.setAttribute("id","fdisconnect"+j);
    label.setAttribute("type", "text");
    label.setAttribute("style", "width:600px");
    cell2.appendChild(label);

    var element = document.createElement("input");
    element.setAttribute("type", "text");
    element.setAttribute("id", "fconnect"+j);
    element.setAttribute("style", "width:600px");
    cell3.appendChild(element);
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
<button type="button" title="Split" id="splitButton"  class="mainButton green"  onclick="myFunction();"></button> 
<button type="button" title="Split1" id="splitButton1"  class="mainButton green"  onclick="myFunction1();"></button>     
<br><br>
<div class="align">
<p><font size="5" color="#000000"> LASER BASED AUTOMATIC RUN TIMING DEVICE </font></p>
</div>
<div class="align">
<p><font size="5" color="#000000"> STARTING BLOCK </font></p>
</div>
    <div id="savedTimePlace">
    <table id="savedTimeTable" cellspacing="0" cellpadding="20" >
      <thead>
        <tr>
                       <th class="columnType6 columnHead" bgcolor="#7fff00" id="Connected"><p style="text-align:left">       Connected</p> </th>
                       <th class="columnType7 columnTail" id="Disconnected">Disconnected</p> </th>

        </tr>
      </thead>
          <tbody>
      </tbody>
    </table>
  </div>
</div>
<div class="align">
<p><font size="5" color="#000000"> FINISH BLOCK</font></p>
</div>
<div id="savedTimePlace1">
    <table id="savedTimeTable1" cellspacing="0" cellpadding="20" >
      <thead>
        <tr>
                       <th class="columnType6 columnHead" bgcolor="#7fff00" id="Connected"><p style="text-align:left">Connected</p> </th>
                       <th class="columnType7 columnTail" id="Disconnected">Disconnected</p> </th>

        </tr>
      </thead>
          <tbody>
      </tbody>
    </table>
  </div> 
<footer>
   <p> &copy; Copyright 2017 Anna University. </p>
</footer>
</div>
  </body>
</html>