from extension import ma

class OrderSchema(ma.Schema):
    class Meta:
        fields = ('description','address','mobile','typeorder','date','price','state','owner_id')

order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)