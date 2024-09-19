from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import User
from api.serializer import UserSerializer

@api_view(['GET'])
def get_user(request):
    return Response(UserSerializer({'name':'johnny','age':19}).data)

@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data , status= status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_all_user(request):
    users= User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_user_by_id(request,pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(UserSerializer(user).data)


@api_view(['PUT','PATCH'])
def update_user(request,pk):
    user = User.objects.get(pk=pk)
    serializer = UserSerializer(user,data=request.data,partial=('PATCH',request.method))
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data , status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_user(request,pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)