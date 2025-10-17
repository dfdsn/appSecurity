from typing import Annotated, Dict

from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field, constr

app = FastAPI(title="AppSecurity - Cadastro")

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

CPF = constr(pattern=r"^\d{11}$", strip_whitespace=True)


class RegistrationData(BaseModel):
    full_name: str = Field(..., title="Nome Completo", min_length=3)
    cpf: CPF = Field(..., title="CPF", description="Informe apenas os números")
    street: str = Field(..., title="Logradouro")
    number: str = Field(..., title="Número")
    complement: str = Field("", title="Complemento")
    district: str = Field(..., title="Bairro")
    city: str = Field(..., title="Cidade")
    state: str = Field(..., title="Estado")
    postal_code: constr(pattern=r"^\d{5}-?\d{3}$", strip_whitespace=True) = Field(..., title="CEP")


@app.get("/", response_class=HTMLResponse)
async def show_registration_form(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(
        "register.html",
        {
            "request": request,
            "submitted": False,
            "form_data": None,
        },
    )


@app.post("/", response_class=HTMLResponse)
async def submit_registration_form(
    request: Request,
    full_name: Annotated[str, Form(...)],
    cpf: Annotated[str, Form(...)],
    street: Annotated[str, Form(...)],
    number: Annotated[str, Form(...)],
    complement: Annotated[str, Form("")],
    district: Annotated[str, Form(...)],
    city: Annotated[str, Form(...)],
    state: Annotated[str, Form(...)],
    postal_code: Annotated[str, Form(...)],
) -> HTMLResponse:
    data = RegistrationData(
        full_name=full_name,
        cpf=cpf,
        street=street,
        number=number,
        complement=complement,
        district=district,
        city=city,
        state=state,
        postal_code=postal_code,
    )

    masked_data: Dict[str, str] = data.model_dump()
    masked_data["cpf"] = f"{data.cpf[:3]}.{data.cpf[3:6]}.{data.cpf[6:9]}-{data.cpf[9:]}"

    return templates.TemplateResponse(
        "register.html",
        {
            "request": request,
            "submitted": True,
            "form_data": masked_data,
        },
    )


__all__ = ["app"]
