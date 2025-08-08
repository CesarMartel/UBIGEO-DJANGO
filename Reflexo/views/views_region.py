from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Reflexo.models import Region

class RegionView(APIView):
    def get(self, request):
        regions = Region.objects.values('id', 'name')
        return Response(list(regions), status=status.HTTP_200_OK)

    def post(self, request):
        return Response({"message": "POST región"}, status=status.HTTP_201_CREATED)