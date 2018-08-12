import cgi
#import sys
#sys.stdout.write("Content-type: text/html\r\n\r\n<p>Body</p>")
#python -m http.server --cgi

print("Content-type: text/html; charset=utf-8\n\n")
print('<!DOCTYPE html>\n\n')
print('<html>')
print('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
print(''' <!DOCTYPE html>
<style>
* {
  box-sizing: border-box;
}
.menu {
  float:left;
  width:20%;
  text-align:center;
}
.menuitem {
  background-color:#22e5e5;
  padding:8px;
  margin-top:7px;
}
.main {
  float:left;
  width:60%;
  padding:0 20px;
}
.right {
  background-color:#e5bbe5;
  float:left;
  width:20%;
  padding:15px;
  margin-top:7px;
  text-align:center;
}

@media only screen and (max-width:620px) {
  /* For mobile phones: */
  .menu, .main, .right {
    width:100%;
  }
}
</style>
<script>
function loadDoc() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      document.getElementById("demo").innerHTML = this.responseText;
    }
  };
  xhttp.open("POST", "demo.bat", true);
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhttp.send("fname=Henry&lname=Ford");
}
function loadDoc2() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      document.getElementById("demo").innerHTML = this.responseText;
    }
  };
  xhttp.open("POST", "demo.py", true);
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhttp.send();
}
function loadDoc3() {
   var form = document.createElement("form");
    form.setAttribute("method", "POST");
    form.setAttribute("action", "file.py");
    form.submit();
}
</script>
</head>
<body style="font-family:Verdana;color:#bbaaca;">

<div style="background-color:#e577ff;padding:15px;text-align:center;">
  <h1>Hello World</h1>
</div>

<div style="overflow:auto">
  <div class="menu">
    <div class="menuitem">Link 1</div>
    <div class="menuitem">Link 2</div>
    <div class="menuitem">Link 3</div>
    <div class="menuitem" onclick="loadDoc()">test</div>
    <div class="menuitem" onclick="loadDoc2()">story</div>
    <div class="menuitem" onclick="loadDoc3()">File</div>
  </div>

  <div class="main">
    <h2>Lorum Ipsum</h2>
    <p id="demo"></p>
  </div>

  <div class="right">
    <h2>About</h2>
    <p>Lorem ipsum dolor sit amet, consectetuer adipiscing elit.</p>
  </div>
</div>

<div style="background-color:#4466e5;
text-align:center;padding:10px;margin-top:7px;">Brandon Stack</div>

</body>
</html>
 ''')

