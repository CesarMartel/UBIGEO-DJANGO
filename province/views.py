# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Province
from .serializers import ProvinceSerializer

class ProvinceListView(APIView):
    def get(self, request, *args, **kwargs):
        provinces = Province.objects.all()
        serializer = ProvinceSerializer(provinces, many=True)
        return Response(serializer.data)
