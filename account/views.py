from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from .forms import UpdateProfileForm,UpdateUserForm
from django.contrib import messages


# Create your views here.

def register(request):
      if request.method=='POST':
            form=UserCreationForm(request.POST)
            if form.is_valid():
                  form.save()
                  messages.success(request,' Votre compte a ete cree veillez vous connectez')
                  return redirect('login-user')
      else:
            form=UserCreationForm()

      context={'form':form}  

      return render(request,'user/register.html',context)

def profile_user(request):
      return render(request,'user/profile.html')

def profile_update(request):
      if request.method=='POST':
            user_form=UpdateUserForm(request.POST,instance=request.user)
            profile_form=UpdateProfileForm(request.POST,  instance=request.user.profile)
            if user_form.is_valid() and profile_form.is_valid():
             user_form.save()
             profile_form.save()
             return redirect('profile-user')
      else:
            user_form=UpdateUserForm(instance=request.user)
            profile_form=UpdateProfileForm(instance=request.user.profile)

      context={
      'user_form':user_form,
      'profile_form':profile_form,

      }
      return render(request,'user/update_profile.html',context)
      

       
   
