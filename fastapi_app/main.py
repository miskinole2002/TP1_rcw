import sys,os
from fastapi import FastAPI,Request,Form
from fastapi.staticfiles import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.wsgi import WSGIMiddleware
from fastapi.templating import Jinja2Templates

#  sys permet la creation d'une liste de repertoire
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

app=FastAPI()

templates_dir=os.path.abspath(os.path.join(os.path.dirname(__file__),"templates"))
static_dir=os.path.abspath(os.path.join(os.path.dirname(__file__),"static"))
app.mount("static",StaticFiles(directory=static_dir))
templates=Jinja2Templates(directory=templates_dir)

