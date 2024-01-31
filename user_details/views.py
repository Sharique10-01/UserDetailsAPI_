 #from django.http import JsonResponse
from .models import UserDetails
from .serializers import UserDetailsSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET','POST'])
def user_list(request):

  if request.method =='GET':
    user = UserDetails.objects.all()#get all the drinks from db
    serializer = UserDetailsSerializer(user,many=True) #serialize them
    return Response({'users':serializer.data}) #return them to any request as JSON file
  
  elif request.method =='POST':
    serializer=UserDetailsSerializer(data=request.data)#de serialize the input data stram
    if serializer.is_valid():# if its valid save
      serializer.save()
      return Response(serializer.data,status=status.HTTP_201_CREATED)#add to the db
    

@api_view(['GET','PUT','DELETE'])
def user_list_db(request,id):

  if request.method =='GET':
    user = UserDetails.objects.all()#get all the drinks from db
    serializer = UserDetailsSerializer(user,many=True) #serialize them
    return Response({'users':serializer.data}) #return them to any request as JSON file
  
  elif request.method =='PUT':
    serializer=UserDetailsSerializer(data=request.data)#de serialize the input data stram
    if serializer.is_valid():# if its valid save
      serializer.save()
      return Response(serializer.data,status=status.HTTP_201_CREATED)#add to the db
    
  elif request.method =='DELETE':
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
