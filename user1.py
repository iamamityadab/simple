#! C:/Users/HP/AppData/Local/Programs/Python/Python310/python
print("Content-Type:text/html")
print()
import cgi
form=cgi.FieldStorage()
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
    cur.execute("select * from user1")
    r=cur.fetchall()
    f=0
    for x in r:
      if(x[0]==int(t1)):
        f=1
        break
       #Match Roll id
    cur.execute("select id from roll")
    r=cur.fetchall()
    d=0
    for x in r:
      if(x[0]==int(t2)):
        d=1
        break
    if(f==1):
      print("<script>alert('ID is already registered')</script>")
    elif(d==0):
      print("<script>alert('Roll ID is not registered')</script>")
    else:
      cur.execute("insert into user1 values('"+t1+"','"+t2+"','"+t3+"','"+t4+"','"+t5+"','"+t6+"')")
      con.commit()
      print("<script>alert('Record Saved....')</script>")
  if form.getvalue("b1")=="Delete":
    con=mysql.connector.connect(user='root',password='',host='localhost', database='hospital')
    cur=con.cursor()
    cur.execute("delete from user1 where id='"+t1+"'")
    con.commit()
    print("<script>alert('Record Deleted....')</script>")
  if form.getvalue("b1")=="Update":
    con=mysql.connector.connect(user='root',password='',host='localhost', database='hospital')
    cur=con.cursor()
    cur.execute("update user1 set roll_id='"+t2+"',name='"+t3+"',email='"+t4+"',dob='"+t5+"',address='"+t6+"' where id='"+t1+"'")
    con.commit()
    print("<script>alert('Record Updated....')</script>")
  if form.getvalue("b1")=="Particular Search":
    con=mysql.connector.connect(user='root',password='',host='localhost', database='hospital')
    print("<table border=1><tr><th>ID</th><th>Roll ID</th><th>Name</th><th>Email</th><th>DOB</th><th>Address</th></tr>")
    cur=con.cursor()
    cur.execute("select * from user1 where id='"+t1+"'")
    r=cur.fetchall()
    for x in r:
      print("<form name='f' method='post' action='userUpdate.py'>")
      print("<tr>")
      print("<th><input type=text readonly name=t1 value=",x[0],"</th>")
      print("<th><input type=text name=t2 value=",x[1],"</th>")
      print("<th><input type=text name=t3 value=",x[2],"</th>")
      print("<th><input type=text name=t4 value=",x[3],"</th>")
      print("<th><input type=text name=t5 value=",x[4],"</th>")
      print("<th><input type=text name=t6 value=",x[5],"</th>")
      print("<input type=submit value='Update' name=b2>")
      print("</form>")
    print("</table>")
  if form.getvalue("b1")=="All Search":
    con=mysql.connector.connect(user='root',password='',host='localhost', database='hospital')
    print("<table border=1><tr><th>ID</th><th>Roll ID</th><th>Name</th><th>Email</th><th>DOB</th><th>Address</th></tr>")
    cur=con.cursor()
    cur.execute("select * from user1")
    r=cur.fetchall()
    for x in r:
      print("<form name='f' method='post' action='userUpdate.py'>")
      print("<tr>")
      print("<th><input type=text readonly name=t1 value=",x[0],"</th>")
      print("<th><input type=text name=t2 value=",x[1],"</th>")
      print("<th><input type=text name=t3 value=",x[2],"</th>")
      print("<th><input type=text name=t4 value=",x[3],"</th>")
      print("<th><input type=text name=t5 value=",x[4],"</th>")
      print("<th><input type=text name=t6 value=",x[5],"</th>")
      print("<input type=submit value='Update' name=b2>")
      print("</form>")
    print("</table>")
  if form.getvalue("b1")=="Search Roll ID":
    con=mysql.connector.connect(user='root',password='',host='localhost', database='hospital')
    print("<table border=1><tr><th>Roll ID</th><th>Roll Title</th></tr>")
    cur=con.cursor()
    cur.execute("select id,roll_title from roll")
    r=cur.fetchall()
    for x in r:
      print("<form name='f'>")
      print("<tr>")
      print("<th><input type=text readonly name=t1 value=",x[0],"</th>")
      print("<th><input type=text readonly name=t2 value=",x[1],"</th>")
      print("</form>")
    print("</table>")
except Exception as e:
  print("<script>alert('Error...')</script>")
