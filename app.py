
from flask import Flask
from extension import db,ma
from config import *
from route.AddProductRoute import routeAddProduct
from route.AddUserRoute import addUserRoute
from route.DefaultRoute import defaultRoute
from route.GetListProductRoute import routeListProduct
from route.GetProductByIdRoute import getProductByIDRoute
from route.UpdateProductRoute import updateProductRoute
from route.GetListUserRoute import getListUserRoute

#init app
app = Flask(__name__)
#set app config
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
#init db and ma
db.init_app(app)
ma.init_app(app)
with app.app_context():
    #db.drop_all()
    db.create_all()
#set route
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

