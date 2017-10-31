from rest_framework import status, generics, mixins
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from beacon.models import Time
from beacon.serializers import TimeSerializer

class SignalList(generics.ListCreateAPIView):
    # 유저 관리 View

    serializer_class = TimeSerializer
    queryset = Time.objects.all()

signal_list = SignalList.as_view()
