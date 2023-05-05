#! C:\Python39\python.exe
print("Content-type:text/html\r\n\r\n")

import cgi,cgitb
cgitb.enable()

form= cgi.FieldStorage()

txtname=form.getvalue('name')
txtgender=form.getvalue('gender')
txtdob=form.getvalue('dob')
txtcourse=form.getvalue('course')
txtemail=form.getvalue('email')
txtphone=form.getvalue('phone')
txtqualification=form.getvalue('qualification')
txtaddress=form.getvalue('address')

print("<html>")
print("<head>")
print("<title>Form Data</title>")
print("</head>")
print("<body>")
print("<h3>Data Received:</h3>")
print("<p>Name: {}</p>".format(txtname))
print("<p>Gender: {}</p>".format(txtgender))
print("<p>DOB: {}</p>".format(txtdob))
print("<p>Course: {}</p>".format(txtcourse))
print("<p>Email: {}</p>".format(txtemail))
print("<p>Phone: {}</p>".format(txtphone))
print("<p>Qualification: {}</p>".format(txtqualification))
print("<p>Address: {}</p>".format(txtaddress))
print("</body>")
print("</html>")
