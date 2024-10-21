import sys,os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from fastapi import FastAPI,Request,Form
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.wsgi import WSGIMiddleware
from fastapi.templating import Jinja2Templates
import uvicorn
from dash_app import app as app_dash
#  sys permet la creation d'une liste de repertoire

app=FastAPI()

templates_dir=os.path.abspath(os.path.join(os.path.dirname(__file__),"templates"))
static_dir=os.path.abspath(os.path.join(os.path.dirname(__file__),"static"))
# app.mount("static",StaticFiles(directory=static_dir))
templates=Jinja2Templates(directory=templates_dir)
users={"admin":"1234"}

@app.get("/")
async def home(request:Request):
    return templates.TemplateResponse("home.html",{"request":request},status_code=200)

@app.get("/login")
async def login(request:Request):
    return templates.TemplateResponse("login.html",{"request":request},status_code=200)

@app.post("/login")
async def login(username:str=Form(...),password:str=Form(...)):
    print(username,password)
    if username in users and users[username]==password:
        response= RedirectResponse(url='/dashboard',status_code=302)
        response.set_cookie(key="Authorisation",value="Bearer Token", httponly=True)
    else:
        response=templates.TemplateResponse("home.html",{"request":request,"error":"Invalid"},status_code=200)
    return response

@app.get("/logout")
async def logout():
    response=RedirectResponse(url='./login')
    response.delete_cookie('Authorization')
    return response 
    

app.mount("/dashboard",WSGIMiddleware(app_dash.server))
if __name__=="__main__":
    uvicorn.run(app,host='0.0.0.0',port=8001 ,workers=1 )