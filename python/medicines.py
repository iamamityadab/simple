#! C:/Users/HP/AppData/Local/Programs/Python/Python310/python
print("Content-Type:text/html")
print()
import cgi
form=cgi.FieldStorage()
print("sdfsdf")
t1=form.getvalue("t1")
t2=form.getvalue("t2")
t3=form.getvalue("t3")
t4=form.getvalue("t4")
t5=form.getvalue("t5")
t6=form.getvalue("t6")
import mysql.connector
try:
  if form.getvalue("b1")=="Save":
    con=mysql.connector.connect(user='root',password='',host='localhost', database='hospital')
    cur=con.cursor()
    cur.execute("insert into medicines values('"+t1+"','"+t2+"','"+t3+"','"+t4+"','"+t5+"','"+t6+"')")
    con.commit()
    print("<script>alert('Record Saved....')</script>")
    if form.getvalue("b1")=="Delete":
    con=mysql.connector.connect(user='root',password='',host='localhost', database='hospital')
    cur=con.cursor()
    cur.execute("delete from medicines where id='"+t1+"'")
    con.commit()
    print("<script>alert('Record Deleted....')</script>")
except Exception as e:
  print("<script>alert('Error...')</script>")
