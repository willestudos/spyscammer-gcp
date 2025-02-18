import os
from loguru import logger

from fastapi import APIRouter, Depends
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, JSONResponse
from app.schemas.member_schema import MemberSchema, LoginForm
from app.service.service_members import ServiceMember

router = APIRouter(prefix='')

templates_dir = os.path.join(os.path.dirname(__file__), '..', 'templates')
templates = Jinja2Templates(directory=templates_dir)

logger.remove()
logger.add(sink=lambda msg: print(msg, end=""), format="{time:YYYY-MM-DD HH:mm:ss} {level} {message}")


@router.get('/')
async def index(request: Request):
    context = {
        "request": request
    }
    return templates.TemplateResponse('/member/index.html', context=context)


@router.get('/login')
async def login(request: Request):
    context = {
        "request": request
    }
    return templates.TemplateResponse('/member/login.html', context=context)


@router.post('/login', response_class=HTMLResponse)
async def login(
        request: Request,
        service: ServiceMember = Depends(ServiceMember)):
    context = {
        "request": request
    }
    form = await request.form()
    email = form.get('email'),
    password = form.get('password')
    response = service.get_auth_member(email, password)
    if response is not None:
        logger.info(f'| logado com -- {response["name"]} - {response["email"]}')
        context['username'] = response['name']
        context['email'] = response['email']
        return templates.TemplateResponse('/member-admin/user.html', context=context)
    logger.error(f"| falha ao logar com -- {form.get('email')} - {form.get('password')}")
    context['alert_message'] = "Email ou senha incorretos. Tente novamente."
    return templates.TemplateResponse('/member/login.html', context=context)


@router.get('/register')
async def register(request: Request):
    context = {
        "request": request
    }

    return templates.TemplateResponse('/member/register.html', context=context)


@router.post('/register', response_class=HTMLResponse)
async def create_register(
        request: Request,
        service: ServiceMember = Depends(ServiceMember)
):
    form = await request.form()
    try:
        payload = MemberSchema(
            name=form.get('name'),
            username=form.get('username').lower(),
            email=form.get('email'),
            password=form.get('password')
        ).dict()
        logger.info(f"| Payload cadastro -- name: {form.get('name')}, username: {form.get('username')}, email: {form.get('email')}")
    except ValueError as e:
        return JSONResponse(
            status_code=400,
            content={"deatil": str(e)}
        )

    response = service.create_member(data=payload)
    context = {
        "request": request,
        "alert_message": response
    }
    return templates.TemplateResponse('/member/register.html', context=context)


@router.get('/forgot_password')
async def forgot_password(request: Request):
    context = {
        "request": request
    }
    return templates.TemplateResponse('/member/forgot_password.html', context=context)
