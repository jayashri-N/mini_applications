from os import system as sys

adm=[{"id":"ad1","pass":"1"},{"id":"ad2","pass":"2"}]
trav=[{"id":"trav1","pass":"1"},{"id":"trav2","pass":"2"},{"id":"trav3","pass":"3"}]
train=[]
place=[]        #["train"],["seats"]
wait=[]         #usrid, train,num,st,ed

def test():
        print("admin",*adm,sep="\n")
        print("passengers",*trav,sep="\n")
        print("trains",*train,sep="\n")
        print("place")
        for i in place:
            print("train: ",i["train"])
            for s in i["seats"]:
                print(*s)
        print("wait list",*wait,sep="\n")

def addTrain():
        nm=input("Enter train name: ")
        c=int(input("Enter number of stations: "))
        x={}
        for i in range(1,c+1):
                    print("Enter station ",i," : ",sep="")
                    sn=input()
                    x[i]=sn
        s=int(input("Enter total seat availablity: "))
        y={"name":nm,"stations":x,"seats":s}
        train.append(y)
        p={}
        array=[[0 for j in range(c)] for i in range(s)]
        p["train"]=nm
        p["seats"]=array
        place.append(p)
        print("Train added successfully!")
        input("Click Enter")
        sys("cls")

def addStation():
        nm=input("Enter train name to add stations: ")
        temp=0
        for i in train:
            if i["name"]==nm:
                tr=i
                st=tr["stations"]
                tr["stations"]={}
                temp+=1
                c=int(input("Enter number of new stations: "))
                x={}
                for j in range(1,len(st)+c+1):
                    print("Enter station ",j," : ",sep="")
                    sn=input()
                    x[j]=sn
                tr["stations"]=x
                print("Stations updated!")
                input("click enter")
                sys("cls")
        if temp==0:
            print("Train not found")

def updateSeat():
        nm=input("Enter train name to update seats: ")
        temp=0
        for i in train:
            if i["name"]==nm:
                temp+=1
                tr=i
                st=tr["seats"]
                c=len(tr["stations"])
                print("Seat availablity: ",st)
                x=int(input("Enter new seat availablity: "))
                tr["seats"]=x
                for t in place:
                    if t["train"]==nm:
                        z={}
                        z["train"]=nm
                        place.remove(t)
                        array=[[0 for j in range(c)] for i in range(x)]
                        z["seats"]=array
                        place.append(z)
                print("Seats updated successfully!!")
                sys("cls")
                break
        if temp==0:
            print("Train not found")

def adtasks(user):
        while(True):

            wrk=int(input("\n1.Add trains \n2.Add stations \n3.Update seat availablity \n0.Exit \nENTER CHOICE: "))
            if wrk==1:
                addTrain()
            elif wrk==2:
                addStation()
            elif wrk==3:
                updateSeat()    
            elif wrk==0:
                break

def admin(inv):
        inp=input("Enter admin id: ")
        p=(input("Enter password: "))
        for i in adm:
                if i["id"]==inp and i["pass"]==p:
                    user=i
                    print("------ADMINISTRATOR-------")
                    adtasks(user)
                    input("Click Enter")
                    break
        else:
                print("Invalid user id or password")
                inv+=1
                if inv<=3:
                    adm(inv)
                else:
                    print("Attempts exceeded")
                    input("Click enter")
                    sys("cls")

def viewavail(user):
        for i in place:
            for k,v in i.items():
                if k=="train":
                    print(k,v)
                elif k=="seats":
                    print(k)
                    for l in v:
                        print(*l,sep="\t")
        input("Click Enter")
        passTasks(user)

def bookTickets(user):
        t=input("Enter train name: ")
        num=int(input("Enter number of seats needed: "))
        trn=None
        for i in place:
            if i["train"]==t:
                trn=i
        array=trn["seats"]
        se=len(array)
        st=len(array[0])
        for p in range(num):
            st=int(input("Enter starting station number: "))
            ed=int(input("Enter ending station number: "))
            for i in range(se):
                if sum(array[i][st-1:ed-1])==0:
                    print("seat allocated is",i)
                    for j in range(st-1,ed):
                        array[i][j]=p+1
                    print("Seat Reservation success!")
                    break
            else:
                x={"usrid":user["id"],"train":t,"seats needed":num,"start":st,"end":ed}
                wait.append(x)
                print("seats Unavailable.\nRequest added to waiting list.")
                break

def passTasks(user):
        tsk=int(input("\n1.View trains and their availablity \n2.Book tickets \n0.Exit \nENTER CHOICE: "))
        if tsk==1:
            viewavail(user)
        if tsk==2:
            bookTickets(user)
        if tsk==0:
            return

def pasenger(inv):
        typ=int(input("\n1.Existing user \n2.New user \n0.Exit \nENTER CHOICE: "))
        if typ==1:
            inp=input("Enter user id: ")
            p=(input("Enter password: "))
            for i in trav:
                if i["id"]==inp and i["pass"]==p:
                        user=i
                        print("------PASSENGER-------")
                        passTasks(user)
                        input("Click Enter")
                        sys("cls")
                        break
            else:
                print("Invalid user id or password")
                inv+=1
                if inv<=3:
                    adm(inv)
                else:
                    print("Attempts exceeded")
                    input("Click enter")
                    sys("cls")
        elif typ==2:
            l=len(trav)+1
            uid="trav"+str(l)
            print("Your user id is: ",uid)
            p=input("Enter password: ")
            z={"id":uid,"pass":p}
            trav.append(z)
            print("User added successfully!")
            input("Click enter")
            sys("cls")

while (True):
        sys("cls")
        print("----------WELCOME--------------")
        login=int(input("\n1.Admin \n2.Passenger \n3.test \nEnter choice:"))
        if login==1:
            inv=1
            admin(inv)
        elif login==2:
            inv=1
            pasenger(inv)

        elif login==3:
            test()

        elif login !=1 or login !=2:
            print("\nEnter valid input")
            input("Click enter")
            continue

        print("Thank you for using online booking services")
        input("Click enter")
        sys("cls")

