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
    


bank=Bank()   

print("Press 1 for creating an account")
print("Press 2 for depositing money")
print("Press 3 for withdrawing money")
print("Press 4 for details of a user")
print("Press 5 updating user details")
print("Press 6 for deleting user")

res=int(input("Tell your response:-"))

if res==1:
    bank.create_user()

elif res==2:
    bank.deposite_money()
    

elif res==3:
    pass

elif res==4:
    pass

elif res==5:
    pass

elif res==6:
    pass

