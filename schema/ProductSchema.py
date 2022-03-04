from extension import ma

#Product Schema
class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id','name','price','owner_id')

product_schema  = ProductSchema()
products_schema = ProductSchema(many=True)