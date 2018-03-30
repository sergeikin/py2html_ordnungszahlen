# -*- coding: utf-8 -*-
import sys, os, glob
import lib.html_module as html

def create_file(head, body, foot):
    f = open("Table_of_enumerations.html", "w")
    f.write(head+body+foot)
    f.close

if __name__=="__main__":
    head = html.head()
    body = html.body()
    foot = html.foot()
    create_file(head,body,foot)
