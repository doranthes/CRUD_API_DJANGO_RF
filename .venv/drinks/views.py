from django.http import JsonResponse 
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

#=============== READ DATA ALL ===============#
@api_view(['GET','POST'])
def drink_list(request, format=None):

    #=============== READ DATA LATEST ===============#
    if request.method == 'GET':
        drinks = Drink.objects.all()
        serializer = DrinkSerializer(drinks, many=True)
        return Response(serializer.data)

    #=============== CREATE DATA ===============#
    if request.method == 'POST':
        serializer = DrinkSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

#=============== READ DATA SPECIFIC BY ID ===============#
@api_view(['GET','PUT','DELETE'])
def drink_detail(request, id, format=None):

    try:
        drink = Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # =============== READ DATA BY ID  ===============#
    if request.method =='GET':
        serializer = DrinkSerializer(drink)
        return Response(serializer.data)
    # =============== UPDATE DATA BY ID  ===============#    
    elif request.method =='PUT': 
        serializer = DrinkSerializer(drink, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # =============== DELETE DATA BY ID  ===============#
    elif request.method =='DELETE':
        drink.delete()
        return Respons(status=status.HTTP_204_NO_CONTENT)