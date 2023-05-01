from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator

class Place(models.Model):
    city=models.CharField(max_length=200,unique=True)
    
    def _str_(self):
        return self.city
    


    @property
    def Place_hotels(self):
        return Hotel.objects.filter(place=self)
    


class Hotel(models.Model):
    hotelname=models.CharField(max_length=200)
    hoteltype=(
        ("5star","5star"),
        ("4star","4star"),
        ("Lodge","Lodge"),
        ("Doormetry","Doormetry")
    )
    place=models.ForeignKey(Place,on_delete=models.CASCADE)
    image=models.ImageField(upload_to="images",null=True,blank=True)
    htype=models.CharField(max_length=200,choices=hoteltype,default="5star")
    address=models.CharField(max_length=200)
    contact=models.PositiveIntegerField()
    description=models.CharField(max_length=260)
    
    def _str_(self):
        return self.hotelname
    

    @property
    def hotel_room(self):
        return Rooms.objects.filter(hotel=self)

    @property
    def hotel_offer(self):
        return Offers.objects.filter(hotel=self)
    
    @property
    def hotel_review(self):
        return Review.objects.filter(hotel=self)
    
    



class Rooms(models.Model):
    status=(
        ("available","available"),
        ("not available","not available")
    )
    roomtype=(
        ("classic","classic"),
        ("premium","premium"),
        ("dulex","dulex")
    )
    bed=(
        ("2-double bed","2-double bed"),
        ("3-king size","3-king size"),
        ("1-single bed","1-single bed")
    )
    foodmenu=(
        ("breakfast included","breakfast included"),
        ("breakfast not-included","breakfast not-included"),
        ("breakfast & dinner included","breakfast & dinner included"),
        ("breakfast & dinner not-included","breakfast & dinner not-included")
    )
    hotel=models.ForeignKey(Hotel,models.CASCADE)
    roomstatus=models.CharField(max_length=200,choices=status,default="available")
    rtype=models.CharField(max_length=200,choices=roomtype,default="classic")
    capacity=models.CharField(max_length=200,choices=bed,default="2-double bed")
    roomimage=models.ImageField(upload_to="images",null=True,blank=True)
    description=models.CharField(max_length=260)
    price=models.PositiveIntegerField()
    doornum=models.IntegerField()
    fmenu=models.CharField(max_length=200,choices=foodmenu,default="breakfast included")



    @property
    def Book_room(self):
        return Booking.objects.filter(room=self)

class Offers(models.Model):
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE)
    discount=models.IntegerField()
    is_available=models.BooleanField(default=True)
    startdate=models.DateField(null=True)
    enddate=models.DateField(null=True)    
   


class Booking(models.Model):
    room=models.ForeignKey(Rooms,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    checkin=models.DateTimeField(auto_now_add=True)
    checkout=models.DateTimeField(auto_now_add=True)
    amount=models.FloatField()
    booked_on=models.DateTimeField(auto_now_add=True)



class Review(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE)
    comment=models.CharField(max_length=260)
    rating=models.FloatField(validators=[MinValueValidator(1),MaxValueValidator(5)]) 
    def _str_(self):
        return self.comment  
    


class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    phone=models.PositiveIntegerField(unique=True)  



class HotelOwner(models.Model):
    owner=models.OneToOneField(User,on_delete=models.CASCADE)
    mobileno=models.PositiveIntegerField(unique=True)
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE)
    owneraddress=models.CharField(max_length=200)