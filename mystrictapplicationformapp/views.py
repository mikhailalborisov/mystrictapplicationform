from django.shortcuts import render

from .serializers import ReferenceSerializer
from mystrictapplicationformapp.models import Reference
from rest_framework import viewsets, mixins


# Create your views here.
class ReferenceViewSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    queryset = Reference.objects.all().order_by("-id")

    def get_serializer_class(self):
        # if self.action == "list":
        #     return NonModelSerializer
        return ReferenceSerializer
        # return NonModelSerializer
        # return super().get_serializer_class()
    # serializer_class = UserSerializer
