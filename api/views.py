from django.shortcuts import render

from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import ViewSet,ModelViewSet,GenericViewSet
from rest_framework.mixins import CreateModelMixin
from django.contrib.auth.models import User
from rest_framework import authentication,permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from hotel.models import UserProfile,Hotel,Place,Rooms,Offers,Booking,Review
from api.serializers import UserSerializer,OwnerSerializer,ProfileSerializer,HotelSerializer,PlaceSerializer,RoomSerializer,OfferSerializer,BookingSerializer,ReviewSerializer
# Create your views here.
class UsersView(GenericViewSet,CreateModelMixin,):
    serializer_class=UserSerializer
    queryset=User.objects.all()

    def create(self, request, *args, **kwargs):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            usr=User.objects.create_user(**serializer.validated_data)
            serializer=UserSerializer(usr,many=False)
            return Response(data=serializer.data)
        else:
             return Response(data=serializer.errors)
        

class OwnersView(GenericViewSet,CreateModelMixin,):
    serializer_class=OwnerSerializer
    queryset=User.objects.all()

    def create(self, request, *args, **kwargs):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            usr=User.objects.create_user(**serializer.validated_data)
            serializer=UserSerializer(usr,many=False)
            return Response(data=serializer.data)
        else:
             return Response(data=serializer.errors)
        
class ProfileView(ModelViewSet):
    serializer_class=ProfileSerializer
    queryset=UserProfile.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    # def create(self,request,args,*kwargs):
    #     serializer=ProfileSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save(user=request.user)
    #         return Response(data=serializer.data)
    #     else:
    #         return Response(data=serializer.errors)


    def get_queryset(self):
        return UserProfile.objects.filter(user=self.request.user)





class Placeview(ModelViewSet):
    serializer_class=PlaceSerializer
    queryset=Place.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]


    @action(methods=["post"],detail=True)
    def add_hotel(self,request,*args,**kwargs):
        serializer=HotelSerializer(data=request.data)
        id=kwargs.get("pk")
        pla=Place.objects.get(id=id)
        
        if serializer.is_valid():
            serializer.save(place=pla)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)  
    

class HotelView(ModelViewSet):
    serializer_class=HotelSerializer
    queryset=Hotel.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]


    def perform_create(self,serializer):
        serializer.save(user=self.request.user)

    @action(methods=["post"],detail=True)
    def add_room(self,request,*args,**kwargs):
        serializer=RoomSerializer(data=request.data)
        id=kwargs.get("pk")
        hote=Hotel.objects.get(id=id)
        
        if serializer.is_valid():
            serializer.save(hotel=hote)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)  
        

    @action(methods=["post"],detail=True)
    def add_offer(self,request,*args,**kwargs):
        serializer=OfferSerializer(data=request.data)
        id=kwargs.get("pk")
        hote=Hotel.objects.get(id=id)
        
        if serializer.is_valid():
            serializer.save(hotel=hote)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)  
        

    @action(methods=["post"],detail=True)
    def add_review(self,request,*args,**kwargs):
        serializer=ReviewSerializer(data=request.data)
        id=kwargs.get("pk")
        hote=Hotel.objects.get(id=id)
        user=request.user
        if serializer.is_valid():
            serializer.save(user=user,hotel=hote)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors) 


class RoomView(ModelViewSet):
    serializer_class=RoomSerializer
    queryset=Rooms.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]


    def perform_create(self,serializer):
        serializer.save(user=self.request.user)

    @action(methods=["post"],detail=True)
    def roombooking(self,request,*args,**kwargs):
        serializer=BookingSerializer(data=request.data)
        id=kwargs.get("pk")
        rom=Rooms.objects.get(id=id)
        user=request.user
        if serializer.is_valid():
            serializer.save(user=user,room=rom)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors) 

class OfferView(ModelViewSet):
    serializer_class=OfferSerializer
    queryset=Offers.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

def perform_create(self,serializer):
        serializer.save(user=self.request.user)

class BookingView(ModelViewSet):
    serializer_class=BookingSerializer
    queryset=Booking.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]


    def perform_create(self,serializer):
     serializer.save(user=self.request.user)

    def destroy(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Booking.objects.get(id=id).delete()
        return Response(data="deleted")  
    




class ReviewView(ModelViewSet):
    serializer_class=ReviewSerializer
    queryset=Review.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)