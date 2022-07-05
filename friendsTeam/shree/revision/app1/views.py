from django.shortcuts import render

# Create your views here.
from app1.models import order,customer
from rest_framework.viewsets import ModelViewSet
from app1.serializer import ordercustomer,customer_


class order_operation(ModelViewSet):
    queryset = order.objects.all()
    seriliazer_class = ordercustomer

class customer_operation(ModelViewSet):
    query = customer.objects.all()
    srriliazer_class = customer_


