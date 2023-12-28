#! C:/Users/HP/AppData/Local/Programs/Python/Python310/python
print("Content-Type:text/html")
print()
import cgi

from mysqlx import Result
form=cgi.FieldStorage()
import mysql.connector
t1=form.getvalue("t1")
t2=form.getvalue("t2")
button = form.getvalue("b1")
try:
  if button == "Login":
    conn = mysql.connector.connect(user='root',password='',host='localhost',database='hospital')
    cur = conn.cursor()
    cur.execute("select * from admin")
    r=cur.fetchall()
    f=0
    for x in r:
        if(x[0]==t1 and x[1]==t2):
            f=1
            break

    if(f==1):
        print("<script>window.open('register.html')</script>")
    else:
        print("<script> alert('Wrong Id or Password') </script>")   
except Exception as e:
  print("<script>alert('Error...')</script>")
