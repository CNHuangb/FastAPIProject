from fastapi import APIRouter
from typing import Union
from pydantic import BaseModel,Field,validator
from datetime import date
from typing import List

from fastapi import Form,File,UploadFile

import os

app05 = APIRouter()

@app05.post("/file")
async def get_file(file:bytes = File()):

    print("file",file)

    return {

        "file":len(file)
    }


@app05.post("/files")
async def get_files(files:List[bytes] = File()):

    # print("file",files)

    for file in files:
        print(len(file))

    return {

        "file":len(files)
    }



@app05.post("/uploadFile")
async def get_file(file:UploadFile):

    print("file",file)

    path = os.path.join("imgs" + file.filename)


    with open(path,"wb") as f:
        for line in file.file:
            f.write(line)

    return {

        "file":file.filename
    }







@app05.post("/uploadFiles")
async def get_uploadFiles(files:List[UploadFile]):

    print("file",files)



    return {

        "names":[file.filename for file in files]
    }

