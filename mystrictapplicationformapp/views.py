from .serializers import ReferenceSerializer
from mystrictapplicationformapp.models import Reference
from rest_framework import viewsets, mixins


# Create your views here.
class ReferenceViewSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = Reference.objects.all().order_by("-id")

    def get_serializer_class(self):
        return ReferenceSerializer

