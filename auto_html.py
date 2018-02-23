# -*- coding: utf-8 -*-
import sys, os, glob

def html_head():
    text2html = """<html>
<head>
<title>Table of enumerations</title>
</head>
<body>
<h3>The table of enumerations from 1st to 1,000,000th</h3>
<table border="1" width="1000">
<tbody>"""
    return text2html

def html_body():
    text2html = """ ###UNDER CONSTRUCTION!### """
    return text2html

def html_foot():
    text2html = """</tbody>
</table>
</body>
</html>"""
    return text2html

def create_file(head, body, foot):
    f = open("Table_of_enumerations.html", "w")
    f.write(head+body+foot)
    f.close

head = html_head()
body = html_body()
foot = html_foot()

create_file(head,body,foot)