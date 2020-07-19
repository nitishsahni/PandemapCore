from django.shortcuts import render
from .models import Place, Interval
from rest_framework.decorators import api_view
from .serializers import PlaceSerializer, IntervalSerializer
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def places_list(request, format=None):
    if request.method == 'GET':
        places = Place.objects.all()
        serializer = PlaceSerializer(places, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PlaceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def place_detail(request, pk, format=None):
    try:
        place = Place.objects.get(pk=pk)
    except Place.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PlaceSerializer(place)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PlaceSerializer(place, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        place.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def intervals_list(request, format=None):
    if request.method == 'GET':
        intervals = Interval.objects.all()
        serializer = IntervalSerializer(intervals, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = IntervalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def interval_detail(request, pk, format=None):
    try:
        interval = Interval.objects.get(pk=pk)
    except Interval.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = IntervalSerializer(interval)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = IntervalSerializer(interval, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        interval.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)