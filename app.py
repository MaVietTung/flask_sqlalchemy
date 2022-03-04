
from flask import Flask

#init app
app = Flask(__name__)
#database config
from config import *
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
#init db 
from extension import db
from model.ProductModel import *
from model.UserModel import *
db.init_app(app)
with app.app_context():
    #db.drop_all()
    db.create_all()

#init ma
from extension import ma
from schema.ProductSchema import *
from schema.UserSchema import *
ma.init_app(app)


#set route
from route.AddProductRoute import routeAddProduct
from route.AddUserRoute import addUserRoute
from route.DefaultRoute import defaultRoute
from route.GetListProductRoute import routeListProduct
from route.GetProductByIdRoute import getProductByIDRoute
from route.UpdateProductRoute import updateProductRoute
from route.GetListUserRoute import getListUserRoute
app.register_blueprint(routeAddProduct)
app.register_blueprint(addUserRoute)
app.register_blueprint(defaultRoute)
app.register_blueprint(routeListProduct)
app.register_blueprint(getProductByIDRoute)
app.register_blueprint(updateProductRoute)
app.register_blueprint(getListUserRoute)




#run server
if __name__ == '__main__':
    app.run(debug = True)

