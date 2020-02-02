<?php
$keyword=$_GET["keywords"];
$result=shell_exec('python resume_classification.py' . $keyword)
#echo gettype($result)
?>
<!DOCTYPE html>
<html>
<head>
	<title></title>

<style type="text/css">

table, th, td {
  border: 1px solid black;
  margin-top: 10px;
  margin-right: 1000px;
  
  border:3px solid black; 
}
th, td {
  padding: 1px;
  font-size: 20px;
  border:1px solid black;
}



.but {
  -webkit-transition-duration: 0.4s; /* Safari */
  transition-duration: 0.4s;
  padding: 10px;
  font-size:10px;
  text-align: center;
  color: #505ABC;
}



html,body{
background-color: #ffffff;
color: #687689;
font: normal 16px/1.5 Helvetica, Arial, sans-serif;
font-family: 'Jost*',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,'Helvetica Neue',Arial,sans-serif,'Apple Color Emoji','Segoe UI Emoji','Segoe UI Symbol';

}




#main{
background: #505ABC url(img/background.svg) no-repeat;
background-position: 50% 50%;
background-size: auto 100%;
color: #fff;
font-size: 15px;
width: 100%;
}


#intro{
float: left;
text-align: center;
width: 100%;
}

#intro h1{
font-size: 2.65em;
margin: 3.5em 0 0 0;
padding: 0;
line-height: 1.2em;
color: #fff;
font-weight: 500;
}

#intro h2{
margin: 0 0 1em 0;
padding: 0;
font-weight: 500;
}

#intro input.text{
background-color: #fff;
color: #4A65BC;
border: 2px solid #4052BC;
box-sizing: border-box;
display: inline-block;
width: 24em;
padding: 0 1.5em;
height: 3em;
font-size: 1.1em;
border-radius: 0.5em;
}

#intro .button{
background-color: #363A8E;
color: #fff;
display: inline-block;
height: 3em;
border-radius: 0.5em;
padding: 0 2em;
line-height: 3em;
font-size: 1.1em;
margin-left: 0.5em;
cursor: pointer;
border: none;
}

#intro .button:hover{
background-color: #051A7F;
}



</style>
</head>
<body bgcolor="powderblue">
<div class="intro">
	<div id="main">
	<center>
	<h1>
	<?php
	echo("Participants for $keyword:");?>
	</h1>
	<?php
	#$skills=$result

	$skills = json_decode($result, true);
	echo $skills[$keyword]
	#echo $skills
	#for ($row = 0; $row < count($skills); $row ++) {

	?>
	<!--<input type="radio"  name="k" value=""<?php echo $skills[$row]?>"">
-->
	<?php #echo $skills[$row]; } ?> 
	</center>
	</div>
<table style="width:100%" border='1'><br />

<?php

$filename = 'Data2.csv';

$the_big_array = []; 

// Open the file for reading
if (($h = fopen("{$filename}", "r")) !== FALSE) 
{
  // Each line in the file is converted into an individual array that we call $data
  // The items of the array are comma separated
  echo "<table border='1'><tr>";
  $data=array();
  error_reporting(0);
  while (($data = fgetcsv($h, 1000, ",")) !== FALSE) 
  {
    // Each individual array is being pushed into the nested array
	$the_big_array[] = $data;	
	if($data[4]=== "['']" or $data[0]=== NUll or $data[1]=== NUll or $data[2]=== NUll or $data[3]=== NUll or $data[5]=== NUll )
	{

	}
	else{
	echo"
	<tr>
	<th>$data[0]</th>
	<th>$data[1]</th>
	<th>$data[2]</th>
	<th>$data[3]</th>
	<th>$data[4]</th>
	<th>$data[5]</th>
	</tr>";	
	}
  }
  echo"</tr>";
  // Close the file
  fclose($h);
}

// Display the code in a readable format
echo "<pre>";
#var_dump($the_big_array);
echo "</pre>";

?>
</table>
</div>
<form class='but'><button>SEARCH</button></form>
</body>
</html>