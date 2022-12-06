from peewee import *

db = SqliteDatabase('drivers_monako.db')

class Drivers(Model):
    id = IntegerField()
    name = CharField()
    time = CharField()
    
    class Meta:
        database = db
        order_by = 'id'