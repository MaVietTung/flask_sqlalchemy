from extension import ma
 
#User Scheama for converting user instance to dict data type
class UserSchema(ma.Schema):
    class Meta:
        fields= ('id','name')

user_schema = UserSchema()
users_schema = UserSchema(many=True)