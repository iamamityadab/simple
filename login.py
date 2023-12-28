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
    cur.execute("select * from login")
    r=cur.fetchall()
    f=0
    m=0
    for x in r:
      if(x[0]==t1 and x[1]==t2):
        if(x[2]>0):
          f=1
          break
        else:
          m=1
          break
    if(f==1):
        cur.execute("update login set counter=counter-1 where logid='"+t1+"'")
        conn.commit()
        print("<script>window.open('menu.html')</script>")
    elif(m==1):
        print("<script>alert('Please do Registration')</script>")
    elif(f==0):
        print("<script> alert(' Wrong Id or Password') </script>")
except Exception as e:
  print("<script>alert('Error...')</script>")

