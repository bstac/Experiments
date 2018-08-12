import cgi
#import sys
#sys.stdout.write("Content-type: text/html\r\n\r\n<p>Body</p>")
#python -m http.server --cgi

print("Content-type: text/html; charset=utf-8\n\n")
print('<!DOCTYPE html>\n\n')
print('<html>')
print('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
print(''' <head>
<style>
body {
    background-color: lightblue;
}

h1 {
    color: white;
    text-align: center;
}

h3 {
    color: red;
    font-size: 30px;
}

p {
    font-family: verdana;
    font-size: 20px;
}
</style>
</head> ''')
print('''<body> <script>
function changeImage()
{
var txt = document.forms["myForm"]["user"].value
document.getElementById("set").innerHTML = txt.length;
document.getElementById("sett").innerHTML = txt;
}
</script>
''')
print('<h1>Hello Program!</h1>')

form = cgi.FieldStorage()
if(form.getvalue('user')):
    name = form.getvalue('user')
    print('<h2>Hello ' + str(name) + '! Thanks for the Hits!</h2>')
if(form.getvalue('happy')):
    print('<p> Yay! I''m happy too! </p>')
if(form.getvalue('sad')):
    print('<p> Oh no! Why are you sad? </p>')

print('<form name="myForm" method=''post'' action=''test.py''>')
print('<h3 id="set">0</h3>')
print('<h3 id="sett"> </h3>')
print('<p>Name: <input id="demo" type=''text'' name=''user'' ')
print('onclick="changeImage()"/></p>')
print('<input type=''checkbox'' name=''happy'' /> Happy')
print('<input type=''checkbox'' name=''sad'' /> Sad')
print('<input type=''submit'' value=''Submit'' />')
print('</form>')
print('<form name="myForm2" method=''post'' action=''file.py''>')
print('<input type=''submit'' value=''Submit'' />')
print('</form>')
print('</body></html>')

