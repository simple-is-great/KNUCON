from fastapi import APIRouter, Depends, Query

from util import get_current_user_id
from domain.post.post_schema import PostInput, PostSearchParams
import domain.post.post_crud as post_crud
from db import get_db_connection

router = APIRouter(
    prefix = '/posts'
)

@router.post("/search")
def search_post(search_params: PostSearchParams,conn=Depends(get_db_connection)):
    search_dict = search_params.model_dump()
    return post_crud.list_post(conn, search_dict, search_params.page, search_params.page_size)

# add user_id for validation
@router.post("") # POST /posts: create new post
def create_post(create_post: PostInput, user_id: str = Depends(get_current_user_id),  conn=Depends(get_db_connection)):
    return post_crud.create_post(create_post, user_id, conn)

@router.get("/{post_id}")
def get_post(post_id: str, user_id: str = Depends(get_current_user_id), conn=Depends(get_db_connection)): # GET /posts/:post_id: GET single post
    return post_crud.get_post(post_id, conn)

@router.delete("/{post_id}") # DELETE /posts/:post_id : delete single post
def delete_post(post_id: str, user_id: str = Depends(get_current_user_id), conn=Depends(get_db_connection)):
    return post_crud.delete_post(post_id, conn)