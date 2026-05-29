import json
import random
import string
from pathlib import Path

class Bank: 
    database="database.json"
    data=[]


    with open(database) as fs:
        data =json.loads(fs.read())
    

    @classmethod            # samjh nhi aaya 
    def __update(cls):
        with open(cls.database,'w') as fs:
            fs.write(json.dumps(cls.data))


    
    def create_user(self):
        info={
            "name":input("Tell user Name:-"),
            "age":int(input("Tell user Age:-")),
            "email":input("Tell user Email:-"),
            "AccountNo.":"123dxc34612",
            "pin":int(input("Tell user Pin:-")),
            "balance":0
        }

        if info['age']<12 or len(str(info["pin"])) !=4 :
            print("sorry cannot create account")
        
        else:
            Bank.data.append(info)
            bank.__update()

    


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
    pass

elif res==3:
    pass

elif res==4:
    pass

elif res==5:
    pass

elif res==6:
    pass