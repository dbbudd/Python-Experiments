#!/usr/bin/python

def my_header():
    print("<!doctype html><html><head>")
    print("<title>PokeCGI</title>")
    #STYLESHEET BELOW
    print("""
          <style>
          body{background:#060;}
          #wrapper{display:block; width:1024px; height:100% float:left; margin:0 auto;}
          #header{display:block; float:left; width:1024px; height:150px; background:#000 url(img/banner.png) no-repeat;}
          #column{float:left; display:inline; width:200px; height:100%; margin-right:50px;}
          #searchbox{display:block; float:right; width:200px; height:110px; text-align:center;}
          #bodycopy{float:left; display:inline; width:700px; height:100%;}
          #menu{float:left; display:block; background:green; width:200px; height:400px; text-align:center;}
          #menu li{float:left; display:block; width:200px; padding:20px; list-style:none; text-align:left;}
          #menu a{color:#FFF; text-decoration:none; }
          #menu a:hover{color:#000; text-decoration:none;}
          #content{display:block; float:left; width:1024px; min-height:300px; background:#ffffff;}
          a{color:#fff; display:block; width:150px; height:25px;}
          a:hover{color:#fff; display:block; width:150px; height:25px;}
          #footer{display:block; float:left; width:1024px; height:80px;}
          </style>
          """)
    
    print("""
          </head>
          <body>
          <div id='wrapper'>
          <div id='header'>
          <div id='searchbox'>
          <form id='search_database' action='search_new_query.py' method='GET'>
          <p><label>search the database:</label><br/>
          <input type='text' name='Search_Query'><br/>
          <label>select:</label>
          <select name='Choose_Table'>
          <option>Locations</option>
          <option>Pokedex</option>
          <option>Trainers</option>
          </select><br/>
          <input type='submit' value='Search' /></p>
          </form>
          </div>
          </div>
          <div id='content'>
          <div id='column'>
          <ul id='menu'>
          <li><a href='index.py' target='_self'>Home</a></li>
          <li><a href='#' target='_self'>Create Database</a></li>
          <li><a href='#' target='_self'>Populate Database</a></li>
          <li><a href='insert_location_form.py' target='_self'>Add Record</a></li>
          <li><a href='#' target='_self'>Query DB</a></li>
          <li><a href='#' target='_self'>View Report</a></li>
          </ul>
          </div>
          <div id='bodycopy'>
          """)

def my_footer():
    print("""
          </div>
          <div id='footer'>
          <!--this is my footer content-->
          </div>
          </div>
          </body>
          </html>
          """)