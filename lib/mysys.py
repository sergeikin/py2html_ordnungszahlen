import sys,os

def create_file(text, filename):
    if os.path.exists(filename):
        os.remove(filename)
    f = open(filename, "w+")
    f.write(text)
    f.close
