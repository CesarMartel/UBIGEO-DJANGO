from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class RegionView(APIView):
    def get(self, request):
        return Response({"message": "GET regiones"}, status=status.HTTP_200_OK)

    def post(self, request):
        return Response({"message": "POST región"}, status=status.HTTP_201_CREATED)