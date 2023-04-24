from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "fakehashedsecret",
        "disabled": False,
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice Wonderson",
        "email": "alice@example.com",
        "hashed_password": "fakehashedsecret2",
        "disabled": True,
    },
}

app = FastAPI()


def fake_hash_password(password: str):
    return "fakehashed" + password


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None


class UserInDB(User):
    hashed_password: str


def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)


def fake_decode_token(token):
    # This doesn't provide any security at all
    # Check the next version
    user = get_user(fake_users_db, token)
    return user


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)]
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


@app.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": user.username, "token_type": "bearer"}


# @app.get("/users/me")
# async def read_users_me(
#     current_user: Annotated[User, Depends(get_current_active_user)]
# ):
#     return current_user


# class getToken(BaseModel):
#     userName : str
#     password : str
#     apiKey : str
#     token : str
#     status : str

# @app.post("/get_token",tags=["Authen"],)
# def get_token(getToken : getToken) -> getToken :
#     getToken.token = "abcdefghijk"
#     getToken.status =  "success"

#     return getToken

class Groupshare(BaseModel):
    name : str 
    description : str 
    price : float 
    datestart : str
    user_id : str 
    imageURL : str

    class Config:
        schema_extra = {
            "example" : {
             "name": "gxxxx",
             "description": "test test ",
             "price": 1000,
             "datestart": "20230418",
             "user_id": "0001",
             "imageURL": "https://img.freepik.com/free-vector/money-bag_23-2147510861.jpg"
            }
        }

class Register(BaseModel):
    userName : str 
    fullName : str 
    userType : str
    orgName : str
    position : str 
    tel : str
    phone : str
    email : str 
    address : str 
    imagepath : str 
    class Config:
        schema_extra = {
            "example" : {
            "userName" : " วิภาวดี นุชถาวร ",
            "fullName" : "หญิงนุ้ย เทสเตอร์เกาหลี " , 
            "userType" : "ลูกแชร์",
            "orgName" : "ธนาคารอาคารสงเคราะห์" ,
            "position" : "นักพัฒนาระบบ",
            "tel" : "026459000" ,
            "phone" :"0891234567", 
            "email" : " mim@gmail.com",
            "address" : "63 ถนนพระราม 9 เขตห้วยขวาง กรุงเทพมหานคร 10310",
            "imagepath" : " ../image/aaaa.jpg",
            }
        }



class Profile(BaseModel):
    token :str 
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
    result : str 
    message : str 

@app.get("/eKYC_Dopa/{citizen_id}",tags=["Register"],)
def read_item(citizen_id:str):
#def read_item(item_id:int , q: Union[str,None] = None):
    print(" we going to  eKYC_Dopa  ID =" + citizen_id)
    return {"citizenId" : citizen_id , 
            "firstName" : "วิภาวดี",
            "lastName" : "นุชถาวร ",
            "result":"true"}
@app.post("/register",tags=["Register"],)
async def register(register : Register,token: Annotated[str, Depends(oauth2_scheme)])-> Register:
    register_dict = register.dict()
    userId = "00001"
    register_dict.update({"userId": "00001"})
    if not userId:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return register

@app.get("/eKYC_NCB/{citizen_id}",tags=["Register"],)
def read_item(citizen_id:str):
#def read_item(item_id:int , q: Union[str,None] = None):
    print(" we going to  eKYC_NCB  ID =" + citizen_id)
      
    return {"citizenId" : citizen_id , 
            "userName" : " วิภาวดี นุชถาวร ",
            "NCBType" : " GE02 ",
            "NCBScore" : "754",
            "NCBScoreType" : " AA " , 
            "NCBCredit" : "99%" ,
            "checkDate" : "20230425 20:00",
            "result":"true"}



class Signin(BaseModel):
    userName : str 
    password : str
    userId : str 
    signinFlag : str
    result : str 
    message : str 

@app.post("/signin",tags=["Register"],)
def signin(singin : Signin) -> Signin:

    singin_dict = singin.dict()
    singin_dict.update({"userId": "00001"})
    singin_dict.update({"signinFlag": "Y"})
    singin_dict.update({"result":"true"})
    singin_dict.update({"message":"Signin Successful"})
    return singin_dict

@app.post("/signout",tags=["Register"],)
def signout(singin : Signin) -> Signin:

    signout_dict = singin.dict()
    signout_dict.update({"userId": "00001"})
    signout_dict.update({"signinFlag": "N"})
    signout_dict.update({"result":"true"})
    signout_dict.update({"message":"Signout Successful"})
    return signout_dict



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

@app.get("/list_province",tags=["Parameter"],)
def list_province() ->list[Province]:
    #SQL select * from city 
    return [
       
        Province(province_id=1,province_name="กระบี่"),
        Province(province_id=2,province_name="กรุงเทพมหานคร"),
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

@app.get("/list_amphoes/{province_id}",tags=["Parameter"],)
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

@app.get("/list_tambons/{amphoes_id}",tags=["Parameter"],)
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





@app.get("/get_profile/{user_id}",tags=["Profile"],)
def read_item(user_id:str):
#def read_item(item_id:int , q: Union[str,None] = None):
    print(" we going to select * from profile userId =" + user_id)
    return {"userId" : user_id , 
            "userName" : " วิภาวดี นุชถาวร ",
            "fullName" : "หญิงนุ้ย เทสเตอร์เกาหลี " , 
            "userType" : "ลูกแชร์",
            "orgName" : "ธนาคารอาคารสงเคราะห์" ,
            "position" : "นักพัฒนาระบบ",
            "tel" : "026459000" ,
            "phone" :"0891234567", 
            "email" : " mim@gmail.com",
            "address" : "63 ถนนพระราม 9 เขตห้วยขวาง กรุงเทพมหานคร 10310",
            "imagepath" : " ../image/aaaa.jpg",
            "isActive" : "Y",
            "results":"Select Successful"}

@app.post("/edit_profile/",tags=["Profile"],)
def edit_item(profile:Profile) -> Profile:
    #profile_dict = profile.dict()
    profile.result = "บันทึกสำเร็จ"
    print(" we going to update profile Item ID =" + profile.userId + profile.userName)
   
    return profile

@app.put("/lock_profile/{user_id}",tags=["Profile"],)
def lock_item(user_id:str):
    print(" we going to change status profile Item ID =" + user_id)
    return {"userId" : user_id , 
            "IsActive" : "N",
            "results":"Lock User Successful"}

@app.delete("/delete_profile/{user_id}",tags=["Profile"],)
def delete_item(user_id:str):
#def read_item(item_id:int , q: Union[str,None] = None):
    print(" we going to delete profile Item ID =" + user_id)
    return {"results":"Delete Successful"}


class MemberLookShare(BaseModel):
    lookShareName : str
    lookShareSurName : str
    imageLookShare : str

class Bidding(BaseModel):
    shareId : int   
    userId : int 
    # lookShareName : str
    # lookShareSurName : str
    # imageLookShare : str
    # userType : str
    period : int
    interest : int
    result : str 
    message : str 

class WinBidding(BaseModel):
    shareId : int   
    lookShareName : str
    lookShareSurName : str
    imageLookShare : str
    userType : str
    period : int
    interest : int
    isWin : str

    
class PaymentStatus(BaseModel):
    shareId : int   
    lookShareName : str
    lookShareSurName : str
    imageLookShare : str
    userType : str
    period : int
    totalAmount : int
    isWin : str
    status : str

    
class ListShareLookShare(BaseModel):
    shareId : int   
    shareName : str
    availableBalance : int
    minInterest : int
    dateStart : str    
    totalPlayer : int
    imageShare : str
    

class QrPayment(BaseModel):
    shareId : int
    userId : int
    period : int
    account : str
    totalAmount : int
    qrImage : str
    paymentKey : str
    status : str

#app=FastAPI()

@app.get("/list_share_look_share/{user_id}",tags=["LookShare"],)
def list_share_look_share(user_id : int) -> list[ListShareLookShare]:
    
    return[
        ListShareLookShare(shareId=1,shareName="สมพร ดอกเบี้ยสูง",availableBalance=5000,minInterest=1000,dateStart="20230101",totalPlayer=6,imageShare="https://image.com",
                         result="true",message="Select Successful"),
    ]

@app.get("/list_member/{share_id}",tags=["Profile"],)
def list_member(share_id : int) -> list[MemberLookShare]:
    
    return[
        MemberLookShare(lookShareName="สมพร",lookShareSurName="สุขสดใส",imageLookShare="https://image.com" ),
        MemberLookShare(lookShareName="วรวิช",lookShareSurName="อังศุศาสตร์",imageLookShare="https://image.com"),
        MemberLookShare(lookShareName="ภาณุชัย",lookShareSurName="สวัสดิ์เรียวกุล",imageLookShare="https://image.com"),
        MemberLookShare(lookShareName="ณัฎฐา",lookShareSurName="ศิริธนไพศาล",imageLookShare="https://image.com"),
        MemberLookShare(lookShareName="ปิยวรรณ",lookShareSurName="แซ่ลิ่ม",imageLookShare="https://image.com"),
        MemberLookShare(lookShareName="วิภาวดี",lookShareSurName="นุชถาวร",imageLookShare="https://image.com"),
    ]

@app.post("/create_bidding",tags=["LookShare"],)
def create_bidding(request : Bidding) -> Bidding  :
    #request_dict = request.dict()

    # request.lookShareName = "วิภาวดี"
    # request.lookShareSurName="นุชถาวร"
    # request.imageLookShare="https://image.com"
    # request.userType ="ลูกแชร์"
    request.result="true"
    request.message= "Create Successful" 
    return request

@app.get("/list_win_bidding/{share_id}",tags=["LookShare"],)
def list_win_bidding(share_id : int) -> list[WinBidding]:
    
    return[
       WinBidding(shareId=1,lookShareName="สมพร",lookShareSurName="สุขสดใส",imageLookShare="https://image.com",userType="ท้าวแชร์",period=1,interest=1000,isWin="Y"),
       WinBidding(shareId=1,lookShareName="วรวิช",lookShareSurName="อังศุศาสตร์",imageLookShare="https://image.com",userType="ลูกแชร์",period=1,interest=1200,isWin="Y"),
       WinBidding(shareId=1,lookShareName="ภาณุชัย",lookShareSurName="สวัสดิ์เรียวกุล",imageLookShare="https://image.com",userType="ลูกแชร์",period=1,interest=1300,isWin="Y"),
       WinBidding(shareId=1,lookShareName="ณัฎฐา",lookShareSurName="ศิริธนไพศาล",imageLookShare="https://image.com",userType="ลูกแชร์",period=1,interest=1400,isWin="Y"),
       #WinBidding(shareId=1,lookShareName="วิภาวดี",lookShareSurName="แซ่ลิ่ม",imageLookShare="https://image.com",userType="ลูกแชร์",period=1,interest=1600,isWin="Y"),
       #WinBidding(shareId=1,lookShareName="ปิยวรรณ",lookShareSurName="แซ่ลิ่ม",imageLookShare="https://image.com",userType="ลูกแชร์",period=1,interest=1000,isWin="Y"),
    ]

@app.post("/payment_status",tags=["LookShare"],)
def payment_status(request : PaymentStatus) -> list[PaymentStatus] :
 
    return[
       PaymentStatus(shareId=1,lookShareName="สมพร",lookShareSurName="สุขสดใส",imageLookShare="https://image.com",userType="ท้าวแชร์",period=1,totalAmount=6000,isWin="N",status="Y"),
       PaymentStatus(shareId=1,lookShareName="วรวิช",lookShareSurName="อังศุศาสตร์",imageLookShare="https://image.com",userType="ลูกแชร์",period=1,totalAmount=6200,isWin="N",status="Y"),
       PaymentStatus(shareId=1,lookShareName="ภาณุชัย",lookShareSurName="สวัสดิ์เรียวกุล",imageLookShare="https://image.com",userType="ลูกแชร์",period=1,totalAmount=6300,isWin="N",status="Y"),
       PaymentStatus(shareId=1,lookShareName="ณัฎฐา",lookShareSurName="ศิริธนไพศาล",imageLookShare="https://image.com",userType="ลูกแชร์",period=1,totalAmount=6400,isWin="N",status="N"),
       PaymentStatus(shareId=1,lookShareName="วิภาวดี",lookShareSurName="แซ่ลิ่ม",imageLookShare="https://image.com",userType="ลูกแชร์",period=1,totalAmount=0,isWin="Y",status="N"),
       PaymentStatus(shareId=1,lookShareName="ปิยวรรณ",lookShareSurName="แซ่ลิ่ม",imageLookShare="https://image.com",userType="ลูกแชร์",period=1,totalAmount=5000,isWin="N",status="N")
    ]

@app.post("/create_payment",tags=["LookShare"],)
def create_payment(QrPayment : QrPayment) -> QrPayment :
    
    QrPayment.shareId=1
    QrPayment.userId=1
    QrPayment.account="1234567890"
    QrPayment.totalAmount=6200
    QrPayment.qrImage = "https://image.com"
    QrPayment.paymentKey="1111111111"
    QrPayment.status="pending"

    return QrPayment




@app.post("/payment_success",tags=["LookShare"],)
def payment_success(QrPayment : QrPayment) -> QrPayment :
    QrPayment.shareId=1
    QrPayment.userId=1
    QrPayment.account="1234567890"
    QrPayment.totalAmount=6200
    QrPayment.qrImage = "https://image.com"
    QrPayment.paymentKey="1111111111"
    QrPayment.status="success"

    return QrPayment


class Group_share(BaseModel):
    group_share_name : str
    available_balance : int
    min_interest : int
    date : str
    total_player : int
    
class Group_share_id(BaseModel):
    group_share_id : str
    group_share_name : str
    monthly_interest : int
    min_interest : int
    total_player : int
    bidding_date : str
    due_date : str
    starting_date :str
    result : str

    class Config:
        schema_extra = {
            "example" : {
            "group_share_id": "00010",
            "group_share_name": "สมพร ดอกเบี้ยสูงมากเลย",
            "monthly_interest": 100000,
            "min_interest": 10000,
            "total_player": 5,
            "bidding_date": "1",
            "due_date": "5",
            "starting_date": "2023-04-04",
            "result": "",
            }
        }


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

class MemberLookShare(BaseModel):
    lookShareName : str
    lookShareSurName : str
    imageLookShare : str

class LookShareBidding(BaseModel):
    lookShareName : str
    lookShareSurName : str
    imageLookShare : str
    role : str
    period : int
    interest : int
    isWin : str


@app.post("/create_group_share",tags=["ThaoShare"])
def create_croup_share_id(Group_share_id:Group_share_id):
    print("insert into Group_share_id value()")
    print("create Group_share_id{0} for {1}" .format(Group_share_id.group_share_name,Group_share_id.monthly_interest,Group_share_id.min_interest,Group_share_id.total_player,
                                                     Group_share_id.bidding_date,Group_share_id.due_date,Group_share_id.starting_date))
    Group_share_id_dict = Group_share_id.dict()
    Group_share_id_dict.update({"Groupshareid":"0000011"})
    Group_share_id_dict.update({"results":"Successful"})
    #return Group_share_id.dict
    return Group_share_id_dict

@app.get("/list_group_share",tags=["ThaoShare"])
def list_group_share() ->list[Group_share]:
    return [
        Group_share(group_share_name="สมพร ดอกเบี้ยสูงมาก",available_balance=100000,min_interest=10000,date="2023-04-04",total_player=0/5),
        Group_share(group_share_name="สมพร ดอกเบี้ยสูง",available_balance=5000,min_interest=1000,date="2023-01-01",total_player=4/5),
        Group_share(group_share_name="สมพร ดอกเบี้ยดี",available_balance=100000,min_interest=10000,date="2023-04-04",total_player=0/5),
        Group_share(group_share_name="สมพร วงเงินน้อย",available_balance=5000,min_interest=1000,date="2023-01-01",total_player=4/5)
    ]

@app.post("/edit_group_share",tags=["ThaoShare"])
def edit_group_share_item(group_share: Group_share_id)-> Group_share_id:
    group_share_dict = group_share.dict()
    # Group_share_id.group_share_id = "000010"
    # Group_share_id.group_share_name = "สมพร ดอกเบี้ยสูงมากเลย"
    # Group_share_id.monthly_interest = 100000
    # Group_share_id.min_interest = 10000
    # Group_share_id.total_player = 5
    # Group_share_id.bidding_date = "1"
    # Group_share_id.due_date = "5"
    # Group_share_id.starting_date = "2023-04-04"
    # Group_share_id.result = "แก้ไขสำเร็จ"

    group_share_dict.update({"result":"แก้ไขสำเร็จ"})
    return group_share_dict

@app.put("/lock_group_share/{group_share_id}",tags=["ThaoShare"])
def lock_group_share_item(group_share_id:str):
    print(" we going to change status profile Item ID =" + group_share_id)
   
    return {"group_share_id" : group_share_id , 
            "IsActive" : "N",
            "result":"Lock Group Share Successful"}

@app.put("/unlock_group_share/{group_share_id}",tags=["ThaoShare"])
def unlock_group_share_item(group_share_id:str):
    print(" we going to change status profile Item ID =" + group_share_id)
   
    return {"group_share_id" : group_share_id , 
            "IsActive" : "Y",
            "result":"Unlock Group Share Successful"}

@app.delete("/delete_group_share/{group_share_id}",tags=["ThaoShare"])
def delete_group_share_item(group_share_id:str):
    print(" we going to delete profile Item ID =" + group_share_id)
    return {"group_share_id" : group_share_id , 
            "result":"Delete Group Share Successful"}
   