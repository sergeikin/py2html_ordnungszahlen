# -*- coding: utf-8 -*-
import sys, os, glob

def html_head():
    text2html = """<html>
<head>
<title>Table of enumerations</title>
</head>
<body>
<h3>The table of enumerations from 1st to 1,000,000th</h3>
###UNDER CONSTRUCTION!###<br>
<table border="1" width="1000">
<tbody>"""
    return text2html

def html_body():
    text2html = """ """
    text2html = text2html + """<tr>"""
    for i in range(10):
        text2html = text2html + """<td>"""
        j = i+1
        text2html = text2html + str(j)
        if j == 1:
            text2html = text2html +"st"
        elif j == 2:
            text2html = text2html +"nd"
        elif j == 3:
            text2html = text2html +"rd"
        else:
            text2html = text2html +"th"
        text2html = text2html + """</td>"""
    text2html = text2html + """</tr>"""
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