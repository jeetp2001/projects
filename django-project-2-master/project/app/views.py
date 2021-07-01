from django.shortcuts import render,redirect     
from .models import User
import MySQLdb
from django.conf import settings
from django.contrib import messages

def index(request):
	return render(request,'login.html')

def display(request):
	contents = {'display':User.objects.all()}
	return render(request,'display.html',contents)

l=[]
def login(request):
    db = MySQLdb.connect(host = '0.0.0.0',user='root',password='G0d!sgreat',database='django')
    cur = db.cursor()
    q1 = 'select * from app_user'
    cur.execute(q1)
    email = request.GET['email']
    password = request.GET['password']
    data = cur.fetchall()
    for i in data:
       for j in i:
           if isinstance(j,str):
                if '.' in j:
                     l.append(j)
           if j == email:  
               if password in i: 
                   return redirect('/display')
               else:
                   messages.info(request,"Your password is incorrect, enter again")
                   return render(request,'login.html')
    if email not in l:
        messages.info(request,'This email is not yet registered.')
        return render(request,'error.html')

def register(request):
	return render(request,'register.html')

def edit(request,id):
	contents = {'edit':User.objects.get(pk=id)}
	return render(request,'edit.html',contents)

def delete(request,id):
	contents = User.objects.get(pk=id)
	contents.delete()
	return redirect('/display')


def edited(request):
	db = MySQLdb.connect(host = '0.0.0.0',user='root',password='G0d!sgreat',database='django')
	cur = db.cursor()
	name = request.GET['name']
	email = request.GET['email']
	password  = request.GET['password']
	cpassword = request.GET['cpassword']
	q2 = "select email from app_user where name=%s"
	t2 = (name,)
	cur.execute(q2,t2)
	data = cur.fetchall()
	q3 = "select email from app_user"
	cur.execute(q3)
	data2 = cur.fetchall()
	q4 = "select name from app_user"
	cur.execute(q4)
	data3 = cur.fetchall()
	if name in data3:
		email1=data[0][0]
	else:
		email1 = 'not accepted'	
	if email == email1:
		if password == cpassword:
			cur.execute("update app_user set email=%s,password=%s,cpassword=%s where name=%s",(email,password,cpassword,name))
			db.commit()
			messages.info(request,"Updated Successfully!")
			return redirect('/display')
			
	else:
		if email not in data2:
			if password == cpassword:
				cur.execute("update app_user set email=%s,password=%s,cpassword=%s where name=%s",(email,password,cpassword,name))	
				db.commit()			
				messages.info(request,"Updated Successfully!")
				return redirect('/display')	
			else:
				messages.info(request,"Your passwords didn't match, write again!")
				return render(request,'edit.html')		
		else:
			messages.info(request,"This email id is already registered, enter another email id")
			return render(request,'edit.html')
	

def registered(request):
	db = MySQLdb.connect(host = '0.0.0.0',user='root',password='G0d!sgreat',database='django')
	cur = db.cursor()
	name = request.GET['name']
	email = request.GET['email']
	q2 = "select email from app_user"
	cur.execute(q2)
	data = cur.fetchall()
	if email not in data:
	
		password  = request.GET['password']
		cpassword = request.GET['cpassword']
		if password == cpassword:
			q1 = 'insert into app_user (name,email,password,cpassword) values (%s,%s,%s,%s)'
			t1 = (name,email,password,cpassword)
			cur.execute(q1,t1)
			db.commit()
			return render(request,'login.html')
		else:
			messages.info(request,"Your passwords didn't match, write again!")	
			return render(request,'register.html')
	else:
		messages.info(request,"This email id is already registered, enter another email id")
		return render(request,'register.html')
