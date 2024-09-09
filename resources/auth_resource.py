from typing import Annotated
from fastapi import APIRouter, Header


auth_resource = APIRouter(prefix="/todo-api/auth")




@auth_resource.post("")
async def auth(x_authorization: str = Header(default=None, convert_underscores=False)):
    print(x_authorization)
    return {"authorization":  x_authorization}
