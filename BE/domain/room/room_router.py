from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer

from domain.room.room_schema import RoomRegister
from util import get_current_user_id
import domain.room.room_crud as room_crud
from db import get_db_connection

router = APIRouter(prefix = '/rooms')

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.post("") # POST /rooms
def register_room(room_register : RoomRegister, user_id: str = Depends(get_current_user_id), conn=Depends(get_db_connection)):
    return room_crud.register_room(user_id, room_register, conn)

@router.get("/list")  # GET /rooms/list
def get_my_rooms(user_id: str = Depends(get_current_user_id), conn=Depends(get_db_connection)):
    return room_crud.get_my_rooms(user_id, conn)