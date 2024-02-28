from django.shortcuts import render
from rest_framework import generics

from referalapp.models import Refer
from referalapp.serializers import ReferSerializer


# Create your views here.
class ReferAPIView(generics.ListAPIView):
    queryset = Refer.objects.all()
    serializer_class = ReferSerializer