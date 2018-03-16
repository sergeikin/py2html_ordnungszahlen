# -*- coding: utf-8 -*-
import sys, os, glob

def html_head():
    text2html = """<html>
<head>
<title>Table of enumerations</title>
</head>
<body>
<h3>The table of enumerations from 1th to 1,000th</h3>
<table border="5" bgcolor="#070707" width="750">
<tbody>"""
    return text2html

def html_body():
    text2html = """ """
    for x in range(100):
        text2html = text2html + """<tr>"""
        for y in range(1, 11):
            zahlenvergleich = x*10+y
            text2html = text2html + """<td align="center"><font color="#00FF00"> """
            text2html = text2html + str(zahlenvergleich) #Zahl wird hinzugefügt
            if (x == 1) and (y == 1):
                text2html = text2html +"""</font>"""+"""<font color="#FF0000">"""+"th"+"""</font>"""
            elif (x == 1) and (y == 2):
                text2html = text2html +"""</font>"""+"""<font color="#FF0000">"""+"th"+"""</font>"""
            elif (x == 1) and (y == 3):
                text2html = text2html +"""</font>"""+"""<font color="#FF0000">"""+"th"+"""</font>"""
            elif y == 1:
                text2html = text2html +"st"
            elif y == 2:
                text2html = text2html +"nd"
            elif y == 3:
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