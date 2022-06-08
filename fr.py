#!C:\Users\pc\anaconda3\python.exe
# -*- coding: utf-8 -*-
import sys
import codecs
import csv
import cgi

# stdout의 인코딩을 UTF-8로 강제 변환한다
print("Content-type: text/html; charset=utf-8\r\n")
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
r = csv.reader(open('db.csv', 'r', encoding='utf-8'))
form = cgi.FieldStorage()
title = str(form["Title"].value)
try:
    ps = str(form["Password"].value)
except:
    ps = ''
con = str(form["Content"].value)
sip = list(filter(None, list(r)))
fields = [title, ps, con]
sip.append(fields)
w = csv.writer(open('db.csv', 'w', encoding='utf-8',newline=""))
w.writerows(sip)

print('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta http-equiv="refresh" content="0;url=http://127.0.0.1/index.py" /> 
    <title>Title</title>
</head>
<body>

</body>
</html>
''')