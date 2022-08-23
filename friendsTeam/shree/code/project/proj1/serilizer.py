


from .models import order,customer,address
from rest_framework import serializers


class addressserilizer(serializers.ModelSerializer):
    class Meta:
        model = address
        fields = ('id','city','state','pincode')

class customerserilizer(serializers.ModelSerializer):
    class Meta:
        model = customer
        fields = ('id','name','address')

class orderserilizer(serializers.ModelSerializer):
    class Meta:
        model = order
        fields = ('id','product_name','prod_qty','prod_price','customer')