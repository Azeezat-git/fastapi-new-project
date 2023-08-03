from .. import models,schemas, utils
from fastapi import FastAPI, Depends, Response, status, HTTPException, APIRouter
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from .. import oauth2

router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)

@router.get("/", response_model=List[schemas.Post])
def get_posts(db: Session = Depends(get_db)):
    #cursor.execute("""SELECT * FROM posts;""")
    #posts = cursor.fetchall()
    posts = db.query(models.Post).all()
    return posts


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db)):
    #cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING * """,(post.title, post.content, post.published))
    #new_post = cursor.fetchone()
    #conn.commit()
    #new_post = models.Post(title=post.title, content=post.content, published=post.published)
    new_post = models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return  new_post

@router.get("/{id}", response_model=schemas.Post)
def get_post(id: int, db: Session = Depends(get_db)):
   posts = db.query(models.Post).filter(models.Post.id == id).first()
   print(posts)
   if not posts:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
   else:
       return posts
       


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db)):
    #cursor.execute("""DELETE FROM posts WHERE id = %s returning *""",(str(id)))
    #deleted_post = cursor.fetchone()
    #conn.commit()
    deleted_post = db.query(models.Post).filter(models.Post.id == id)
    if deleted_post.first() == None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"post with id: {id} was not found")
    deleted_post.delete(synchronize_session=False)
    db.commit()
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def update_post(id: int, updated_post: schemas.PostCreate, db: Session = Depends(get_db)):
    #cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s returning * """, (post.title, post.content, post.published, (str(id))) )
    #updated_post = cursor.fetchone()
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
    
    
    post_query.update(updated_post.dict(), synchronize_session=False)
    db.commit()
    return  post_query.first()