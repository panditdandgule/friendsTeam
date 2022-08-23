from django.shortcuts import render
from .models import order,customer,address
from .serilizer import orderserilizer,customerserilizer,addressserilizer
from rest_framework import viewsets
# Create your views here.


class addressview(viewsets.ModelViewSet):
    queryset = address.objects.all()
    serializer_class = addressserilizer

class customerview(viewsets.ModelViewSet):
    queryset = customer.objects.all()
    serializer_class = customerserilizer

class orderview(viewsets.ModelViewSet):
    queryset = order.objects.all()
    serializer_class = orderserilizer

