from typing import Union

from fastapi import FastAPI 
from pydantic import BaseModel

class Groupshare(BaseModel):
    name : str 
    description : str 
    price : float 
    datestart : str
    userId : str 
    imageURL : str

    class Config:
        schema_extra = {
            "example" : {
             "name": "gxxxx",
             "description": "test test ",
             "price": 1000,
             "datestart": "20230418",
             "userId": "0001",
             "imageURL": "https://img.freepik.com/free-vector/money-bag_23-2147510861.jpg"
            }
        }

class Order(BaseModel):
    serviceType : str
    location : str
    provider : str 
    distance : int
    customer : str
    price : int
    eta : int


class Cat(BaseModel):
    name : str 
    breed : str
    age : int
    gender : str
    location : str


class Login(BaseModel):
    username : str 
    password : str
    userId : str 

class Profile(BaseModel):
    userId : str 
    userName : str 
    userType : str
    fullName : str 
    orgName : str
    position : str 
    tel : str
    phone : str
    email : str 
    address : str 



app = FastAPI()


@app.get("/")
def read_root():  
    print(" Somebody call /")
    return{"Hello" : "World"}  

@app.get("/items/{item_id}")
def read_item(item_id:str):
#def read_item(item_id:int , q: Union[str,None] = None):
    print(" we going to select * from product Item ID =" + item_id)
    return {"item_id" : item_id}
            #, "q" : q}

@app.post("/order")
def create_groupshare(order : Order) -> Order:
    order_dict = order.dict()
    # order_dict.update({"price": order.distance * 5})
    # order_dict.update({"eta": order.distance * 2})
    # order_dict.update({"results":"Successful"})

    order.price = order.distance * 5
    order.eta =  order.distance * 2
    
    #SQL insert into order values() 

    order.results = "Successful"

    return order_dict


@app.get("/list_cat")
def list_cat() ->list[Cat]:
    #SQL select * from cat 
    return [
        Cat(name="numnim",breed="Persia",age=5,gender="F",location="TBS libary"),
        Cat(name="momo",breed="Persia",age=5,gender="F",location="TBS entrance"),

    ]


@app.post("/create_groupshare")
def create_groupshare(groupshare : Groupshare):
    print("insert into groupshare values()")
    print("Create groupshare {0} for {1}".format(groupshare.name,groupshare.userId))

    groupshare_dict = groupshare.dict()
    groupshare_dict.update({"results":"Successful"})

    #return{"results " : "Successful"}
    return groupshare_dict



@app.post("/login")
def login(login : Login) -> Login:

    login_dict = login.dict()
   
    login_dict.update({"userId": "00001"})
    login_dict.update({"results":"Successful"})
   # login.results = "Successful"

    return login_dict



@app.get("/profile/{userId}")
def read_item(item_id:str):
#def read_item(item_id:int , q: Union[str,None] = None):
    print(" we going to select * from product Item ID =" + item_id)
    return {"userId" : item_id , 
            "userName" : " วิภาวดี นุชถาวร ",
            "userType" : "ลูกแชร์",
            "fullName" : "หญิงนุ้ย เทสเตอร์เกาหลี " , 
            "orgName" : "ธนาคารอาคารสงเคราะห์" ,
            "position" : "นักพัฒนาระบบ",
            "Tel" : "026459000" ,
            "Mobile" :"0891234567", 
            "Email" : " mim@gmail.com",
            "results":"Successful"}



province_db = [
    {
        "provinceId" : 1,
        "provinceName" : "กรุงเทพมหานคร"
    },
    {
        "provinceId" : 2,
        "provinceName" : "กระบี่"
    },
    {
        "provinceId" : 3,
        "provinceName" : "xxx"
    },
    {
        "provinceId" : 4,
        "provinceName" : "xxx"
    },
    
]



@app.get("/getprovince/")
async def get_province():
    return province_db


@app.get("/getprovince/{provinceId}")
async def get_province(provinceId: int):
    return province_db[provinceId]