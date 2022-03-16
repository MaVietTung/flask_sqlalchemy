from extension import ma
 
#User Scheama for converting user instance to dict data type
class UserSchema(ma.Schema):
    class Meta:
        fields= ('id','name','address','mobile','email','age')

user_schema = UserSchema()
users_schema = UserSchema(many=True)