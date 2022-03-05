
from flask import Flask
from extension import db,ma
from config import *
from routes.AddProductRoute import routeAddProduct
from routes.AddUserRoute import addUserRoute
from routes.DefaultRoute import defaultRoute
from routes.GetListProductRoute import routeListProduct
from routes.GetProductByIdRoute import getProductByIDRoute
from routes.UpdateProductRoute import updateProductRoute
from routes.GetListUserRoute import getListUserRoute
from routes.DeleteProductRoute import deleteProductRoute

#init app
app = Flask(__name__)
#set app config
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
#init db and ma
db.init_app(app)
ma.init_app(app)
#run create table if they are not exits first time when running app
with app.app_context():
    #db.drop_all()
    db.create_all()
#register route from Bluprint instance we set in routes package
app.register_blueprint(routeAddProduct)
app.register_blueprint(addUserRoute)
app.register_blueprint(defaultRoute)
app.register_blueprint(routeListProduct)
app.register_blueprint(getProductByIDRoute)
app.register_blueprint(updateProductRoute)
app.register_blueprint(getListUserRoute)
app.register_blueprint(deleteProductRoute)
#run server
if __name__ == '__main__':
    app.run(debug = True)

