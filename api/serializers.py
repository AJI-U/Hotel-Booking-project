from django.contrib.auth.models import User
from rest_framework import serializers
from hotel.models import UserProfile,Hotel,Place,Rooms,Offers,Booking,Review



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username","email","password"]

        def create(self,validated_data):
            return User.objects.create_user(**validated_data)
        
class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username","email","password"]

        def create(self,validated_data):
            return User.objects.create_user(**validated_data)
        



        
class ProfileSerializer(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True)
    
    class Meta:
        model=UserProfile
        fields="_all_"




class BookingSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)
    
    class Meta:
        model=Booking
        fields=["id","user","checkin","checkout","amount","booked_on"]


class ReviewSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True) 
    class Meta:
        model=Review
        fields=["id","user","comment","rating"]



class RoomSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    owner=serializers.CharField(read_only=True)
    Book_room=BookingSerializer(read_only=True,many=True)
    class Meta:
        model=Rooms
        fields=["id","roomstatus","rtype","capacity","roomimage","description","price","doornum","fmenu","owner","Book_room"]


class OfferSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    owner=serializers.CharField(read_only=True)

    class Meta:
        model=Offers
        fields=["id","owner","discount","is_available","startdate","enddate"]






class HotelSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    owner=serializers.CharField(read_only=True)
    hotel_room=RoomSerializer(read_only=True,many=True)
    hotel_offer=OfferSerializer(read_only=True,many=True)
    hotel_review=ReviewSerializer(read_only=True,many=True)
    class Meta:
        model=Hotel
        fields=["id","hotelname","htype","contact","description","image","address","owner","hotel_room","hotel_offer","hotel_review"]


class PlaceSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    owner=serializers.CharField(read_only=True)
    Place_hotels=HotelSerializer(read_only=True,many=True)
    class Meta:
        model=Place
        fields=["id","city","owner","Place_hotels"]