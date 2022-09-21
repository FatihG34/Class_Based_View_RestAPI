from django.urls import path,include
from .views import PeopleGetPost, home
from rest_framework import routers


router = routers.DefaultRouter()
router.register("people/", PeopleGetPost)

urlpatterns = [
    path("", home),
    path("", include(router.urls))
]