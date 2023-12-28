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
  if form.getvalue("b1")=="Save":
    con=mysql.connector.connect(user='root',password='',host='localhost', database='hospital')
    cur=con.cursor()
    cur.execute("select * from roll")
    r=cur.fetchall()
    f=0
    for x in r:
      if(x[0]==int(t1)):
        f=1
        break
    if(f==1):
      print("<script>alert('ID is already registered')</script>")
    else:
      cur.execute("insert into roll values('"+t1+"','"+t2+"','"+t3+"')")
      con.commit()
      print("<script>alert('Record Saved....')</script>")
  if form.getvalue("b1")=="Delete":
    con=mysql.connector.connect(user='root',password='',host='localhost', database='hospital')
    cur=con.cursor()
    cur.execute("delete from roll where id='"+t1+"'")
    con.commit()
    print("<script>alert('Record Deleted....')</script>")
  if form.getvalue("b1")=="Update":
    con=mysql.connector.connect(user='root',password='',host='localhost', database='hospital')
    cur=con.cursor()
    cur.execute("update roll set roll_title='"+t2+"',roll_descr='"+t3+"' where id='"+t1+"'")
    con.commit()
    print("<script>alert('Record Updated....')</script>")
  if form.getvalue("b1")=="Particular Search":
    con=mysql.connector.connect(user='root',password='',host='localhost', database='hospital')
    print("<table border=1><tr><th>ID</th><th>Roll Title</th><th>Roll Description</th></tr>")
    cur=con.cursor()
    cur.execute("select * from roll where id='"+t1+"'")
    r=cur.fetchall()
    for x in r:
      print("<form name='f' method='post' action='rollUpdate.py'>")
      print("<tr>")
      print("<th><input type=text readonly name=t1 value=",x[0],"</th>")
      print("<th><input type=text name=t2 value=",x[1],"</th>")
      print("<th><input type=text name=t3 value=",x[2],"</th>")
      print("<input type=submit value='Update' name=b2>")
      print("</form>")
    print("</table>")
  if form.getvalue("b1")=="All Search":
    con=mysql.connector.connect(user='root',password='',host='localhost', database='hospital')
    print("<table border=1><tr><th>ID</th><th>Roll Title</th><th>Roll Description</th></tr>")
    cur=con.cursor()
    cur.execute("select * from roll")
    r=cur.fetchall()
    for x in r:
      print("<form name='f' method='post' action='rollUpdate.py'>")
      print("<tr>")
      print("<th><input type=text readonly name=t1 value=",x[0],"</th>")
      print("<th><input type=text name=t2 value=",x[1],"</th>")
      print("<th><input type=text name=t3 value=",x[2],"</th>")
      print("<input type=submit value='Update' name=b2>")
      print("</form>")
    print("</table>")
except Exception as e:
  print("<script>alert('Error...')</script>")
