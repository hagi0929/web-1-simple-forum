#!C:\Users\pc\anaconda3\python.exe
#-*- coding: utf-8 -*-
import sys
import codecs

# stdout의 인코딩을 UTF-8로 강제 변환한다
print("Content-type: text/html; charset=utf-8\r\n")
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
print('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="add">
        <form action="fr.py" method="POST">
            <div class="single-line">
                <label for="Title">Title: </label>
                <input type="text" name="Title" id="Title" required>
                <label for="Password">Password: </label>
                <input type="text" name="Password" id="Password">
            </div>
            <div class="content">
                <label for="Content">content: </label>
                <textarea name="Content" id="Content" cols="50" rows="5" required></textarea>
            </div>
            <input type="submit" value="전송">
        </form>
    </div>
</body>
</html>
''')