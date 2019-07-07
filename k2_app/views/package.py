from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from k2_app.models.package import Package
from k2_app.serializers.package import PackageSerializer

class PackageList(APIView):
    
    def get(self, request, format=None):
        data = Package.objects.all()
        serializer = PackageSerializer(data, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = PackageSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     
        
class PackageDetail(APIView):
    def _get_object(self, name):
        try:
            return Package.objects.get(name=name)
        except Package.DoesNotExist:
            raise Http404
        
    def get(self, request, name, format=None):
        data = self._get_object(name)
        serializer = PackageSerializer(data)
        return Response(serializer.data)
    
    def put(self, request, name, format=None):
        data = self._get_object(name)
        serializer = PackageSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, name, format=None):
        data = self._get_object(name)
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)