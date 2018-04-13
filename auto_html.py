# -*- coding: utf-8 -*-
import sys, os, glob
import lib.html_module as html
import lib.mysys as msys

def main():
    text = html.head() + html.body() + html.foot()
    filename = "C:/Users/Daniel/Git/py2html_ordnungszahlen/Table_of_enumerations.html"
    msys.create_file(text, filename)


if __name__=="__main__":
    main()