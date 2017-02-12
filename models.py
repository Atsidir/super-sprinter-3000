from peewee import *

db = PostgresqlDatabase('atsidir', user='atsidir')


class BaseModel(Model):
    class Meta:
        database = db

class UserStory(BaseModel):
    title=CharField(unique=True,max_length=100)
    story=CharField(max_length=500)
    acceptance=CharField(max_length=500)
    bvalue=IntegerField()
    hours=FloatField()
    status=CharField()

class Status(BaseModel):
    status=CharField()