from fastapi import FastAPI, HTTPException, Header, Depends
from . routers import profile


app = FastAPI()

async def get_token_header(x_token: str = Header(...)):
    print(x_token)
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return PlainTextResponse(str({'message': 'token is not valid'}), status_code=400)


app.include_router(
    profile.router,
    prefix='/profile',
    tags=['profile'],
    dependencies=[Depends(get_token_header)],
    responses={404: {'message': 'Not Found'}}
)