
if __name__=='__main__':
    print(globals())
    be_imported =  __import__("be_imported")
    print(globals())
    y1 = be_imported.Y1()
    print(y1)
