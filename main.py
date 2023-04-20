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
    results : str 


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
    provinceId : int
    amphoesId: int
    tambonsId: int
    zipcode : str
    imagepath : str
    isActive : str
    result :str



app = FastAPI()


# @app.get("/")
# def read_root():  
#     print(" Somebody call /")
#     return{"Hello" : "World"}  

# @app.get("/items/{item_id}")
# def read_item(item_id:str):
# #def read_item(item_id:int , q: Union[str,None] = None):
#     print(" we going to select * from product Item ID =" + item_id)
#     return {"item_id" : item_id}
#             #, "q" : q}

# @app.post("/order")
# def create_groupshare(order : Order) -> Order:
#     # order_dict = order.dict()
#     # order_dict.update({"price": order.distance * 5})
#     # order_dict.update({"eta": order.distance * 2})
#     # order_dict.update({"results":"Successful"})
    
#     #SQL insert into order values() 
#     order.price = order.distance * 5
#     order.eta =  order.distance * 2
#     order.results = "Successful"

#     return order


# @app.get("/list_cat")
# def list_cat() ->list[Cat]:
#     #SQL select * from cat 
#     return [
#         Cat(name="numnim",breed="Persia",age=5,gender="F",location="TBS libary"),
#         Cat(name="momo",breed="Persia",age=5,gender="F",location="TBS entrance"),

#     ]


@app.post("/login")
def login(login : Login) -> Login:

    login_dict = login.dict()
   
    login_dict.update({"userId": "00001"})
    login_dict.update({"results":"Successful"})
   # login.results = "Successful"

    return login_dict



# @app.get("/profile/{userId}")
# def read_item(item_id:str):
# #def read_item(item_id:int , q: Union[str,None] = None):
#     print(" we going to select * from product Item ID =" + item_id)
#     return {"userId" : item_id , 
#             "userName" : " วิภาวดี นุชถาวร ",
#             "userType" : "ลูกแชร์",
#             "fullName" : "หญิงนุ้ย เทสเตอร์เกาหลี " , 
#             "orgName" : "ธนาคารอาคารสงเคราะห์" ,
#             "position" : "นักพัฒนาระบบ",
#             "Tel" : "026459000" ,
#             "Mobile" :"0891234567", 
#             "Email" : " mim@gmail.com",
#             "results":"Successful"}



@app.get("/get_profile/{user_id}")
def read_item(item_id:str):
#def read_item(item_id:int , q: Union[str,None] = None):
    print(" we going to select * from profile userId =" + item_id)
    return {"userId" : item_id , 
            "userName" : " วิภาวดี นุชถาวร ",
            "userType" : "ลูกแชร์",
            "fullName" : "หญิงนุ้ย เทสเตอร์เกาหลี " , 
            "orgName" : "ธนาคารอาคารสงเคราะห์" ,
            "position" : "นักพัฒนาระบบ",
            "Tel" : "026459000" ,
            "Mobile" :"0891234567", 
            "Email" : " mim@gmail.com",
            "Address" : "wwwwwww",
            "Imagepath" : " ../image/aaaa.jpg",
            "IsActive" : "Y",
            "results":"Select Successful"}

@app.post("/edit_profile/")
def edit_item(profile:Profile) -> Profile:
    #profile_dict = profile.dict()
    profile.result = "Update Successful"
    print(" we going to update profile Item ID =" + profile.userId + profile.userName)
   
    return profile


@app.put("/lock_profile/{user_id}")
def lock_item(item_id:str):
    print(" we going to change status profile Item ID =" + item_id)
    return {"userId" : item_id , 
            "IsActive" : "N",
            "results":"Lock User Successful"}


@app.delete("/delete_profile/{user_id}")
def delete_item(item_id:str):
#def read_item(item_id:int , q: Union[str,None] = None):
    print(" we going to delete profile Item ID =" + item_id)
    return {"results":"Delete Successful"}



@app.get("/eKYC_Dopa/{citizen_id}")
def read_item(item_id:str):
#def read_item(item_id:int , q: Union[str,None] = None):
    print(" we going to  eKYC_Dopa  ID =" + item_id)
    return {"citizen_id" : item_id , 
            "CardNumber" : " GE02 ",
            "RequestNumber" : " วิภาวดี นุชถาวร ",
            "NCBScore" : "754",
            "results":"true"}

@app.get("/eKYC_NCB/{citizen_id}")
def read_item(item_id:str):
#def read_item(item_id:int , q: Union[str,None] = None):
    print(" we going to  eKYC_NCB  ID =" + item_id)
      
    return {"citizen_id" : item_id , 
            "userName" : " วิภาวดี นุชถาวร ",
            "NCBType" : " GE02 ",
            "NCBScore" : "754",
            "NCBScoreType" : " AA " , 
            "NCBCredit" : "99%" ,
            "CheckDate" : "20230425 20:00",
            "results":"Select / Insert Successful"}


class Province(BaseModel):
    province_id : int
    province_name : str

class Amphoes(BaseModel):
    province_id : int
    amphoes_id: int
    amphoes_name : str

class Tambons(BaseModel):
    amphoes_id: int
    tambons_id: int
    tambons_name : str
    zipcode : str

@app.get("/list_province")
def list_province() ->list[Province]:
    #SQL select * from city 
    return [
        Province(province_id=1,province_name="กรุงเทพมหานคร"),
        Province(province_id=2,province_name="กระบี่"),
        Province(province_id=3,province_name="กาญจนบุรี"),
        Province(province_id=4,province_name="กาฬสินธุ์"),
        Province(province_id=5,province_name="กำแพงเพชร"),
        Province(province_id=6,province_name="ขอนแก่น"),
        Province(province_id=7,province_name="จันทบุรี"),
        Province(province_id=8,province_name="ฉะเชิงเทรา"),
        Province(province_id=9,province_name="ชลบุรี"),
        Province(province_id=10,province_name="ชัยนาท"),
        Province(province_id=11,province_name="ชัยภูมิ"),
        Province(province_id=12,province_name="ชุมพร"),
        Province(province_id=13,province_name="เชียงราย"),
        Province(province_id=14,province_name="เชียงใหม่"),
        Province(province_id=15,province_name="ตรัง"),
        Province(province_id=16,province_name="ตราด"),
        Province(province_id=17,province_name="ตาก"),
        Province(province_id=18,province_name="นครนายก"),
        Province(province_id=19,province_name="นครปฐม"),
        Province(province_id=20,province_name="นครพนม"),
        Province(province_id=21,province_name="นครราชสีมา"),
        Province(province_id=22,province_name="นครศรีธรรมราช"),
        Province(province_id=23,province_name="นครสวรรค์"),
        Province(province_id=24,province_name="นนทบุรี"),
        Province(province_id=25,province_name="นราธิวาส"),
        Province(province_id=26,province_name="น่าน"),
        Province(province_id=27,province_name="บึงกาฬ"),
        Province(province_id=28,province_name="บุรีรัมย์"),
        Province(province_id=29,province_name="ปทุมธานี"),
        Province(province_id=30,province_name="ประจวบคีรีขันธ์"),
        Province(province_id=31,province_name="ปราจีนบุรี"),
        Province(province_id=32,province_name="ปัตตานี"),
        Province(province_id=33,province_name="พระนครศรีอยุธยา"),
        Province(province_id=34,province_name="พะเยา"),
        Province(province_id=35,province_name="พังงา"),
        Province(province_id=36,province_name="พัทลุง"),
        Province(province_id=37,province_name="พิจิตร"),
        Province(province_id=38,province_name="พิษณุโลก"),
        Province(province_id=39,province_name="เพชรบุรี"),
        Province(province_id=40,province_name="เพชรบูรณ์"),
        Province(province_id=41,province_name="แพร่"),
        Province(province_id=42,province_name="ภูเก็ต"),
        Province(province_id=43,province_name="มหาสารคาม"),
        Province(province_id=44,province_name="มุกดาหาร"),
        Province(province_id=45,province_name="แม่ฮ่องสอน"),
        Province(province_id=46,province_name="ยโสธร"),
        Province(province_id=47,province_name="ยะลา"),
        Province(province_id=48,province_name="ร้อยเอ็ด"),
        Province(province_id=49,province_name="ระนอง"),
        Province(province_id=50,province_name="ระยอง"),
        Province(province_id=51,province_name="ราชบุรี"),
        Province(province_id=52,province_name="ลพบุรี"),
        Province(province_id=53,province_name="ลำปาง"),
        Province(province_id=54,province_name="ลำพูน"),
        Province(province_id=55,province_name="เลย"),
        Province(province_id=56,province_name="ศรีสะเกษ"),
        Province(province_id=57,province_name="สกลนคร"),
        Province(province_id=58,province_name="สงขลา"),
        Province(province_id=59,province_name="สตูล"),
        Province(province_id=60,province_name="สมุทรปราการ"),
        Province(province_id=61,province_name="สมุทรสงคราม"),
        Province(province_id=62,province_name="สมุทรสาคร"),
        Province(province_id=63,province_name="สระแก้ว"),
        Province(province_id=64,province_name="สระบุรี"),
        Province(province_id=65,province_name="สิงห์บุรี"),
        Province(province_id=66,province_name="สุโขทัย"),
        Province(province_id=67,province_name="สุพรรณบุรี"),
        Province(province_id=68,province_name="สุราษฎร์ธานี"),
        Province(province_id=69,province_name="สุรินทร์"),
        Province(province_id=70,province_name="หนองคาย"),
        Province(province_id=71,province_name="หนองบัวลำภู"),
        Province(province_id=72,province_name="อ่างทอง"),
        Province(province_id=73,province_name="อำนาจเจริญ"),
        Province(province_id=74,province_name="อุดรธานี"),
        Province(province_id=75,province_name="อุตรดิตถ์"),
        Province(province_id=76,province_name="อุทัยธานี"),
        Province(province_id=77,province_name="อุบลราชธานี"),

    ]

@app.get("/list_amphoes/{province_id}")
def list_Amphoes(province_id: int) ->list[Amphoes]:
    #SQL select * from cat 
    return [
        Amphoes(province_id=1,amphoes_id=1,amphoes_name="เขตพระนคร"),
        Amphoes(province_id=1,amphoes_id=2,amphoes_name="เขตดุสิต"),
        Amphoes(province_id=1,amphoes_id=3,amphoes_name="เขตหนองจอก"),
        Amphoes(province_id=1,amphoes_id=4,amphoes_name="เขตบางรัก"),
        Amphoes(province_id=1,amphoes_id=5,amphoes_name="เขตบางเขน"),
        Amphoes(province_id=1,amphoes_id=6,amphoes_name="เขตบางกะปิ"),
        Amphoes(province_id=1,amphoes_id=7,amphoes_name="เขตปทุมวัน"),
        Amphoes(province_id=1,amphoes_id=8,amphoes_name="เขตป้อมปราบศัตรูพ่าย"),
        Amphoes(province_id=1,amphoes_id=9,amphoes_name="เขตพระโขนง"),
        Amphoes(province_id=1,amphoes_id=10,amphoes_name="เขตมีนบุรี"),
        Amphoes(province_id=1,amphoes_id=11,amphoes_name="เขตลาดกระบัง"),
        Amphoes(province_id=1,amphoes_id=12,amphoes_name="เขตยานนาวา"),
        Amphoes(province_id=1,amphoes_id=13,amphoes_name="เขตสัมพันธวงศ์"),
        Amphoes(province_id=1,amphoes_id=14,amphoes_name="เขตพญาไท"),
        Amphoes(province_id=1,amphoes_id=15,amphoes_name="เขตธนบุรี"),
        Amphoes(province_id=1,amphoes_id=16,amphoes_name="เขตบางกอกใหญ่"),
        Amphoes(province_id=1,amphoes_id=17,amphoes_name="เขตห้วยขวาง"),
        Amphoes(province_id=1,amphoes_id=18,amphoes_name="เขตคลองสาน"),
        Amphoes(province_id=1,amphoes_id=19,amphoes_name="เขตตลิ่งชัน"),
        Amphoes(province_id=1,amphoes_id=20,amphoes_name="เขตบางกอกน้อย"),
        Amphoes(province_id=1,amphoes_id=21,amphoes_name="เขตบางขุนเทียน"),
        Amphoes(province_id=1,amphoes_id=22,amphoes_name="เขตภาษีเจริญ"),
        Amphoes(province_id=1,amphoes_id=23,amphoes_name="เขตหนองแขม"),
        Amphoes(province_id=1,amphoes_id=24,amphoes_name="เขตราษฎร์บูรณะ"),
        Amphoes(province_id=1,amphoes_id=25,amphoes_name="เขตบางพลัด"),
        Amphoes(province_id=1,amphoes_id=26,amphoes_name="เขตดินแดง"),
        Amphoes(province_id=1,amphoes_id=27,amphoes_name="เขตบึงกุ่ม"),
        Amphoes(province_id=1,amphoes_id=28,amphoes_name="เขตสาทร"),
        Amphoes(province_id=1,amphoes_id=29,amphoes_name="เขตบางซื่อ"),
        Amphoes(province_id=1,amphoes_id=30,amphoes_name="เขตจตุจักร"),
        Amphoes(province_id=1,amphoes_id=31,amphoes_name="เขตบางคอแหลม"),
        Amphoes(province_id=1,amphoes_id=32,amphoes_name="เขตประเวศ"),
        Amphoes(province_id=1,amphoes_id=33,amphoes_name="เขตคลองเตย"),
        Amphoes(province_id=1,amphoes_id=34,amphoes_name="เขตสวนหลวง"),
        Amphoes(province_id=1,amphoes_id=35,amphoes_name="เขตจอมทอง"),
        Amphoes(province_id=1,amphoes_id=36,amphoes_name="เขตดอนเมือง"),
        Amphoes(province_id=1,amphoes_id=37,amphoes_name="เขตราชเทวี"),
        Amphoes(province_id=1,amphoes_id=38,amphoes_name="เขตลาดพร้าว"),
        Amphoes(province_id=1,amphoes_id=39,amphoes_name="เขตวัฒนา"),
        Amphoes(province_id=1,amphoes_id=40,amphoes_name="เขตบางแค"),
        Amphoes(province_id=1,amphoes_id=41,amphoes_name="เขตหลักสี่"),
        Amphoes(province_id=1,amphoes_id=42,amphoes_name="เขตสายไหม"),
        Amphoes(province_id=1,amphoes_id=43,amphoes_name="เขตคันนายาว"),
        Amphoes(province_id=1,amphoes_id=44,amphoes_name="เขตสะพานสูง"),
        Amphoes(province_id=1,amphoes_id=45,amphoes_name="เขตวังทองหลาง"),
        Amphoes(province_id=1,amphoes_id=46,amphoes_name="เขตคลองสามวา"),
        Amphoes(province_id=1,amphoes_id=47,amphoes_name="เขตบางนา"),
        Amphoes(province_id=1,amphoes_id=48,amphoes_name="เขตทวีวัฒนา"),
        Amphoes(province_id=1,amphoes_id=49,amphoes_name="เขตทุ่งครุ"),
        Amphoes(province_id=1,amphoes_id=50,amphoes_name="เขตบางบอน"),

    ]



@app.get("/list_tambons/{amphoes_id}")
def list_Tambons(amphoes_id: int) ->list[Tambons]:
    #SQL select * from cat 
    return [
        Tambons(amphoes_id=1,tambons_id=1,tambons_name="ชนะสงคราม",zipcode="10200"),
        Tambons(amphoes_id=1,tambons_id=2,tambons_name="ตลาดยอด",zipcode="10200"),
        Tambons(amphoes_id=1,tambons_id=3,tambons_name="บวรนิเวศ",zipcode="10200"),
        Tambons(amphoes_id=1,tambons_id=4,tambons_name="บางขุนพรหม",zipcode="10200"),
        Tambons(amphoes_id=1,tambons_id=5,tambons_name="บ้านพานถม",zipcode="10200"),
        Tambons(amphoes_id=1,tambons_id=6,tambons_name="พระบรมมหาราชวัง",zipcode="10200"),
        Tambons(amphoes_id=1,tambons_id=7,tambons_name="วังบูรพาภิรมย์",zipcode="10200"),
        Tambons(amphoes_id=1,tambons_id=8,tambons_name="วัดราชบพิธ",zipcode="10200"),
        Tambons(amphoes_id=1,tambons_id=9,tambons_name="วัดสามพระยา",zipcode="10200"),
        Tambons(amphoes_id=1,tambons_id=10,tambons_name="ศาลเจ้าพ่อเสือ",zipcode="10200"),
        Tambons(amphoes_id=1,tambons_id=11,tambons_name="สำราญราษฎร์",zipcode="10200"),
        Tambons(amphoes_id=1,tambons_id=12,tambons_name="เสาชิงช้า",zipcode="10200"),

    ]
