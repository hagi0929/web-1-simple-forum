#!C:\Users\pc\anaconda3\python.exe
#-*- coding: utf-8 -*-
import sys
import codecs
import csv

# stdout의 인코딩을 UTF-8로 강제 변환한다
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
f = open('db.csv', 'r', encoding='utf-8')
contents = csv.reader(f)
print("Content-type: text/html; charset=utf-8\r\n")
print('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Title</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
<form>
    <div>
        <h1>게시판</h1>
        <a href="add.py" class="Small">게시글 올리기</a>
    </div>
    <div class="viewer">
        <ul>
''')
for i,lst in enumerate(contents):
    print(f'''
    <li>
        <a href="view.py?id={i}">
            {lst[0]}
        </a>
    </li>
            ''')

print('''
        </ul>
    </div>
</form>

</body>
<script type="text/javascript" src="main.js"></script>

</html>
''')