import json
import random
import string
from pathlib import Path

class Bank: 
    database="database.json"
    data=[]


    if Path(database).exists():
        with open(database) as fs:
            data =json.loads(fs.read())
    

    @classmethod           
    def __update(cls):
        with open(cls.database,'w') as fs:
            fs.write(json.dumps(cls.data))
    
    @classmethod
    def __accountgenerate(cls):
        alpha=random.choices(string.ascii_letters,k=8)
        num=random.choices(string.digits,k=4)
        acc=alpha+num
        random.shuffle(acc)
        return"".join(acc)


    def create_user(self):
        info={
            "name":input("Tell user Name:-"),
            "age":int(input("Tell user Age:-")),
            "email":input("Tell user Email:-"),
            "AccountNo.":Bank.__accountgenerate(),
            "pin":int(input("Tell user Pin:-")),
            "balance":0 
        }
        
        if info['age']<12 or len(str(info["pin"])) !=4 :
            print("sorry cannot create account")
        else:
            Bank.data.append(info)
            bank.__update()

    def deposite_money(self):
        accno=input("Tell your account number :-")
        pin=int(input("tell your pin:-"))
        userdata=[i for i in Bank.data if i['AccountNo.']==accno and i['pin']==pin]

        if userdata==False:
            print("sorry no such user exist")
        else:
            amount=int(input("Money :-"))
            userdata[0]['balance']+=amount  #copy by references agr isme change karnge to data mei change ho jayega 
            bank.__update()
            print("Balance added successfully")




    def withdraw_money(self):
        accno=input("Tell your account number :-")
        pin=int(input("tell your pin:-"))
        userdata=[i for i in Bank.data if i['AccountNo.']==accno and i['pin']==pin]

        if userdata==False:
            print("sorry no such user exist")
        else:
            amount=int(input("Money :-"))
            if amount>userdata[0]['balance']:
                print("insufficient balance")

            userdata[0]['balance']-=amount  #copy by references agr isme change karnge to data mei change ho jayega 
            bank.__update()
            print("Balance withdraw successfully")



    def show_details():
        accno=input("Tell your account number :-")
        pin=int(input("tell your pin:-"))
        userdata=[i for i in Bank.data if i['AccountNo.']==accno and i['pin']==pin]
        if not userdata:
            print("No data found!")
        else:
             for i in userdata[0]:
                 print(f"{i} - {userdata[0][i]}")

    
    def update_details():
        accno=input("Tell your account number :-")
        pin=int(input("tell your pin:-"))
        userdata=[i for i in Bank.data if i['AccountNo.']==accno and i['pin']==pin]
        if not userdata:
            print("No user found!")
        else:
            print("you cannot change bankbalance account number and age")
             
            newdata={
                "name": input("Tell your new name or press enter to skip"),
                "email": input("Tell your new mail or press enter to skip"),
                "pin": input("Tell your new pin or press enter to skip")    
            }

            if newdata['name']=="":
                newdata['name']=userdata[0]['name']
            if newdata['email']=="":
                newdata['email']=userdata[0]['email']
            if newdata['pin']=="":
                newdata['pin']=userdata[0]['pin']
            
            for i in userdata[0]:
                if i in newdata:
                    userdata[0][i]=newdata[i]
                if i =="pin":
                    userdata[0][i]=int(newdata[i])
            Bank.__update()

    def delete_account():
        accno=input("Tell your account number :-")
        pin=int(input("tell your pin:-"))
        userdata=[i for i in Bank.data if i['AccountNo.']==accno and i['pin']==pin]

        if userdata==False:
            print("No such user")
        else:
            print("Are you sure you want to delete")
            check=input("Press y (YES) or n (NO)")
            if check=="y":
                index=Bank.data.index(userdata[0])
                Bank.data.pop(index)
                Bank.__update()

bank=Bank()   
while True:
    print("Press 1 for creating an account")
    print("Press 2 for depositing money")
    print("Press 3 for withdrawing money")
    print("Press 4 for details of a user")
    print("Press 5 updating user details")
    print("Press 6 for deleting account")
    print("Press 0 for Exit")

    res=int(input("Tell your response:-"))

    if res==1:
        bank.create_user()

    elif res==2:
        bank.deposite_money()

    elif res==3:
        bank.withdraw_money()

    elif res==4:
        bank.show_details()

    elif res==5:
        bank.update_details()

    elif res==6:
        bank.delete_account()

    elif res==0:
        break

    else:
        print("invalid input try again")

    


