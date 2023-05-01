from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from hotel.models import UserProfile,HotelOwner,Hotel,Place,Booking,Rooms,Review,Offers

class RegistrationForm(UserCreationForm):
    password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    class Meta:
        model=User
        fields=["first_name","last_name","email","username","password1","password2"]
        widgets={
            "first_name":forms.TextInput(attrs={"class":"form-control"}),
            "last_name":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "username":forms.TextInput(attrs={"class":"form-control"})
        }

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))


class OwnerRegistrationForm(UserCreationForm):
    password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    class Meta:
        model=User
        fields=["email","username","password1","password2"]
        widgets={
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "username":forms.TextInput(attrs={"class":"form-control"})
        }

class OwnerLoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

class UserProfileForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields="__all__"

class OwnerProfileForm(forms.ModelForm):
    class Meta:
        model=HotelOwner
        fields="__all__"
class PlaceForm(forms.ModelForm):
    class Meta:
        model=Place
        fields=["city"]       

class HotelForm(forms.ModelForm):
    class Meta:
        model=Hotel
        fields="__all__"
class HotelEditForm(forms.ModelForm):
    class Meta:
        model=Hotel
        fields="__all__"
class RoomForm(forms.ModelForm):
    class Meta:
        model=Rooms
        fields="__all__"
class RoomEditForm(forms.ModelForm):
    class Meta:
        model=Rooms
        fields=["hotel","rtype"]

class BookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields="__all__"

class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields=["comment","rating"]
class OfferForm(forms.ModelForm):
    class Meta:
        model=Offers
        fields="__all__"        