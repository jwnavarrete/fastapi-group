from fastapi import Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List, Optional
from sqlalchemy import func
from .. import oauth2
from ..schemas.post import PostResponse, PostCreate, PostUpdate, PostVoteResponse
from ..models.Post import PostModel
from ..models.Vote import VoteModel
from ..database import get_db

router = APIRouter(
    prefix="/posts",
    tags=['Posts']
)

@router.get("/", response_model=List[PostVoteResponse])
def get_posts(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user), limit: int = 10, offset: int = 0, search : Optional[str] = ""):
    posts = db.query(PostModel, func.count(VoteModel.post_id).label("votes")).join(
        VoteModel, VoteModel.post_id == PostModel.id, isouter=True).group_by(PostModel.id).filter(PostModel.title.contains(search)).limit(limit).offset(offset).all()
    return posts


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=PostResponse)
def create_posts(post: PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    new_post = PostModel(owner_id=current_user.id, **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post


@router.get("/{id}", response_model=PostVoteResponse)
def get_post(id: int, db: Session = Depends(get_db), user_id: int = Depends(oauth2.get_current_user)):
    post = db.query(PostModel, func.count(VoteModel.post_id).label("votes")).join(
        VoteModel, VoteModel.post_id == PostModel.id, isouter=True).group_by(PostModel.id).filter(PostModel.id == id).first()


    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} was not found")

    return post


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    post_query = db.query(PostModel).filter(PostModel.id == id)

    post = post_query.first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")

    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")
    post_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.patch("/{id}", response_model=PostResponse)
def update_post(id: int, updated_post: PostUpdate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    post_query = db.query(PostModel).filter(PostModel.id == id)

    post = post_query.first()


    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")

    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action")
    
    update_data = updated_post.dict(exclude_unset=True)
    post_query.update(update_data, synchronize_session=False)

    db.commit()

    return post_query.first()