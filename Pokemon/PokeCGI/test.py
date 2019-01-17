
    #!/usr/bin/python
    print "Content-type: text/html"
    print
    
    #import the libraries
    import cgi
    import cgitb; cgitb.enable()
    import sqlite3
    import sys
    
    print("<html>")
    print("<head>")
    print("<title>")
    print(filename)
    print("</title>")
    print("<meta http-equiv='Content-Type' content='text/html;charset=utf-8'>")
    print("</head>")
    print("<body>")
    
    print("<!--put your python code here-->")
    
    print("</body>")
    print("</html>")
    