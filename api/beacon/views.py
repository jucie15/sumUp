from django.shortcuts import get_object_or_404
from rest_framework import status, generics, mixins
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from numpy import matrix, matmul
from numpy.linalg import pinv
from beacon.models import Time, Beacon
from beacon.serializers import TimeSerializer

class SignalList(generics.ListCreateAPIView):
    # 유저 관리 View

    serializer_class = TimeSerializer
    queryset = Time.objects.all()
    filter_fields = ('created_at', 'user')

    def location_calculate(self, signals):
        mat_a_col = []
        mat_b_col = []

        for signal in signals:
            uuid = signal['uuid']
            rssi = signal['rssi']
            beacon = get_object_or_404(Beacon, uuid=uuid)
            x, y, z = beacon.x, beacon.y, beacon.z
            mat_a_col.append([1, -2*x, -2*y, -2*z])
            mat_b_col.append([pow(10, (-60-rssi)/60)-x**2-y**2-z**2])

        mat_a = matrix(mat_a_col)
        mat_b = matrix(mat_b_col)
        mat_x = matmul(pinv(mat_a), mat_b)

        return mat_x

    def create(self, request, *args, **kwargs):
        # 해당 요청 유저 정보 보기(GET)
        data = request.data
        serializer = TimeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            res_data = {'user': data['user'], 'location': self.location_calculate(data['signals'])}
            return Response(data=res_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

signal_list = SignalList.as_view()
