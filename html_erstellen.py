# -*- coding: utf-8 -*-
import sys,os,glob

text = ""
text = text + """
<html>
<head>
<title>Uebersicht der Ordnungszahlen von 1 bis 1.000.000</title>
</head>
<body>
<b>Uebersicht der Ordnungszahlen von 1 bis 1.000.000</b>
<table border=1>

<tr>
<td>1st first</td>
<td>11th eleventh</td>
<td>21st twenty-first</td>
<td>31st thirty-first</td>
</tr>

<tr>
<td>2nd second</td>
<td>12th twelfth</td>
<td>22nd twenty-second</td>
<td>40th fouteenth</td>
</tr>



<tr>
<td>3th thirteenth</td>
<td>13th thirteenth</td>
<td>23th twenty-third</td>
<td>50th fiftieth</td>
</tr>

<tr>
<td>4th fourth</td>
<td>14th fourteenth</td>
<td>24th twenty-fourth</td>
<td>60th sixtieth</td>
</tr>


<tr>
<td>5th fifth</td>
<td>15th fifteenth</td>
<td>25th twenty fifth</td>
<td>70th seventieth</td>
</tr>


<tr>
<td>6th sixth</td>
<td>16th sixteenth</td>
<td>26th twenty-sixth</td>
<td>80th eightieeth</td>
</tr>


<tr>
<td>7th seventh</td>
<td>17th seventeenth</td>
<td>27th twenty-seventh</td>
<td>90th ninetieth</td>
</tr>


<tr>
<td>8th eighth</td>
<td>18th eighteenth</td>
<td>28th twentie-eighth</td>
<td>100th onehundreth</td>
</tr>


<tr>
<td>9 nineth</td>
<td>19 nineteenth</td>
<td>29 twentie-nineth</td>
<td>1.000th thousanth</td>
</tr>


<tr>
<td>10th tenth</td>
<td>20th twentieth</td>
<td>30th thirtieth</td>
<td>1.000.000th onemillionth</td>
</tr>

</table>
</body>
</html>
"""

for i in range (31):




f = open ("test_py.html","w")
f.write(text)
f.close