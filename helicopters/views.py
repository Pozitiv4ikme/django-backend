from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from helicopters.models import Helicopter
from helicopters.serializers import HelicopterSerializers, HelicopterSerializersPUT


class HelicoptersListCreateAPIView(APIView):
    def get(self, request):
        helicopters = Helicopter.objects.all()
        serializer = HelicopterSerializers(helicopters, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        serializer = HelicopterSerializers(data=data)
        serializer.is_valid(raise_exception=True)    # chekc valid your data
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class HelicopterRetrieveUpdateDeleteAPIView(APIView):
    # def get(self, request, pk):
    #     helicopter = Helicopter.objects.get(id=pk)
    #     serializer = HelicopterSerializers(helicopter)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        helicopter = Helicopter.objects.get(id=pk)      # 1 - find element by id
        data = request.data                             # 2 - get data from request
        serializer = HelicopterSerializersPUT(helicopter, data=data)   # 3 - serialize ( 1 args -
        serializer.is_valid(raise_exception=True)              # 4 - check serializer
        serializer.save()                                           # 5 - save data to db
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        helicopter = Helicopter.objects.get(id=pk)
        helicopter.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)