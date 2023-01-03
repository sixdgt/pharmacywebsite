from django.shortcuts import render, HttpResponse
from django.views import View
from django.contrib.auth.models import User
# from django.contrib import auth

# Create your views here.
class LoginView(View):
    def get(self, request):
        return render(request, 'authentication/login.html')

class RegisterView(View):
    def get(self, request):
        # return HttpResponse("Hello World")
        return render(request, 'authentication/register.html')
    
    def post(self, request):
        req_email = request.POST.get('email'),
        req_password = request.POST.get('password'),
        req_username = request.POST.get('username'),
        user = User.objects.create_user(email=req_email, username=req_username)
        user.set_password(req_password)
        user.save()
        return render(request, 'authentication/register.html')