from tkinter import *
from tkinter import messagebox
import mysql.connector

db=mysql.connector.connect(host="localhost",user="root",database="python",password="-")
cur=db.cursor()

window1=Tk()

l=Label(window1,text="Welcome to Admin page").grid(row=2,column=6)
l1=Label(window1,text="New User!").grid(row=4,column=2)
count=0
def signup(): 
    global count
    window=Tk()
    count=count+1
    l1=Label(window,text="Enter name")
    l1.grid(row=2,column=5)
    l2=Label(window,text="Enter role")
    l2.grid(row=3,column=5)
    l3=Label(window,text="Enter password")
    l3.grid(row=4,column=5)
    e1=Entry(window)
    e2=Entry(window)
    e3=Entry(window)
    e1.grid(row=2,column=9)
    e2.grid(row=3,column=9)
    e3.grid(row=4,column=9)   
    def submit():
        q1="insert ignore into login values (%s,%s,MD5(%s))"
        t1=tuple([e1.get(),e2.get(),e3.get()])
        cur.execute(q1,t1)
        l=Label(window1,text="Registered Successfully")
        l.grid(row=count+6,column=2)
        db.commit()
    def done():
        window.destroy()            
        
    b1=Button(window,text="Done",command=done)
    b1.grid(row=6,column=5)
    b2=Button(window,text="submit",command=submit)
    b2.grid(row=6,column=9)
    window.mainloop()
    
def login():
    window=Tk()
    
    def student():
        window1=Tk()
        l1=Label(window1,text="enter name of student")
        l1.grid(row=3,column=3)
        l2=Label(window1,text="enter password")
        l2.grid(row=6,column=3)
        e11=Entry(window1)
        e2=Entry(window1)
        e11.grid(row=3,column=6)
        e2.grid(row=6,column=6)
        q="select name,password from login where role='student'"
        cur.execute(q)
        data=cur.fetchall()
        def slogin():
            s=''
            s1=''
            s=s+e11.get()
            s1=s1+e2.get()
            l=[]
            l1=[]
            for i in data:
                l.append(i[0])
            for i in data:
                l1.append(i[1])
            for i,j in zip(l,l1):
                if i==s and j==s1:
                    window=Tk()
                    l=Label(window,text="Displaying Marks").grid(row=5,column=5)
                    l1=Label(window,text="Enter Student's id").grid(row=7,column=3)
                    e1=Entry(window)
                    e1.grid(row=7,column=6)
                    def show():
                    
                        window=Tk()
                        
                        q1="select name,id,class from marks where id = %s"
                        t1=tuple([int(e1.get())])
                        cur.execute(q1,t1)
                        data1=cur.fetchall()
                        db.commit()
                        q2="select phy,che,mat,eng,comp from marks where id = %s"
                        t2=tuple([int(e1.get())])
                        cur.execute(q2,t2)
                        data2=cur.fetchall()
                        db.commit()
                        q3="select percentage from marks where id = %s"
                        t3=tuple([int(e1.get())])
                        cur.execute(q3,t3)
                        data3=cur.fetchall()
                        db.commit()
                        q4="select max,min from marks where id = %s"
                        t4=tuple([int(e1.get())])
                        cur.execute(q4,t4)
                        data4=cur.fetchall()
                        db.commit()
                                                
                        l1=Label(window,text="Name of student : "+str(data1[0][0])+"\nId of student : "+str(data1[0][1])+"\nClass of student : "+str(data1[0][2]))
                        l1.grid(row=5,column=5)
                        l2=Label(window,text="Marks of Student : \nPhysics : "+str(data2[0][0])+"\nChemistry : "+str(data2[0][1])+"\nMaths : "+str(data2[0][2])+"\nEnglish : "+str(data2[0][3])+"\nComputer : "+str(data2[0][4]))
                        l2.grid(row=10,column=5)
                        l3=Label(window,text="Maximum marks : "+str(data4[0][0])+"\nMinimum marks : "+str(data4[0][1])+"\nPercentage of student : "+str(data3[0][0]))
                        l3.grid(row=15,column=5)
                        
                        window.mainloop()
                    b1=Button(window,text="show",command=show)
                    b1.grid(row=10,column=3)
                        
                    window.mainloop()
                else:
                    messagebox.showerror("Error", "Name or Password is wrong!")
                
                
        b=Button(window1,text="login",command=slogin)
        b.grid(row=8,column=3)
        window1.mainloop()
        
        
    def teacher():
        window=Tk()
        l1=Label(window,text="enter name of teacher")
        l1.grid(row=3,column=3)
        l2=Label(window,text="enter password")
        l2.grid(row=6,column=3)
        e111=Entry(window)
        e22=Entry(window)
        e111.grid(row=3,column=6)
        e22.grid(row=6,column=6)
        q="select name,password from login where role='teacher'"
        cur.execute(q)
        data=cur.fetchall()
        def tlogin():
            s1=''
            s2=''
            s1=s1+e111.get()
            s2=s2+e22.get()
            l=[]
            l1=[]
            for i in data:
                l.append(i[0])
            for i in data:
                l1.append(i[1])
            for i,j in zip(l,l1):
                if i==s1 and j==s2:  
                    window=Tk()
                    l11=Label(window,text="Fill the marks of student")
                    l11.grid(row=1,column=5)
                    l1=Label(window,text="Physics")
                    l1.grid(row=10,column=2)
                    l2=Label(window,text="Chemistry")
                    l2.grid(row=12,column=2)
                    l3=Label(window,text="Mathematics")
                    l3.grid(row=14,column=2)
                    l4=Label(window,text="English")
                    l4.grid(row=16,column=2)
                    l5=Label(window,text="Computer")
                    l5.grid(row=18,column=2)
                    l6=Label(window,text="Student's name")
                    l6.grid(row=4,column=2)
                    l7=Label(window,text="Student's id")
                    l7.grid(row=6,column=2)
                    l8=Label(window,text="Student's class")
                    l8.grid(row=8,column=2)
                    
                    e1=Entry(window)
                    e2=Entry(window)
                    e3=Entry(window)
                    e4=Entry(window)
                    e5=Entry(window)
                    e6=Entry(window)
                    e7=Entry(window)
                    e8=Entry(window)
            
                    e1.grid(row=10,column=4)
                    e2.grid(row=12,column=4)
                    e3.grid(row=14,column=4)
                    e4.grid(row=16,column=4)
                    e5.grid(row=18,column=4)
                    e6.grid(row=4,column=4)
                    e7.grid(row=6,column=4)
                    e8.grid(row=8,column=4)
                    def average():
                        s1=int(e1.get())
                        s2=int(e2.get())
                        s3=int(e3.get())
                        s4=int(e4.get())
                        s5=int(e5.get())
                        avg=(s1+s2+s3+s4+s5)/5
                        avg=str(avg)
                        l=Label(window,text="your average marks is "+avg).grid(row=24,column=2)
                    global max,min 
                    
                    def submit():
                        name=e6.get()
                        id1=int(e7.get())
                        c=int(e8.get())
                        s1=int(e1.get())
                        s2=int(e2.get())
                        s3=int(e3.get())
                        s4=int(e4.get())
                        s5=int(e5.get())
                        avg=(s1+s2+s3+s4+s5)/5
                        avg=str(avg)
                        marks=[int(e1.get()),int(e2.get()),int(e3.get()),int(e4.get()),int(e5.get())]
                        max=0
                        for i in marks:
                            if max<i:
                                max=i
                        min=marks[0]
                        for i in marks:
                            if i<min:
                                min=i 
                    
                        q1="insert into marks values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                        t1=tuple([name,id1,c,s1,s2,s3,s4,s5,avg,max,min])
                        cur.execute(q1,t1)
                        db.commit()    
                        l=Label(window,text="Submitted successfully")
                        l.grid(row=26,column=2)
                    
                    def clear():
                        e1.delete(0,END)
                        e2.delete(0,END)
                        e3.delete(0,END)
                        e4.delete(0,END)
                        e5.delete(0,END)
                        e6.delete(0,END)
                        e7.delete(0,END)
                        e8.delete(0,END)
                    b1=Button(window,text="Calculate Average",command=average)
                    b1.grid(row=20,column=2)
                    b2=Button(window,text="Submit to database",command=submit)
                    b2.grid(row=20,column=6)
                    b3=Button(window,text="clear data",command=clear)
                    b3.grid(row=20,column=10)
                        
                    window.mainloop()
                else:
                    messagebox.showerror("Error", "Name or Password is wrong!")
                    
        b=Button(window,text="login",command=tlogin)
        b.grid(row=8,column=3)
        window.mainloop()
        
    b1=Button(window,text="student",command=student)
    b1.grid(row=3,column=3)
    b2=Button(window,text="teacher",command=teacher)
    b2.grid(row=5,column=3)  
        
    window.mainloop()
   
b1=Button(window1,text="sign up",command=signup)
b1.grid(row=5,column=2)
l2=Label(window1,text="OR")
l2.grid(row=4,column=6)
b2=Button(window1,text="login",command=login)
b2.grid(row=5,column=6)

window1.mainloop()
