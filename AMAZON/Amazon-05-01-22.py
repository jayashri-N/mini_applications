from os import system as sys
adm=[{"id":"ad1","pass":1},{"id":"ad2","pass":2},{"id":"ad3","pass":3}]
mer=[{"id":"m1","pass":1,"user":[]},{"id":"m2","pass":2,"user":[]},{"id":"m3","pass":3,"user":[]}]
users=[{"id":"u1","pass":1,"wallet":15000},{"id":"u2","pass":2,"wallet":20000},{"id":"u3","pass":3,"wallet":10000}]
wait=[{"id":"w1","pass":1},{"id":"w2","pass":2}]
prod=[{"discount":0,"prodId":"101","name":"analog watch","price":2000,"type":"electronics","seller":"m1","stock":50,"count":0},
{"discount":10,"prodId":"101","name":"analog watch","price":1500,"type":"electronics","seller":"m2","stock":45,"count":0},
{"discount":20,"prodId":"102","name":"shoes","price":900,"type":"clothing","seller":"m1","stock":25,"count":0},
{"discount":0,"prodId":"103","name":"pencil","price":10,"type":"stationery","seller":"m1","stock":150,"count":0}]
cart=[{"id":"u1","cart":[]}]
rej=[]
orders=[]

def admin(inv):
    def works():
        global mer
        global wait
        global rej
        global prod
        while True:
            w=int(input("\n1.Approve \n2.Remove \n3.Add \n4.view products \n5.Exit \nEnter choice: "))
            if w==1:
                if len(wait)>0:
                    for i in wait:
                        print()
                        for j in i:
                            print(j,i[j])
                        ap=int(input("\n1.Approve \n2.Reject \nEnter choice: "))
                        if ap==1:
                            mer.append(i)
                        elif ap==2:
                            rej.append(i)
                        else:
                            print("enter valid input")
                            input("click enter")
                            sys("cls")
                    print("no merchants to review")
                    wait=[]
                    input("click enter")
                else:
                    print("no merchants to review")
                    input("click enter")

            elif w==2:
                x=mer
                mer=[]
                for i in x:
                    print()
                    for j in i:
                        print(j,i[j])
                    ap=int(input("\n1.keep \n2.Remove \nEnter choice: "))
                    if ap==1:
                        mer.append(i)
                    else:
                        continue
                print("no more merchants to review")
                input("click enter")

            elif w==3:
                d={}
                d["id"]=input("Enter merchant id: ")
                d["pass"]=int(input("enter a password:"))
                d["user"]=[]
                mer.append(d)
                input("click enter")
            
            elif w==4:
                for p in prod:
                    print("----------")
                    for ki,val in p.items():
                        print(ki,val)
                print("No more products to display")
                input("click enter")
                sys("cls")

            elif w<1 or w>5:
                print("enter valid input")
                admin(inv)
            
            elif w==5:
                break
        
    print("""\t\tADMINISTRATOR""")
    id=input("\nEnter user id: ")
    p=int(input("\nEnter password: "))
    usr=None
    for i in adm:
        if i["id"]==id and i["pass"]==p:
            usr=i
            print("welcome admin")
            works()
            break
    else:
        if inv<=3:
            inv+=1
            print("Incorrect UserId or Password")
            admin(inv)
        else:
            print("Attempts exceeded")
            input("press enter key to continue")

def mworks(i):
    global prod
    while(True):
        
        x=int(input("\n1.add product \n2.remove product \n3.update product \n4.review sales \n5.check stocks \n6.view customer frequency \n7.View product frequency \n8.Exit \nEnter choice: "))
        sys("cls")
        if x==1:
            y={"discount":0}
            pid=input("enter product id: ")
            name=input("enter product name: ")
            typ=input("product type: ")
            stock=int(input("Enter available stock: "))
            pri=int(input("enter selling price per unit: "))
            dis=int(input("enter discount percent if any:"))
            y["proId"]=pid
            y["name"]=name
            y["price"]=pri
            y["discount"]=dis
            y["type"]=typ
            y["seller"]=i["id"]
            y["stock"]=stock
            y["count"]=0
            prod.append(y)
            print("\nProduct added successfully")
            input("click enter")
            sys("cls")

        elif x==2:
            temp=prod
            prod=[]
            for j in temp:
                if j["seller"]==i["id"]:
                    print()
                    for k in j:
                        print(k,j[k])
                    tst=int(input("\n1.remove \n2.keep\nEnterchoice: "))
                    if tst==2:
                        prod.append(j)

                    elif x!=1 and x!=2:
                        print("enter valid input")
                        input("click enter")
                        sys("cls")
                        break

                    elif tst==1:
                        print("\nRemoved successfully")
                        
                else:
                    prod.append(j)
            print("no more products")
            input("click enter")
            sys("cls")

        elif x==3:
            pid=input("enter product id: ")
            for p in prod:
                if p["prodId"]==pid and p["seller"]==i["id"]:
                    while (True):
                        x=input("\n1.update price\n2.update discount\n3.update stock\n4.Exit\nEnter choice: ")
                        if x=="1":
                            print("current price is:",p["price"])
                            y=int(input("enter new price"))
                            p["price"]=y
                            print("Updation successful")
                            input("click enter")
                            sys("cls")

                        elif x=="2":
                            print("current discouont is:",p["discount"])
                            y=int(input("enter new discount percentage"))
                            p["discount"]=y
                            print("Updation successful")
                            input("click enter")
                            sys("cls")

                        elif x=="3":
                            print("current stock availablity is:",p["stock"])
                            y=int(input("enter updated stock availablity:"))
                            p["stock"]=y
                            print("Updation successful")
                            input("click enter")
                            sys("cls")

                        elif x!="1" and x!="2" and x!="3" and x!="4":
                            print("Enter valid input")
                            input("click enter")
                            sys("cls")

                        elif x=="4":
                            mworks(i)
            else:
                print("product not found")
            

        elif x==4:
            for w in orders:
                if w["seller"]==i["id"]:
                    print("---------")
                    for ki,val in w.items():
                        print(ki,val)
            input("click enter")
            sys("cls")

        elif x==5:
            for k in prod:
                if k["seller"]==i["id"]:
                    print("Product Id:",k["prodId"])
                    print("Product Name:",k["name"])
                    print("Stock available:",k["stock"])
                    print("------")
            print("No more products to display")
            input("click enter")
            sys("cls")

        elif x==6:
            for k in mer:
                if k["id"]==i["id"]:
                    c=i["id"]
                    l=[]
                    for z in c:
                        if z not in l:l.append(z)
                    print("user","count")
                    for y in l:
                        print(y,c.count(y))
            print("No more users to display")
            input("click enter")
            sys("cls")

        elif x==7:
            for k in prod:
                if k["seller"]==i["id"]:
                    print("Product Id:",k["prodId"])
                    print("Product Name:",k["name"])
                    print("pieces sold:",k["count"])
                    print("------")
            print("No more products to display")
            input("click enter")
            sys("cls")

        elif x<1 or x>8:
            print("Enter valid input")
            input("click enter")
            sys("cls")
            mworks(i)

        elif x==8:
            sys("cls")
            break
    
def merchant(inv):
    print("""\t\tMERCHANT""")
    while(True):
        typ=int(input("\n1.Existing user \n2.New user \n3.Check status \n4.exit \nEnter choice: "))
        if typ ==1:
            id=input("\nEnter user id: ")
            p=int(input("\nEnter password: "))
            usr=None
            for i in mer:
                if i["id"]==id and i["pass"]==p:
                    usr=i
                    mworks(usr)
                    break
            else:
                if inv<=3:
                    inv+=1
                    print("Incorrect UserId or Password")
                    merchant(inv)
                else:
                    print("Attempts exceeded")
                    input("press enter key to continue")
        elif typ==2:
            id=input("\nEnter user id: ")
            p=int(input("\nEnter password: "))
            for  i in mer:
                if i["id"]==id:
                    print("user id taken")
                    break
            else:
                x={"id":id,"pass":p}
                wait.append(x)
                print("information added for Admin's approval")
                input("press enter to continue")

        elif typ==3:
            id=input("\nEnter user id: ")
            p=int(input("\nEnter password: "))
            for  i in wait:
                if i["id"]==id and i["pass"]==p:
                    print("waiting for approval")
                    input("click enter")
                    sys("cls")
                    break
            else:
                for i in rej:
                    if i["id"]==id and i["pass"]==p:
                        print("Account rejected")
                        input("click enter")
                        sys("cls")
                        break

                else:
                    for i in mer:
                        if i["id"]==id and i["pass"]==p:
                            print("Account approved\nLog in as existing user")
                            input("click enter")
                    else:
                        print("Id not found")
                        input("click enter")

        elif typ!=1 and typ!=2 and typ!=3 and typ!=4:
            print("enter valid input")
            input("click enter")
            merchant(inv)

        elif typ==4:
            break

def orderF(i,k):
    print("product name: ",k["name"])
    print("price: ",k["price"])
    print("Discount: ",k["discount"],"%")
    x=int(input("\nConfirm order\n1.YES \t\t2.NO \nenter choice:"))
    if x==1:
        pm=""
        opt=int(input("\n1.Online wallet\n2.Cash On delivery \nEnter choice: "))
        if opt==1:
            if k["price"]<=i["wallet"]:
                pm="Online Wallet"
                i["wallet"]-=k["price"]
                s=k["seller"]
                for o in mer:
                    if o["id"]==s:
                        o["user"].append(i["id"])
                k["count"]+=1
                k["stock"]-=1
                print("\nOrder placed!!")
            else:
                print("Not enough balance in wallet")
                input("click enter")
                sys("cls")
                orderF(i,k)

        elif opt==2:
            pm="COD"
            s=k["seller"]
            for o in mer:
                if o["id"]==s:
                    o["user"].append(i["id"])
            k["count"]+=1
            print("order placed")
        if len(pm)>1:
            o={}
            o["name"]=k["name"]
            o["buyer"]=i["id"]
            o["seller"]=k["seller"]
            o["price"]=k["price"]
            o["pay"]=pm
            orders.append(o)


    elif x==2:
        uworks(i)

    else:
        print("Invalid input")
        input("click enter")
        sys("cls")
        orderF(i,k)

def cartF(i,k):
    for p in cart:
        if i["id"]==p["id"]:
            p["cart"].append(k)
            break
    else:
        x={}
        x["id"]=i["id"]
        x["cart"]=[k]
        cart.append(x)
    print("Added to cart")
        
def uworks(i):
    global prod
    global cart
    sys("cls")
    while(True):
        x=int(input("\n1.View all products \n2.search \n3.view cart \n4.check wallet \n5.Previous orders \n6.Exit \nEnter choice: "))
        if x==1:
            for k in prod:
                print("-------")
                print("product name: ",k["name"])
                print("price: ",k["price"])
                print("Discount: ",k["discount"],"%")
                print("seller id: ",k["seller"])
                print("stock available: ",k["stock"])
                z=int(input("1.Place order \n2.Add to cart \n3.next \n4.exit \n eenter choice: "))
                if z==1:
                    orderF(i,k)
                    break
                elif z==2:
                    cartF(i,k)
                    break
                elif z==3:
                    continue
                elif z<1 or z>4:
                    print("Enter valid input")
                    continue
                elif x==4:
                    break
                input("click enter")
                sys("cls")

        elif x==2:
            key=input("search by\n1.product name \n2.product type \nEnter choice: ")
            if key=="1":
                nm=input("Enter product name: ")
                for k in prod:
                    if k["name"]==nm:
                        print("-------")
                        print("product name: ",k["name"])
                        print("price: ",k["price"])
                        print("Discount: ",k["discount"],"%")
                        print("seller id: ",k["seller"])
                        print("stock available: ",k["stock"])
                        z=int(input("1.Place order \n2.Add to cart \n3.next \n4.exit \n eenter choice: "))
                        if z==1:
                            orderF(i,k)
                            break
                        elif z==2:
                            cartF(i,k)
                            break
                        elif z==3:
                            continue
                        elif z<1 or z>4:
                            print("Enter valid input")
                            continue
                        elif x==4:
                            break
                else:
                    print("Product not found")
                    input("click enter")
                    sys("cls")

            elif key=="2":
                nm=input("Enter product Type: ")
                for k in prod:
                    if k["type"]==nm:
                        print("-------")
                        print("product name: ",k["name"])
                        print("price: ",k["price"])
                        print("Discount: ",k["discount"],"%")
                        print("seller id: ",k["seller"])
                        print("stock available: ",k["stock"])
                        z=int(input("1.Place order \n2.Add to cart \n3.next \n4.exit ]nEnter choice: "))
                        if z==1:
                            orderF(i,k)
                            break
                        elif z==2:
                            cartF(i,k)
                            break
                        elif z==3:
                            continue
                        elif z<1 or z>4:
                            print("Enter valid input")
                            continue
                        elif x==4:
                            break
                else:
                    print("Product not found")
                    input("click enter")
                    sys("cls")
        elif x==3:
            sys("cls")
            print("-------cart-------")
            for h in cart:
                if h["id"]==i["id"]:
                    l1=h["cart"]
                    for l in l1:
                        print("-----")
                        for k,v in l.items():
                            if k!="count":
                                print(k,v)
                    break
            else:
                print("No items in cart")
            input("click enter to continue")
            sys("cls")
        
        elif x==4:
            print("\nBalance in e-wallet is:",i["wallet"])

        elif x==5:
            for k in orders:
                if k["buyer"]==i["id"]:
                    print("product name",k["name"])
                    print("price",k["price"])
                    print("Payment method",k["pay"])
                    break
            else:
                print("No previous orders")
    
        elif x<1 or x>6:
            print("Enter valid input")
            input("click enter")
            sys("cls")
            uworks(i)

        elif x==6:
            sys("cls")
            break
        input("click enter")
        sys("cls")
    
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
                z=int(input("Add amount to wallet: "))
                x["wallet"]=z
                users.append(x)
        elif typ!=1 and typ!=2 and typ!=3:
            print("enter valid input")
            input("click enter")
            user(inv)
        elif typ==3:
            sys("cls")
            break

while(True):
    sys("cls")
    print("""\t\tWelcome \n Log in as \n1.Admin \n2.Merchant \n3.User """)
    log=input("Enter your choice: ")
    if log=="1":
        inv=1
        admin(inv)
    elif log=="2":
        inv=1
        merchant(inv)
    elif log=="3":
        inv=1
        user(inv)
    
    elif log=="4":
        print("merchant",*mer,sep="\n")

    elif log!="1" or log !="2" or log!="3":
        print("Enter valid input")