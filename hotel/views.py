from django.shortcuts import render,redirect
from hotel.forms import RegistrationForm,LoginForm,OwnerRegistrationForm,OwnerLoginForm,UserProfileForm,OwnerProfileForm,HotelForm,HotelEditForm,BookingForm,PlaceForm,RoomForm,RoomEditForm,ReviewForm,OfferForm
from django.views.generic import View,CreateView,FormView,TemplateView,UpdateView
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse_lazy
from hotel.models import UserProfile,HotelOwner,Hotel,Place,Rooms,Booking,Offers,Review
#from hotel import Hotel
from django.contrib.auth import login,authenticate,logout
# Create your views here.

class SignUpView(CreateView):
    model=User
    form_class=RegistrationForm
    template_name="u_register.html"
    success_url=reverse_lazy("signin")

class SigninView(FormView):
    template_name="u_login.html"
    form_class=LoginForm
    
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
           uname=form.cleaned_data.get("username")
           pwd=form.cleaned_data.get("password")
           usr=authenticate(request,username=uname,password=pwd)
           if usr:
                 login(request,usr)
                 return redirect("index")
           else:
                 return render(request,"u_login.html",{"form":form})


class IndexView(View):
     def get(self,request,*args,**kwargs):
        template_name="index.html"
        qs=Hotel.objects.all()
        return render(request,"index.html",{"hotels":qs})


class HotelOwnerRegistrationView(View):

    def get(self, request):
        form = OwnerRegistrationForm()
        return render(request, "o-register.html", {'form': form})

    def post(self, request):
        form =  OwnerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_staff = True
            user.save()
            login(request, user)
            return redirect("o-signin")
        return render(request,"o-login.html" , {"form": form})

class HotelOwnerLoginView(View):

    def get(self, request):
        return render(request,"o-login.html")

    # def post(self, request):
    #     email = request.POST.get("email")
    #     password = request.POST.get("password")
    #     user = authenticate(request, email=email, password=password)
    #     if user is not None and user.is_staff:
    #         login(request, user)
    #         return redirect("o-index")
    #     else:
    #         messages.warning(request, "Invalid login.")
    #         return redirect("o-signin")
    def post(self,request,*args,**kwargs):
        form=OwnerLoginForm(request.POST)
        if form.is_valid():
           uname=form.cleaned_data.get("username")
           pwd=form.cleaned_data.get("password")
           usr=authenticate(request,username=uname,password=pwd)
           if usr:
                 login(request,usr)
                 return redirect("o-index")
           else:
                 return render(request,"o-login.html",{"form":form})

        
class OIndex(FormView):
    template_name="o-index.html"
    form_class=HotelForm
    success_url=reverse_lazy("o-index")


class UserProfileCreateView(CreateView):
    form_class=UserProfileForm
    model=UserProfile
    template_name="u-profile-add.html"
    success_url=reverse_lazy("index")
    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)
    

class ProfileDetailView(TemplateView):
    template_name="u-profile-detail.html"



class ProfileUpdateView(UpdateView):
    model=UserProfile
    form_class=UserProfileForm
    template_name="u-profile-edit.html"
    success_url=reverse_lazy("o-index")
    pk_url_kwarg="id"

class OwnerProfileCreateView(CreateView):
    form_class=OwnerProfileForm
    model=HotelOwner
    template_name="o-profile-add.html"
    success_url=reverse_lazy("index")
    def form_valid(self,form):
        form.instance.owner=self.request.owner
        return super().form_valid(form)

class OwnerProfileDetailView(TemplateView):
    template_name="o-profile-detail.html"

class OwnerProfileUpdateView(UpdateView):
    model=HotelOwner
    form_class=OwnerProfileForm
    template_name="o-profile-edit.html"
    success_url=reverse_lazy("index")
    pk_url_kwarg="id"

class PlaceCreateView(View):
     def get(self,request,*args,**kwargs):
         form=PlaceForm()
         return render(request,"place-add.html",{"form":form})
    
     def post(self,request,*args,**kwargs):
        form=PlaceForm(request.POST)
        if form.is_valid():
            form.instance.user=request.user
            form.save()
            print("saved")
            return redirect("place-list")
        else:
         return render(request,"place-add.html",{"form":form})
class PlaceListView(View):
    def get(self,request,*args,**kwargs):
        qs=Place.objects.all()
        return render(request,"place-list.html",{"place":qs})


class HotelCreateView(View):
    def get(self,request,*args,**kwargs):
        form=HotelForm()
        return render(request,"hotel-add.html",{"form":form})

    def post(self,request,*args,**kwargs):
        form=HotelForm(request.POST)
        if form.is_valid():
            form.instance.user=request.user
            form.save()
            print("saved")
            return redirect("o-index")
        else:
        
           return render(request,"hotel-add.html",{"form":form})


class HotelListView(View):
    def get(self,request,*args,**kwargs):
        print(request.GET["city"])
        qs=Hotel.objects.filter(place__city=request.GET["city"])
        print(qs[0].hotel_name)
        return render(request,"hotel-list.html",{"hotel":qs})



class HotelDetailView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Hotel.objects.get(id=id)
        return render(request,"hotel-detail.html",{"hotel":qs})


class HotelEditView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        print(id)
        obj=Hotel.objects.get(id=id)
        form=HotelEditForm(instance=obj)
        return render(request,"hotel-edit.html",{"form":form})
    def post(self,request,*args,**kwargs):
        id=kwargs.get("id")
        obj=Hotel.objects.get(id=id)
        form=HotelEditForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/hotel/list?city="+obj.place.city)
        else:
            return render(request,"hotel-edit.html",{"form":form})
        

class HotelDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        obj=Hotel.objects.get(id=id)
        city=obj.city
        obj.delete()
        return redirect("/hotel/list?city="+city)

class RoomCreateView(View):
    def get(self,request,*args,**kwargs):
        form=RoomForm()
        return render(request,"room-add.html",{"form":form})

    def post(self,request,*args,**kwargs):
        form=RoomForm(request.POST)
        if form.is_valid():
            form.instance.user=request.user
            form.save()
            print("saved")
            return redirect("room-list")
        else:
        
            return render(request,"room-add.html",{"form":form})
class RoomListView(View):
    def get(self,request,*args,**kwargs):
        # id=kwargs.get("id")
        qs=Rooms.objects.all()
        return render(request,"room-list.html",{"rooms":qs})



class RoomDetailView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Rooms.objects.get(id=id)
        return render(request,"room-detail.html",{"room":qs})


class RoomEditView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        obj=Rooms.objects.get(id=id)
        form=RoomEditForm(instance=obj)
        return render(request,"room-edit.html",{"form":form})
    def post(self,request,*args,**kwargs):
        id=kwargs.get("id")
        obj=Rooms.objects.get(id=id)
        form=RoomEditForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect("/room/"+str(obj.hotel.id)+"/list")
        else:
            return render(request,"room-edit.html",{"form":form})
        

class RoomDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        Rooms.objects.filter(id=id).delete()
        return redirect("room-list")




class BookingView(View):
   def get(self,request,*args,**kwargs):
        form=BookingForm()
        return render(request,"booking_form.html",{"form":form})
   def post(self,request,*args,**kwargs):
        form=BookingForm(request.POST)
        if form.is_valid():
            form.instance.user=request.user
            form.save()
            print("saved")
            return redirect("index")
        else:
         return render(request,"booking_form.html",{"form":form})

class BookingListView(View):
   def get(self,request,*args,**kwargs):
      qs=Booking.objects.filter(user_id=request.user.id)
      print(qs)
      return render(request,"booking-list.html",{"booking":qs})

   
class BookingCancelView(View):
    def get(self,request,*args,**kwargs):
      id=kwargs.get("id")
      Booking.objects.filter(id=id)
      return redirect("index")
    
class OfferCreateView(View):    
    def get(self,request,*args,**kqargs):
     form=OfferForm() 
     return render(request,"offer-add.html",{"form":form}) 
    def post(self,request,*args,**kwargs):
        form=OfferForm(request.POST)
        if form.is_valid():
         form.save()
         return redirect("o-index")
        else:
          return render(request,"offer-add.html",{"form":form}) 


class OffersView(View):
   def get(self,request,*args,**kwargs):
      qs=Offers.objects.all()
      return render(request,"offer-list.html",{"offers":qs})
   
class ReviewCreateView(View):
   def get(self,request,*args,**kwargs):
      form=ReviewForm()
      return render(request,"review-add.html",{"form":form})
   def post(self,request,*args,**kwargs):
      form=ReviewForm(request.POST)
      id=kwargs.get("id")
      pro=Hotel.objects.get(id=id)
      if form.is_valid():
         form.instance.user=request.user
         form.instance.hotel=pro
         form.save()
         return redirect("index")
      else:
         return render(request,"review-add.html",{"form":form})
      

class SignoutView(View):
     def get(self,request,*args,**kwargs):
          logout(request)
          return redirect("base")
     
class HomeView(CreateView):
     def get(self,request,*args,**kwargs):
        template_name="base.html"
        qs=Hotel.objects.all()
        return render(request,"base.html",{"hotels":qs})
