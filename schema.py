from flask_marshmallow import Marshmallow
#init ma
ma = Marshmallow()
#Product Schema
class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id','name','price','owner_id')
#User Scheama
class UserSchema(ma.Schema):
    class Meta:
        fields= ('id','name')
#init schema
product_schema  = ProductSchema()
products_schema = ProductSchema(many=True)
user_schema = UserSchema()
users_schema = UserSchema(many=True)