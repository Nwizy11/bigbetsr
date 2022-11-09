from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from .forms import RegistrationForm, LoginForm, UploadForm
from user.models import CustomUser
from django.contrib.auth import login, authenticate
from django.views import View
from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
# Create your views here.
class HomeView(UserPassesTestMixin, View):
    def get(self, request):
        return render(request, 'index.html')
    '''Return to profle if user is already logged in'''
    def test_func(self):
        return self.request.user.is_anonymous
    def handle_no_permission(self):
        return redirect('profile')
class RegistrationView(UserPassesTestMixin,View):
    model = CustomUser
    form = RegistrationForm()
    template_name = 'register.html'
    def get(self, request):
        return render(request, self.template_name, {'form':self.form})
    def post(self, request):
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                usr = CustomUser(email=form.data['email'], name=form.data['name'])
                usr.set_password(form.data['password1'])
                usr.save()
                login(request,usr)
                return redirect('profile')
            return render(request, self.template_name, {'form':form})
    '''Return to profle if user is already logged in'''
    def test_func(self):
        return self.request.user.is_anonymous
    def handle_no_permission(self):
        return redirect('profile')

class CustomLoginView(UserPassesTestMixin, LoginView):
    form = LoginForm()
    def get(self, request):
        return render(request, 'login.html', {'form':self.form})
    def post(self, request):
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                usr= authenticate(email=form.data.get('email'), password=form.data.get('password'))
                if usr is not None:
                    login(request, usr)
                    messages.success(request, 'Successful logged in')
                    return redirect('profile')
            messages.error(request, 'Invalid details, please check your email or password')
            return render(request, 'login.html', {'form': self.form})
    '''Return to profle if user is already logged in'''
    def test_func(self):
        return self.request.user.is_anonymous
    def handle_no_permission(self):
        return redirect('profile')


class ProfileView(LoginRequiredMixin,View):
    form = UploadForm()
    User = get_user_model()
    def get(self, request):
        return render(request,'profile.html', {'form':self.form})
    # def post(self, request):
    #     if request.method == 'POST':
    #         form = UploadForm(request.POST, request.FILES)
    #         if form.is_valid():
    #             obj=form.save(commit=False)
    #             obj.save()
    #             # usr = CustomUser.objects.get(email=request.user.email)
    #             # usr.reciept = form.data.get('reciept')
    #             # usr.save()
    #             messages.success(request, 'Images uploaded successfully, we will get back to you')
    #             return HttpResponse('usr.reciept.url')
    #         messages.success(request, 'An error occurred')
    #         return render(request, 'profile.html', {'form': self.form})
class UpdateProfileView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    fields = ('reciept',)
    successful_url = reverse_lazy('profile')
