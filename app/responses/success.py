from fastapi.responses import JSONResponse

def response(data, msg:str = 'Success', internal_code:int = 1, status_code:int = 200):
    return JSONResponse({
        'status': {
            'msg': msg,
            'rc': internal_code
        },
        'data': data
    }, status_code= status_code)