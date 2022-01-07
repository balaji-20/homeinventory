from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import *
import PIL
from PIL import ImageTk,Image
from functools import partial
import mysql.connector
#create table his(item varchar(70) primary key,location varchar(100),mark integer(1),serialno varchar(30),price varchar(10),dat varchar(9),place varchar(70), note varchar(300),photoloc varchar(200) );
mydb=mysql.connector.connect(host="localhost",user="****",password="****",database="php")
cur=mydb.cursor()
x=[]
ran=0
def new():
    r1.delete(0,END)
    r2.delete(0,END)
    mark.set(0)
    r4.delete(0,END)
    r5.delete(0,END)
    r6.delete(0,END)
    r7.delete(0,END)
    r8.delete(0,END)
    r9.delete(0,END)

def delete():
    it=item.get()
    sql="delete from his where item ='"+it+"'"
    cur.execute(sql)
    mydb.commit()
    r1.delete(0,END)
    r2.delete(0,END)
    mark.set(0)
    r4.delete(0,END)
    r5.delete(0,END)
    r6.delete(0,END)
    r7.delete(0,END)
    r8.delete(0,END)
    r9.delete(0,END)
    
def save():
    it=item.get()
    lc=loc.get()
    mk=mark.get() 
    sn=sno.get()
    pr=price.get()
    dte=dt.get()
    wh=where.get()
    nt=note.get()
    phl=photo.get()
    if(it==""):
        messagebox.showerror("Error", "Item name not given")
    else:
        try:
            values=(it,lc,mk,sn,pr,dte,wh,nt,phl)
            cur.execute("insert into his values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",values)
            mydb.commit()
        except:
            messagebox.showerror("Error", "Item already exists")

    
def previous():
    global ran
    ran=ran-1
    do()

def nexto():
    global ran
    ran=ran+1
    do()
    
def photoo():
    try:
        l=photo.get()
        if l=="":
            messagebox.showerror("Error", "Path Not Entered")
        else:
            r = Toplevel()
            r.title("image")
            img = ImageTk.PhotoImage(Image.open(l),height=500,width=500)
            panel = Label(r, image = img)
            panel.pack(side = "bottom", fill = "both", expand = "yes")
            #Button(r,text="Close",command=lambda:r.destroy()).pack()
            r.mainloop()
    except:
        r.destroy()
        messagebox.showerror("Error", "Invalid Path")
    

def bo(s):
    global x
    global ran
    st=alpha[s]
    sql="select * from his where item like '"+st+"%'"
    cur.execute(sql)
    x=list(cur)
    do()
def do():
    global x
    global ran
    try:
        ele=x[ran]
        item.set(ele[0])
        lc=loc.set(ele[1])
        mark.set(ele[2]) 
        sno.set(ele[3])
        price.set(ele[4])
        dt.set(ele[5])
        where.set(ele[6])
        note.set(ele[7])
        photo.set(ele[8])
    except:
        messagebox.showerror("Error", "No Item Found")
def ex():
    answer = messagebox.askokcancel("Question","Do you want to close the application?")
    if answer:
        root.destroy()
    
root = Tk()
root.geometry("800x380+550+0")
root.title("Home Inventory Manager")
item=StringVar()
loc=StringVar()
mark=IntVar()
sno=StringVar()
price=StringVar()
dt=StringVar()
where=StringVar()
note=StringVar()
photo=StringVar()

tbar=Frame(root,bg="black",height=470,width=80)
tbar.grid(row=0,column=0,rowspan=8)

photo1 = PhotoImage(file = r"run.png")
np = photo1.subsample(3,3)
newb=Button(tbar,text="New",image=np,command=new,compound = TOP,width=70,activebackground="white")
newb.grid(row=0,column=0)

phot = PhotoImage(file = r"del.png")
dp = phot.subsample(3,3)
delb=Button(tbar,text="Delete",width=70,command=delete,image=dp,compound = TOP,activebackground="white")
delb.grid(row=1,column=0)

pho = PhotoImage(file = r"save.png")
sp = pho.subsample(3,3)
saveb=Button(tbar,text="Save",width=70,command=save,image=sp,compound = TOP,activebackground="white")
saveb.grid(row=2,column=0)

s1=ttk.Separator(tbar,orient="horizontal")
s1.grid(row=3,column=0,pady=4)

pho1 = PhotoImage(file = r"prev2.png")
pp = pho1.subsample(3,3)
prevb=Button(tbar,text="Previous",width=70,command=previous,image=pp,compound = TOP,activebackground="white")
prevb.grid(row=4,column=0)

pho2 = PhotoImage(file = r"next2.png")
n1p = pho2.subsample(3,3)
nextb=Button(tbar,text="Next",width=70,command=nexto,image=n1p,compound = TOP,activebackground="white")
nextb.grid(row=5,column=0)

s2=ttk.Separator(tbar,orient="horizontal")
s2.grid(row=6,column=0,pady=4)

exitb=Button(tbar,text="Exit",height=3,width=10,activebackground="white",command=ex,relief=RAISED)
exitb.grid(row=7,column=0)

Label(root,text="Inventory Item ",width=12,anchor=E).grid(row=0,column=1)

r1=Entry(root,width=100,textvariable=item)
r1.grid(row=0,column=2,columnspan=5,padx=10)

Label(root,text="Location ",width=12,anchor=E).grid(row=1,column=1)

r2=Entry(root,width=64,textvariable=loc)
r2.grid(row=1,column=2,columnspan=3,padx=10)

r3=Checkbutton(root,text="Marked?",variable=mark)
r3.grid(row=1,column=5,padx=10)

Label(root,text="Serial Number",width=12,anchor=E).grid(row=2,column=1)

r4=Entry(root,width=64,textvariable=sno)
r4.grid(row=2,column=2,columnspan=3,padx=10)

Label(root,text="Purchase Price",width=12,anchor=E).grid(row=3,column=1)

r5=Entry(root,width=40,textvariable=price)
r5.grid(row=3,column=2,columnspan=2,padx=10)

Label(root,text="Date Purchased",width=14,anchor=E).grid(row=3,column=4)

r6=DateEntry(root,width=20,textvariable=dt)
r6.grid(row=3,column=5)

Label(root,text="Store/Website",width=12,anchor=E).grid(row=4,column=1)

r7=Entry(root,width=100,textvariable=where)
r7.grid(row=4,column=2,columnspan=5,padx=10)

Label(root,text="Note",width=12,anchor=E).grid(row=5,column=1)

r8=Entry(root,width=100,textvariable=note)
r8.grid(row=5,column=2,columnspan=5,padx=10)

Label(root,text="Photo path",width=12,anchor=E).grid(row=6,column=1)

r9=Entry(root,width=100,bg="light yellow",textvariable=photo)
r9.grid(row=6,column=2,columnspan=5,padx=10)

pic1 = PhotoImage(file = r"pic1.png")
rp = pic1.subsample(3,3)
Button(root,text="View Photo",image=rp,command=photoo,compound =TOP,activebackground="white").grid(row=7,column=5)

searchf=LabelFrame(root,text="ItemSearch")
searchf.grid(row=7,column=1,columnspan=4)

alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ...."
btn=[]
i=0
for j in range(0,4):
    for k in range(7):
        if alpha[i]!=".":
            btn.append(Button(searchf,width=4,text=alpha[i],command=partial(bo,i),bg="light blue"))
            btn[i].grid(row=j,column=k)
            i+=1
        else:
            i+=1
            continue


root.mainloop()


