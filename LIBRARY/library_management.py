from os import system as sys
from datetime import datetime
from datetime import timedelta

adm=[{"id":"ad1@gmail.com","pass":1},{"id":"ad2@gmail.com","pass":2},{"id":"ad3@gmail.com","pass":3}]
users=[{"id":"u1@gmail.com","pass":1,"balance":1500,"out":0},{"id":"u2@gmail.com","pass":2,"balance":1000,"out":0},{"id":"u3@gmail.com","pass":3,"balance":1500,"out":0}]
book=[{"name":"i'm malala","ISBN":"buk1","total":15,"avail":10,"count":0},{"name":"pi","ISBN":"buk2","total":10,"avail":5,"count":1},{"name":"wings of fire","ISBN":"buk3","total":20,"avail":15,"count":2},{"name":"physics","ISBN":"buk4","total":10,"avail":3,"count":3}]
cart=[{}]
out=[]
trans=[]
def report():
    z=int(input("\n1.Unreturned books \n2.Most Borrowed \n3.Least borrowed \n4.Refill requirement \n5.Search book \n0.Exit \nEnter choice: "))
    if z==1:
        for i in out:
            print("------------")
            for k,v in i.items():
                print(k,v,sep="   ")
        input("Click enter")
        sys("cls")
    elif z==2:
        l=[]
        u=[]
        for i in book:
            for j in range(i["count"]):
                l.append(i["name"])
        z=sorted(l,key=l.count,reverse=True)
        for i in z:
            if i not in u:
                u.append(i)
        print("List of books in the Descending order of frequency:")
        print(*u,sep="\n")

    elif z==3:
        l=[]
        u=[]
        for i in book:
            for j in range(i["count"]):
                l.append(i["name"])
        z=sorted(l,key=l.count)
        for i in z:
            if i not in u:
                u.append(i)
        print("List of books in the Ascending order of frequency:")
        print(*u,sep="\n")
    
    if z==4:
        l=[]
        for i in book:
            if i["total"]<3:
                l.append(i["name"])
        if len(l)==0:
            print("No refill needed")
        else:
            print("Refill required for:")
            print(*l,sep="\n")

def works(usr):
    global book
    while True:
            print("----Administrator----")
            w=int(input("\n1.search \n2.View all books \n3.Add\delete book \n4.update book availability \n5.Add admin \n6.Add borrower \n7.View reports \n0.Exit \nEnter choice: "))
            if w==1:
                key=int(input("\n1.Search by name \n2.search by ISBN \n3.exit \nEnter choice: "))
                if key==1:
                    nm=input("Enter book name: ")
                    for i in book:
                        if i["name"]==nm:
                            print("----------")
                            print("Book: ",i["name"])
                            print("ISBN: ",i["ISBN"])
                            print("Total books",i["total"])
                            print("Books available: ",i["avail"])
                            input("\nclick enter to continue")
                            sys("cls")
                            break
                    else:
                        print("Book not found")
                elif key==2:
                    nm=input("Enter ISBN: ")
                    for i in book:
                        if i["ISBN"]==nm:
                            print("Book: ",i["name"])
                            print("ISBN: ",i["ISBN"])
                            print("Total books",i["total"])
                            print("Books available: ",i["avail"])
                            input("\nclick enter to continue")
                            sys("cls")
                            break
                    else:
                        print("Book not found")
            elif w==2:
                for i in book:
                    print()
                    for k,v in i.items():
                        print(k,v)
                print("No more books to display")
                input("click enter")
                sys("cls")
                
            elif w==3:
                    act=int(input("\n1.Add book \n2.Delete book \n3.Exit \nEnter choice:"))
                    if act==1:
                        nm=input("Enter book name: ")
                        isbn=input("Enter ISBN number: ")
                        tot=int(input("Enter total number of books: "))
                        new={}
                        new["name"]=nm
                        new["ISBN"]=isbn
                        new["total"]=tot
                        new["avail"]=tot
                        book.append(new)
                        print("Book added successfully!")
                        input("Click enter")
                        sys("cls")
                        
                    elif act==2:
                        nm=input("Enter ISBN: ")
                        x=book
                        book=[]
                        for i in x:
                            if i["ISBN"]==nm:
                                print("\nBook Removed successfully!")
                                continue
                            else:
                                book.append(i)
                            break
                        else:
                            print("\nBook not found.")

                        input("Click enter")
                        sys("cls")
                    elif act<1 or act>3:
                        print("Enter valid input")
                        works(usr)
                    elif act==3:
                        input("Press enter")
                        sys("cls")
                        break
            elif w==4:
                    nm=input("Enter book name: ")
                    for i in book:
                        if i["name"]==nm:
                            print("\n\n")
                            print("Book: ",i["name"])
                            print("ISBN: ",i["ISBN"])
                            print("Total books",i["total"])
                            print("Books available: ",i["avail"])
                            upd=int(input("Enter current availability: "))
                            z=upd-i["total"]
                            i["total"]=upd
                            i["avail"]+=z
                            print("\nUpdate successful")
                            input("\n\tClick enter")
                            sys("cls")
                            break
                    else:
                        print("Book not found")
                        input("\n\tClick enter")
                        sys("cls")
      
            elif w==5:
                    print()
                    nm=input("Enter new admin's mail id: ")
                    pas=(input("enter a numerical password:"))
                    if pas.isdigit():
                        z={"id":nm,"pass":int(pas)}
                        adm.append(z)
                        print("\nAdmin added successfully!!")
                        input("\n\tClick enter")
                        sys("cls")
                    else:
                        print("\nError!!Enter only numerical value")
                        input("\n\tClick enter")
                        sys("cls")
                        works(usr)
            elif w==6:
                    nm=input("Enter new user's mail id: ")
                    pas=(input("enter a numerical password;"))
                    bal=input("Enter deposit amount: ")
                    if pas.isdigit() and bal.isdigit():
                        z={"id":nm,"pass":int(pas),"balance":int(bal)}
                        users.append(z)
                        print("\nUser added successfully!!")
                        input("\t\tclick enter")
                        sys("cls")
                    else:
                        print("\nError!!Enter only numerical value")
                        input("\t\tclick enter")
                        sys("cls")
                        works(usr)
            elif w==7:
                report()
                input("Click enter")
                sys("cls")

            elif w<0 or w>7:
                    print("\nenter valid input")
                    input("\t\tclick enter")
                    works(usr)   
            elif w==0:
                print("\nThank you! Have a smiley day!") 
                input("\t\tClick enter")
                break
                                    
def admin(inv):
    print("""\t\tADMINISTRATOR""")
    id=input("\nEnter user id: ")
    p=int(input("\nEnter password: "))
    usr=None
    sys("cls")
    for i in adm:
        if i["id"]==id and i["pass"]==p:
            usr=i
            print("welcome admin")
            works(usr)
            break
    else:
        if inv<=3:
            inv+=1
            print("Incorrect UserId or Password")
            admin(inv)
        else:
            print("Attempts exceeded")
            input("press enter key to continue")

def ret(usr):
    b=input("enter book title:")
    d,m,y=map(int,input("Enter date in dd/m/yyyy format: ").split())
    re=datetime(y,m,d)
    y=str(re).split(" ",1)[0]
    for i in out:
        if i["id"]==usr["id"]:
            if b in i["book"]: 
                d1=str(re-i["due"])
                d=d1[:2]
                delay=int(d)
                if delay<=0:
                    usr["out"]-=1
                    z={"id":usr["id"],"book":b,"action":"Return","return date":y,"comment":"No dues"}
                    trans.append(z)
                    print("Return updated")
                elif delay>0:
                    fine=(2**(delay//10))*delay
                    usr["balance"]-=fine
                    com=str(delay)+"days delay"
                    z={"id":usr["id"],"book":b,"action":"Return","return date":y,"comment":com}
                    trans.append(z)
                    usr["out"]-=1
                    print("\n",delay,"days delay from due date.\nRs.",fine,"was deducted from your deposit.\nCurrent balance is:",usr["balance"])
                out.remove(i)
                break

        for i in book:
            if i["name"]==b:
                i["avail"]+=1
                break
        input("click enter")
        sys("cls")

def incCount(c):
    for i in book:
        if i["name"]==c:
            i["count"]+=1
            break

def check(usr):
    for i in cart:
        if i["user"]==usr["id"]:
            c=i["book"]
            i["book"]=[]
            for j in i["book"]: 
                print("Book: ",j)
                x=int(input("\n1.Check out \n2.continue \nEnter choice: "))
                if x==1:        
                    if usr["balance"]<500:
                        print("cannot checkout.Deposit is less than 500.")
                    elif usr["out"]>=3:
                        print("Cannot checkout more than 3 books")
                    else: 
                        for k in c:
                            if k["name"]==j:
                                k["avail"]-=1   
                        usr["out"]+=1
                        t=datetime(2022,3,9)
                        y=str(t).split(" ",1)[0]
                        dt=t+timedelta(days=20)
                        z1=str(dt).split(" ",1)[0]
                        z={"id":usr["id"],"book":j,"action":"Out","outdate":y,"due":dt}
                        z2={"id":usr["id"],"book":j,"action":"Out","outdate":y,"due":z1}
                        out.append(z)
                        trans.append(z2)
                        print("Book checked out successfully!")
                        incCount(j)
                elif x==2:
                    i["book"].append(j)
                    continue

def uworks(usr):
    global book
    while True:
            print("----BORROWER----")
            w=int(input("\n1.View all books \n2.Search book  \n3.checkout books \n4.Return book \n5.My report\n0.Exit \nEnter choice: "))
            
            if w==1:
                for i in book:
                    print()
                    for k,v in i.items():
                        print(k,v)
                print("No more books to display")
                input("click enter")

            elif w==2:
                sys("cls")
                key=int(input("\n1.Search by name \n2.search by ISBN \n3.exit \nEnter choice: "))
                buk=None
                if key==1:
                    nm=input("Enter book name: ")
                    for i in book:
                        if i["name"]==nm:
                            print("----------")
                            print("Book: ",i["name"])
                            print("ISBN: ",i["ISBN"])
                            print("Total books",i["total"])
                            print("Books available: ",i["avail"])
                            buk=i
                            input("\nclick enter to continue")
                            break
                    else:
                        print("\nBook not found")
                elif key==2:
                    nm=input("Enter ISBN: ")
                    for i in book:
                        if i["ISBN"]==nm:
                            print("Book: ",i["name"])
                            print("ISBN: ",i["ISBN"])
                            print("Total books",i["total"])
                            print("Books available: ",i["avail"])
                            buk=i
                            input("\nclick enter to continue")
                            break
                    else:
                        print("\nBook not found")

                if buk!=None:
                    act=int(input("\n1.add to cart \n2.continue \nEnter choice: "))
                    if act==1:
                        us=usr["id"]
                        b=buk["name"]
                        for i in cart:
                            if i["user"]==us:
                                if b not in i["book"]:
                                    i["book"].append(b)
                                    print("Book added successfully")
                                    input("click enter")
                                    break
                                    
                                else:
                                    print("Cant add the same book twice")
                                    input("click enter")
                                    break
                                    
                        else:
                            x={"user":us,"book":[]}
                            x["book"].append(b)
                            
                            cart.append(x)
                            print("Book added successfully")
                            input("click enter")
                            break
                    if act==2:
                        sys("cls")
                        continue
            elif w==3:
                check(usr)
                input("click enter")
                sys("cls")
            elif w==4:
                ret(usr)
                input("click enter")
                sys("cls")
            elif w==5:
                x=int(input("\n1.View previous borrows \n2.View previous fines \n0.Exit\nEnter choice: "))
                if x==1:
                    for i in trans:
                        if i["id"]==usr["id"] and i["action"]=="out":
                            print("book",i["book"])
                            print("Outdate",i["outdate"])
                            print("Due Date",i["due"])
                            break
                    else:
                        print("No books borrowed")
                elif x==2:
                    temp=0
                    for i in trans:
                        if i["id"]==usr["id"] and i["action"]=="Return" and i["comment"]!="No dues":
                            print("book",i["book"])
                            print("Return date",i["return date"])
                            print("Reason",i["comment"])  
                            temp+=1      
                    else:
                        if temp==0:
                            print("No fines")
                    input("click enter")
                    sys("cls")

                elif x==0:
                    break

            elif w==0:
                break 

def user(inv):
    print("""\t\tUSER""")
    while(True):
        typ=int(input("\n1.Existing user \n2.New user \n3.Exit\nEnter choice: "))
        if typ==1:
            id=input("\nEnter user id: ")
            p=int(input("\nEnter password: "))
            usr=None
            for i in users:
                if i["id"]==id and i["pass"]==p:
                    usr=i
                    print("Hello",id)
                    uworks(usr)
                    break
            else:
                if inv<=3:
                    inv+=1
                    print("Incorrect UserId or Password")
                    admin(inv)
                else:
                    print("Attempts exceeded")
                    input("press enter key to continue")
        elif typ==2:
            id=input("\nEnter user id: ")
            p=int(input("\nEnter password: "))
            for  i in users:
                if i["id"]==id:
                    print("user id taken")
                    break
            else:
                x={"id":id,"pass":p}
                z=int(input("Add amount to deposit: "))
                if z<1500:
                    print("Minimum initial deposit is Rs.1500")
                    input("click enter")
                    sys("cls")
                    user(inv)
                else:
                    x["balance"]=z
                    users.append(x)

        elif typ!=1 and typ!=2 and typ!=3:
            print("enter valid input")
            input("click enter")
            user(inv)
        elif typ==3:
            sys("cls")
            break
        input("Click enter")
        sys("cls")

while(True):
    sys("cls")
    print("""\t\tWelcome \n Log in as \n1.Admin \n2.User \n3.test \n""")
    log=input("Enter your choice: ")
    if log=="1":
        inv=1
        sys("cls")
        admin(inv)
    elif log=="2":
        inv=1
        sys("cls")
        user(inv)
    
    elif log=="3":
        print("Admin",*adm,sep="\n")
        print("borrowers",*users,sep="\n")
        print("books",*book,sep="\n")
        print("cart",*cart,sep="\n")
        print("out",*out,sep="\n")
        print("trans",*trans,sep="\n")
        input("click enter")

    elif log!="1" or log !="2" or log!="3":
        print("Enter valid input")