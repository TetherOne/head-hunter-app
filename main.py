from fastapi import FastAPI
from pydantic import EmailStr

import uvicorn



app = FastAPI()



@app.get('/')
def hello_world():
    return {
        'message': 'hellow world'
    }



if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)