#ATM APPLICATION

from os import system as sys
import datetime
amt={2000:0,500:0,200:0,100:0}
users = [{"user":"aaaa","pass":"0000","balance":100000,"bank":"xyz","count":5},{"user":"bbbb","pass":"1111","balance":200000,"bank":"abc","count":3}]
history={"aaaa":[],"bbbb":[]}
atmbal=0
dl=15000

def addAmt():
    global atmbal
    for i in amt:
        x=int(input("enter number of"+str(i)+":"))
        amt[i]+=x
        y=x*i
        atmbal+=y
    print("\nAmount added successfully!")

def Adcheckbal():
    global atmbal
    print("balance is:\n")
    for i in amt:
        print("Rs.",i,"x",amt[i])
    print("Total: ",atmbal)

def admin(i):
    inv=i
    u=["A","B","C"]
    p={"A":"1111","B":"2222","C":"3333"}
    
    ui=input("Please enter USER ID:")
    ps=input("Enter password: ")

    if (ui not in u or p[ui]!=ps) and inv<=3:
        print("Incorrect id or password")
        inv+=1
        admin(inv)
    
    elif ui in u and p[ui]==ps:
            print("Hello",ui)
            while(True):
                x=(input("""\t\n1.Add amount \n2.Check balance \n3.Exit \nEnter choice:"""))
                if x=="1":
                    sys("cls")
                    addAmt()
                elif x=="2":
                    sys("cls")
                    Adcheckbal()
                elif x!=1 and x!=2 and x!=3:
                    print("Enter valid input")
                    sys("cls")
                    break
                elif x=="3":
                    sys("cls")
                    break
            
    else:
        print("Attempts exceeded")
        input("press enter to continue")

def instance():
    x,y=map(str,str(datetime.datetime.now()).split())
    m=list(map(str,x.split("-")))
    m.reverse()
    date="-".join(m)
    n=list(map(str,y.split(".")))
    time=n[0]
    point=str(date)+" "+str(time)
    return(point)

def deposit(i):
    global atmbal
    global amt
    #print(i)
    #print(i["balance"])
    print("\t\t\t\t DEPOSIT")
    x={}
    y=0
    x[2000]=(int(input("enter number of 2000: ")))
    x[500]=(int(input("enter number of 500: ")))
    x[200]=(int(input("enter number of 200: ")))
    x[100]=(int(input("enter number of 100: ")))
    for j in x:
        amt[j]+=x[j]
    for j in x:
        y+=j*x[j]
    atmbal+=y
    i["balance"]+=y
    print("Rs.",y,"deposited successfully")
    h=instance()
    history[i["user"]].append("Action-deposit,"+h+" Rs. "+str(y))
    input("press enter to continue")

def denomCk(i,x):
    z={2000:0,500:0,200:0,100:0}
    p=0
    for d in z:
        j=x//d
        if j>0:
            z[d]=j   
        if z[d]<=amt[d] and z[d]!=0:
            x-=(j*d)
            amt[d]-=j
            p+=1
    i["count"]-=1
    return(bool(p))      

def withdraw(i):
    global atmbal
    x = int(input("\nEnter Amount to Withdraw:"))
    if x<=atmbal and x%100==0 and x<=dl:
        if x<=i["balance"]:
            if denomCk(i,x):
                if i["count"]<0:
                    x+=20
                i["balance"]-=x
                atmbal-=x
                print("\nWithdraw successful")
                h=instance()
                history[i["user"]].append("Action-withdraw, "+h+" Rs. "+str(x))
                input("press enter to continue")
            else:
                print("\nDenomination unavailable")
                input("press enter to continue")
        else:
            print("\nAccount Balance insufficient")
            input("press enter to continue")
    elif x%100!=0:
        print("Enter valid denomination")
        withdraw(i)
    elif x>dl:
        print("Daily limit exceeded")
        input("press enter to continue")
    else:
        print("\nDenomination unavailable")
        input("press enter to continue")

def transfer(i):
    y=input("Enter recepient id: ")
    x=int(input("Enter amount to transfer: "))
    for j in users:
        if j["user"]==y and i["balance"]<=x:
            j["balance"]+=x
            i["balance"]-=x
            print("Transfer successful!!")
            input("press enter to continue")
            break
        elif x>i["balance"]:
            print("blance insufficient")
            transfer(i)
    else:
        i["balance"]-=x
        print("Transfer successful!!")
        input("press enter to continue")
    h=instance()
    history[i["user"]].append("Action-transfer, "+h+" Rs. "+str(x))

def checkbalance(i):
    return(i["balance"])

def changeP(i):
    z=input("\nEnter new pin: ")
    i["pass"]=z
    print("Pin updated")
    input("press enter to continue")

def statement(i):
    global history
    x=i["user"]
    b="Balance: "+"Rs."+str(i["balance"])
    y=history[x]
    y.append(b)
    for i in y:
        print(i)
    input("press enter to continue")

def cust(inc):

    c=inc
    def scr(i):
        while(True):
                print("Hello",ui)
                x=int(input("""\t\n1.Withdraw \n2.Check balance \n3.Change pin \n4.Deposit \n5.Transfer \n6.Mini statement \n7.Exit \nEnter choice:"""))
                if x==1:
                    sys("cls")
                    withdraw(i)  
                elif x==2:
                    sys("cls")
                    print("Your balance is",checkbalance(i))
                    input("press enter to continue")
                elif x==3:
                    sys("cls")
                    changeP(i)
                elif x==4:
                    sys("cls")
                    deposit(i)
                elif x==5:
                    sys("cls")
                    transfer(i)
                elif x==6:
                    sys("cls")
                    statement(i)
                elif x>7 or x<1:
                    print("Enter valid input")
                    input("press enter to continue")
                elif x==7:
                    sys("cls")
                    break
    ui=input("Please enter USER ID:")
    pas=input("Enter password:")
    usr = None
    for i in users:
        if i["user"]==ui and i["pass"]==pas:
            scr(i)
            break
    else :
        c+=1
        print("Invalid user")
        input("press enter to continue")
        if c<=3:
            cust(c)
        else:
            print("Attempts exceeded")
            input("press enter to continue")
            breakpoint

while(True):
    print("""\t\tXYZ ATM \n1-ADMIN \n2-CUSTOMER \n3-EXIT""")
    x =int(input("enter choice:"))

    if x==1:
        inv=1
        admin(inv)
    elif x==2:
        inc=1
        cust(inc)
    elif x==3:
        print("\t\tThank you for using XYZ atm!!!\n\n\t\tHave a nice day😁")
    else:
        print("please enter valid input.")
        break

sys("cls")
