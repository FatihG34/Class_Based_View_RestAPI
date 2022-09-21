from django.shortcuts import render, HttpResponse, get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

from cbv.serializers import PeopleSerializer
from .models import People
# Create your views here.

def home(request):
    return HttpResponse("<h1>API Page</h1>")

class PeopleGetPost(ModelViewSet):
    queryset=People.objects.all()
    serializer_class = PeopleSerializer

    @action(detail=False,methods=["GET"])
    def people_count(self, request):
        count = {
            "peopleCount":self.queryset.count()
        }
        return Response(count)