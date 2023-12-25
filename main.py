from fastapi import FastAPI, Path, Query,Form,File,UploadFile,HTTPException
from enum import Enum
from typing import Union
from pydantic import BaseModel


class schema1(BaseModel):
    name:str
    Class:str
    roll_no:int

app= FastAPI()

@app.get("/hello")
async def root():
    return {"message":"MY Name is Udrasht"}


@app.get("/Bye")
async def root():
    return {"message":"hello hello"}


# path parameter
@app.get("/item/{item}")
async def path_func(item):
    var_name= {"path_variable":item}
    return var_name




# Query parameter
# ex: http://127.0.0.1:8000/Query/?name=udrasht&roll_no=1234

# @app.get("/Query/")
# async def Query_func(name: str, roll_no: int):
#     var_name= {"Name":name, "Roll No": roll_no}
#     return var_name


#  default value

@app.get("/Query/")
async def Query_func(name: str, roll_no: Union[str, None]=Query(None, min_length=3, max_length=5)):   #Querry is use for validation
    var_name= {"Name":name, "Roll No": roll_no}
    return var_name





# Request Body
@app.post("/items/")
async def creat_item(item:schema1):
    return item

class vipan(BaseModel):
    one: str
    two:str
    three:int

# how we send the form data
@app.post("/form/data")
async def from_data(username: str=Form(),password: str=Form()):
    return {"username": username, "password": password}

@app.post("/form/vipan")
async def vipan(item:vipan):
    # print(item)
    item.three+=10
    return {"items":item}



# video 4
#upload file with the help of FastAPI

@app.post("/form/upload")
async def uploded_file_size(file:bytes=File()):
    # print(file)
    return {"file size": len(file)}    # return the size of file in Bytes


@app.post("/file/info")
async def uploded_file_info(file:UploadFile):
    # print(file)
    return {"File Info": file}   # it wil return the information of file



# fastAPI error handling
items=["1","2","3","4","5"]
@app.get("/error/hadling")
async def handle_error(item: str):
    if item not in items:
        return HTTPException(status_code=400, detail="item is not equal to 2 try another value!!")
    return {"value": item}

