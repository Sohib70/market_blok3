from django.shortcuts import render,redirect
from .forms import SignupForm,UpdateProfileForm
from django.views import View
from django.contrib import messages
from django.shortcuts import get_object_or_404
from .models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class SignupView(View):
    def get(self,request):
        return render(request,'registration/signup.html',{'form':SignupForm()})


    def post(self,request):
        form = SignupForm(data = request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Sizning hisobingiz yaratildi!")
            return redirect('login')
        return render(request,'registration/signup.html',{'form':form})

class ProfileView(View):
    def get(self,request,username):
        user = get_object_or_404(CustomUser,username = username)
        return render(request,'profile.html',{'customuser':user})


class UpdateProfileView(View,LoginRequiredMixin):
    login_url = 'login'
    def get(self,request):
        form = UpdateProfileForm(instance=request.user)
        return render(request,'profile_update.html',{"form":form})
    def post(self,request):
        form = SignupForm(instance=request.user,data = request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"Sizning hisobingiz ozgartirildi!")
            return redirect('users:profile',request.user)
        return render(request,'registration/signup.html',{'form':form})