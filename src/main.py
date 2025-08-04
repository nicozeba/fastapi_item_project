from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from src.routes.item_routes import router

app = FastAPI()

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    msgs = [ f"Validation Error: {dict_err['type']} {dict_err['loc'][1]} attribute." for dict_err in exc.errors() ]
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content= {"detail": msgs}
    )

app.include_router(router)