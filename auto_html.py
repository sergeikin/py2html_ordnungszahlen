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
    for j in range(2):
        text2html = text2html + """<tr>"""
        for i in range(10):
            zahlenvergleich = j*10+i
            text2html = text2html + """<td>"""
            text2html = text2html + str(zahlenvergleich) #Zahl wird hinzugefügt
            if i == 1:
                text2html = text2html +"st"
            elif i == 2:
                text2html = text2html +"nd"
            elif i == 3:
                text2html = text2html +"rd"
            elif i == 11:
                text2html = text2html +"th"
            elif i == 12:
                text2html = text2html +"th"
            elif i == 13:
                text2html = text2html +"th"
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