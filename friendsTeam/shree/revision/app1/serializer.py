
from app1.models import order,customer
from rest_framework.serializers import ModelSerializer

class ordercustomer(ModelSerializer):
    class Meta:
        Model = order
        fields = "__all__"

class customer_(ModelSerializer):
    class Meta:
        Model = customer
        fields = "__all__"





















