import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'user' 
    id = Column(Integer, primary_key=True)
    username = Column(String(250), unique = True)
    firstname = Column(String(250))
    lastname = Column(String(250))
    email = Column(String(250), nullable = False)

class Follower(Base):
    __tablename__ = 'follower' 
    user_form_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    user_to_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    user = relationship(User)

class Post(Base):
    __tablename__ = 'post' 
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Media(Base):
    __tablename__ = 'media' 
    id = Column(Integer, primary_key=True)
    type = Column(Enum('image', 'video', 'audio', name='media_types'), nullable=False)
    url = Column(String(250))
    post_id = Column(Integer, ForeignKey('post.id'))
    user = relationship(Post)

class Comment(Base):
    __tablename__ = 'comment' 
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250))
    url = Column(String(250))
    author_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
