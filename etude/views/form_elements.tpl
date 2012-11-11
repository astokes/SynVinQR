<!DOCTYPE html> 
<!-- 
-- Associated with ../form_elements.py 
-- Contains examples of the major form elements without the layout 
-- clutter of forms or div/span/CSS elements.  
--> 
<html>
<head>
<title>Bottle Form Elements</title>
</head>
<body>

<!-- working through http://www.w3schools.com/html/html_forms.asp
-->

<form action="/text" method="POST" enctype="multipart/form-data">
Q: <input type="text" name="question"><br/>
A: <input type="text" name="answer"><br/>
<input type="submit" value="Submit"/>
</form>
<br/>

<form action="/password" method="POST" enctype="multipart/form-data">
Password: <input type="password" name= password><br/>
For security and simplicity password must consist of symbols only<br/>
<input type="submit" value="Submit"/>
</form>
<br/>

<form action="/radiobutton" method="POST" enctype="multipart/form-data"> 
<!-- the reference shows no default selection -->
<input type="radio" name="sex" value="male"/>Male<br/>
<input type="radio" name="sex" value="female"/>Female<br/>
<input type="submit" value="Submit"/>
</form>
<br/>

<form action="/radcook" method="POST" enctype="multipart/form-data"> 
<input type="radio" name="purience" value="prude"/>Prude<br/>
<input type="radio" name="purience" value="pervert"/>Pervert<br/>
<input type="submit" value="Submit"/>
</form>
<br/>

<form action="/checkbox" method="POST" enctype="multipart/form-data"> 
<input type="checkbox" name="phoneOS" value="Android"/>I own an Android phone<br/>
<input type="checkbox" name="phoneOS" value="iOS"/>I own an iOS phone<br/>
<input type="checkbox" name="phoneOS" value="Blackberry"/>I once owned a Blackberry phone<br/>
<input type="checkbox" name="phoneOS" value="Symbian"/>I once owned a Symbian phone<br/>
<input type="submit" value="Submit"/>
</form>
</br>


<!-- TODO
-- figure out <input type='checkbox' name='lang[en]'/>
-- from http://stackoverflow.com/questions/6412319/array-for-checkboxes-in-html-forms
-->

<!-- TOOD 
-- dropdown
-- dropdown with default selection
-- textarea 
-- buttons
-- fieldsets and other formatting 
-- HTML5: datalist, keygen, output
-->

</body>
</html>

