from fastapi import FastAPI, HTTPException, Header, Depends
from .routers import profile, auth

app = FastAPI()


app.include_router(
    profile.router,
    prefix='/profile',
    tags=['profile'],
    responses={404: {'message': 'Not Found'}}
)


app.include_router(
    auth.router,
    prefix='/auth',
    tags=['auth'],
    responses={404: {'message': 'Not Found'}}
)
