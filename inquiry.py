#! C:/Users/HP/AppData/Local/Programs/Python/Python310/python
print("Content-Type:text/html")
print()
import cgi
form=cgi.FieldStorage()
t1=form.getvalue("t1")
t2=form.getvalue("t2")
t3=form.getvalue("t3")
t4=form.getvalue("t4")
import mysql.connector
try:
  if form.getvalue("b1")=="Submit":
    con=mysql.connector.connect(user='root',password='',host='localhost', database='hospital')
    cur=con.cursor()
    cur.execute("insert into inquiry values('"+t1+"','"+t2+"','"+t3+"','"+t4+"')")
    con.commit()
    print("<script>alert('Record Saved....')</script>")
except Exception as e:
  print(e)
