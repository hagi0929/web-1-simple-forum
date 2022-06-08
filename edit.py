#!C:\Users\pc\anaconda3\python.exe
# -*- coding: utf-8 -*-
import sys
import codecs
import csv
import cgi

print("Content-type: text/html; charset=utf-8\r\n")
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

r = csv.reader(open('db.csv', 'r', encoding='utf-8'))
form = cgi.FieldStorage()
num = int(form["id"].value)
sip = list(filter(None, list(r)))
try:
    ps = form["pw"].value
except:
    ps = ''
if sip[num][1] == ps:
    view_target = sip[num]
    print(f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <link rel="stylesheet" href="style.css">
    <title>Title</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
<div>
    <form id="del" action="editit.py" method="POST">
        <input type="hidden" name="id" value="{num}">
        <div>
            <input name="Title" type="text" class="title Small" value="{view_target[0]}">
        </div>
        <div>
            <textarea name="Content" id="Content" cols="100" rows="10" required>{view_target[2]}</textarea>
        </div>
        <input type="submit">
    </form>
</div>
</body>
</html>
''')
else:
    print(sip[num], ps)
    print("failed")
