#! C:/Users/HP/AppData/Local/Programs/Python/Python310/python
print("Content-Type:text/html")
print()
import cgi
form=cgi.FieldStorage()
import mysql.connector
t1=form.getvalue("t1")
t2=form.getvalue("t2")
t3=form.getvalue("t3")
t4=form.getvalue("t4")
t5=form.getvalue("t5")
t6=form.getvalue("t6")
button = form.getvalue("b1")

try:
  if button == "Save":
    conn = mysql.connector.connect(user='root',password='',host='localhost',database='hospital')
    cur = conn.cursor()
    cur.execute("select * from appointments")
    r=cur.fetchall()
    f=0
    for x in r:
      if(x[0]==int(t1)):
        f=1
        break

    #Match Doctor id
    cur.execute("select id from doctor")
    s=cur.fetchall()
    d=0
    for x in s:
      if(x[0]==int(t6)):
        d=1
        break

    if(f==1):
      print("<script>alert('ID is already registered')</script>")
    elif(d==0):
      print("<script>alert('Doctor is not registered')</script>")
    else:
      cur.execute("insert into appointments values ('"+t1+"','"+t2+"','"+t3+"','"+t4+"','"+t5+"','"+t6+"')")
      conn.commit()
      print("<script>alert('Record saved....')</script>")
      

  if button == "Delete":
    conn = mysql.connector.connect(user='root',password='',host='localhost',database='hospital')
    cur = conn.cursor()
    cur.execute("delete from appointments where id='"+t1+"'")
    conn.commit()
    print("<script>alert('Record Deleted....')</script>")
  if button == "Update":
    conn = mysql.connector.connect(user='root',password='',host='localhost',database='hospital')
    cur = conn.cursor()
    cur.execute("update appointments set appnum='"+t2+"',type='"+t3+"',date1='"+t4+"',descr='"+t5+"',doctor_id='"+t6+"' where id='"+t1+"'")
    conn.commit()
    print("<script>alert('Record Updated....')</script>")
  if form.getvalue("b1")=="Particular Search":
    con=mysql.connector.connect(user='root',password='',host='localhost', database='hospital')
    print("<table border=1><tr><th>ID</th><th>Application Number</th><th>Type</th><th>Date</th><th>Description</th><th>Doctor ID</th></tr>")
    cur=con.cursor()
    cur.execute("select * from appointments where id='"+t1+"'")
    r=cur.fetchall()
    for x in r:
      print("<form name='f' method='post' action='appointmentsUpdate.py'>")
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
    print("<table border=1><tr><th>ID</th><th>Application Number</th><th>Type</th><th>Date</th><th>Description</th><th>Doctor ID</th></tr>")
    cur=con.cursor()
    cur.execute("select * from appointments")
    r=cur.fetchall()
    for x in r:
      print("<form name='f' method='post' action='appointmentsUpdate.py'>")
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
  if form.getvalue("b1")=="Search Doctor ID":
    con=mysql.connector.connect(user='root',password='',host='localhost', database='hospital')
    print("<table border=1><tr><th>Doctor ID</th><th>Doctor Name</th></tr>")
    cur=con.cursor()
    cur.execute("select id,name from doctor")
    r=cur.fetchall()
    for x in r:
      print("<form name='f'>")
      print("<tr>")
      print("<th><input type=text readonly name=t1 value=",x[0],"</th>")
      print("<th><input type=text readonly name=t2 value=",x[1],"</th>")
      print("</form>")
    print("</table>")
except Exception as e:
  print(e)

