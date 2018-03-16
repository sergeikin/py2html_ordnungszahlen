# -*- coding: utf-8 -*-
import sys, os, glob


Altf4 = ""
Altf4 = Altf4 + """<h3>""" + " Ü" + """bersicht der Ordnungszahlen von 1 bis 1.000.000</h3>"""
for i in range(10):
    #Altf4 = Altf4 +"""<b>"""+ str(i) + """st</b><br>"""
    Altf4 = Altf4 + """<html>
    <head>
    <title>seite</title>
    </head>
    <body>
    <table border="1" width="1000">
    <tbody>
    <tr>
      <td><b>1st</b> <font color="#6495ed">first</font></td>
      <td><b>11th</b> <font color="#6495ed">eleventh</font></td>
      <td><b>21st</b> <font color="#6495ed">twenty-first</font></td>
      <td><b>31st</b> <font color="#6495ed">thirty-first</font></td>
    </tr>
    <tr>
      <td><b>2nd</b> <font color="#6495ed">second</font></td>
      <td><b>12th</b> <font color="#6495ed">twelfth</font></td>
      <td><b>22st</b> <font color="#6495ed">twenty-second</font></td>
      <td><b>40th</b> <font color="#6495ed">fortieth</font></td>
    </tr>
    <tr>
      <td><b>3rd</b> <font color="#6495ed">third</font></td>
      <td><b>13th</b> <font color="#6495ed">thirtieenth</font></td>
      <td><b>23rd</b> <font color="#6495ed">twenty-third</font></td>
      <td><b>50th</b> <font color="#6495ed">fiftieth</font></td>
    </tr>
    <tr>
      <td><b>4th</b> <font color="#6495ed">fourth</font></td>
      <td><b>14th</b> <font color="#6495ed">fourteenth</font></td>
      <td><b>24th</b> <font color="#6495ed">twenty-fourth</font></td>
      <td><b>60th</b> <font color="#6495ed">sixtieth</font></td>
    </tr>
    <tr>
      <td><b>5th</b> <font color="#6495ed">fifth</font></td>
      <td><b>15th</b> <font color="#6495ed">fifteenth</font></td>
      <td><b>25th</b> <font color="#6495ed">twenty-fifth</font></td>
      <td><b>70th</b> <font color="#6495ed">seventieth</font></td>
    </tr>
    <tr>
      <td><b>6th</b> <font color="#6495ed">sixth</font></td>
      <td><b>16th</b> <font color="#6495ed">sixteenth</font></td>
      <td><b>26th</b> <font color="#6495ed">twenty-sixth</font></td>
      <td><b>80th</b> <font color="#6495ed">eightieth</font></td>
    </tr>
    <tr>
      <td><b>7th</b> <font color="#6495ed">seventh</font></td>
      <td><b>17th</b> <font color="#6495ed">seventeenth</font></td>
      <td><b>27th</b> <font color="#6495ed">twenty-seventh</font></td>
      <td><b>90th</b> <font color="#6495ed">ninetieth</font></td>
    </tr>
    <tr>
      <td><b>8th</b> <font color="#6495ed">eighth</font></td>
      <td><b>18th</b> <font color="#6495ed">eighteenth</font></td>
      <td><b>28th</b> <font color="#6495ed">twenty-eighth</font></td>
      <td><b>100th</b> <font color="#6495ed">one
    hundredth</font></td>
    </tr>
    <tr>
      <td><b>9th</b> <font color="#6495ed">ninth</font></td>
      <td><b>19th</b> <font color="#6495ed">nineteenth</font></td>
      <td><b>29th</b> <font color="#6495ed">twenty-ninth</font></td>
      <td><b>1,000th</b> <font color="#6495ed">one
    thousandth</font></td>
    </tr>
    <tr>
      <td><b>10th</b> <font color="#6495ed">tenth</font></td>
      <td><b>20th</b> <font color="#6495ed">twentieth</font></td>
      <td><b>30th</b> <font color="#6495ed">thirtieth</font></td>
      <td><b>1,000,000th</b> <font color="#6495ed">one
    millionth</font></td>
    </tr>
    </tbody>
    </table>
    </body>
    </html>
    """

f = open("test_py.html", "w")
f.write(Altf4)
f.close