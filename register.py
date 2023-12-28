#! C:/Users/HP/AppData/Local/Programs/Python/Python310/python
print("Content-Type:text/html")
print()
import cgi
from typing import Counter

from mysqlx import Result
form=cgi.FieldStorage()
import mysql.connector
t1=form.getvalue("t1")
t2=form.getvalue("t2")
t3=form.getvalue("t3")
button = form.getvalue("b1")
try:
  if button == "Set":
    conn = mysql.connector.connect(user='root',password='',host='localhost',database='hospital')
    cur = conn.cursor()
    cur.execute("select * from login")
    r=cur.fetchall()
    f=0
    for x in r:
        if(x[0]==t1 and x[1]==t2):
          if(x[2]==0):
            f=1
            break
          else:
            print("<script>alert('You Have Some Counter')")
    if(f==1):
        cur.execute("update login set logpwd='"+t2+"',counter='"+t3+"' where logid='"+t1+"'")
        conn.commit()
        print("<script> alert('Registration Updated') </script>")
    else:
        cur.execute("insert into login values ('"+t1+"','"+t2+"','"+t3+"')")
        conn.commit()
        print("<script> alert('Registration complete') </script>")   
except Exception as e:
  print("<script>alert('Error...')</script>")
