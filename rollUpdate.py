#! C:/Users/HP/AppData/Local/Programs/Python/Python310/python
print("Content-Type:text/html")
print()
import cgi
form=cgi.FieldStorage()
t1=form.getvalue("t1")
t2=form.getvalue("t2")
t3=form.getvalue("t3")
import mysql.connector
try:
    if form.getvalue("b2")=="Update":
        con=mysql.connector.connect(user='root',password='',host='localhost', database='hospital')
        cur=con.cursor()
        cur.execute("update roll set roll_title='"+t2+"',roll_descr='"+t3+"' where id='"+t1+"'")
        con.commit()
        print("<script>alert('Record Updated....')</script>")
except Exception as e:
  print("<script>alert('Error...')</script>")
