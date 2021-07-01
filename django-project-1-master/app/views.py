from django.shortcuts import render
from .models import User
import MySQLdb
from django.conf import settings
from django.core.mail import EmailMessage

# Create your views here.
def user(request):
    return render(request,'form.html')

def display(request):
    db = MySQLdb.connect(host='jeet2908.mysql.pythonanywhere-services.com',user='jeet2908',password='G0d!sgreat',database='jeet2908$user')
    cur = db.cursor()
    name = request.GET['name']
    email = request.GET['email']
    dob = request.GET['dob']
    phone = request.GET['phone']
    q1 = "insert into app_user (name,email,dob,phone) values (%s,%s,%s,%s)"
    t1 = (name,email,dob,phone,)
    cur.execute(q1,t1)
    db.commit()
    db.close()
    obj = User.objects.all()
    context = {"object" : obj}
    subject = 'Form filled and submitted successfully!'
    from_email = settings.EMAIL_HOST_USER
    to_email = [from_email , email]
    body = {'Name':name,'Email-id':email,'Date_of_Birth':dob,'Phone_no.':phone}
    content = {"%s: %s" % (key, value) for (key, value) in body.items()}
    content = "\n".join(content)
    mail=EmailMessage(subject,content,from_email,to_email)
    mail.send()
    return render(request,'display.html',context)