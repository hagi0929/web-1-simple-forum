#!C:\Users\pc\anaconda3\python.exe
# -*- coding: utf-8 -*-
import sys
import codecs
import csv
import cgi

print("Content-type: text/html; charset=utf-8\r\n\n")
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
r = csv.reader(open('db.csv', 'r', encoding='utf-8'))
form = cgi.FieldStorage()
try:
    num = int(form["id"].value)
except:
    num = 1
sip = list(filter(None, list(r)))
view_target = sip[int(num)]

print(f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>title</title>
    <link rel="stylesheet" href="style.css">
    <script type = "text/javascript" src="main.js"></script>
</head>
<body>
    <div>
        <form id="del" action="del.py" method="POST">
            <input type="hidden" name="id" value="{num}">
            <input type="hidden" name="pw" id="hidden_pw1">
            <button onclick="check_pw('del')">삭제</button>
        </form>
        <form id="edit" action="edit.py" method="POST">
            <input type="hidden" name="id" value="{num}">
            <input type="hidden" name="pw" id="hidden_pw2">
            <button onclick="check_pw('edit')">수정</button>
        </form>
    </div>
    <div>
        <div class="title Small">{view_target[0]}</div>  
        <div class="viewer">{view_target[2]}</div>
    </div>
</body>

</html>
''')
