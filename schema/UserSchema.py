from extension import ma

#User Scheama
class UserSchema(ma.Schema):
    class Meta:
        fields= ('id','name')

user_schema = UserSchema()
users_schema = UserSchema(many=True)