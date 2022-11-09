from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_view
from django.conf import settings
from django.conf.urls.static import static
from .forms import LoginForm
from .views import *
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', CustomLoginView.as_view(template_name='login.html'), name='login'),
    path('register/', RegistrationView.as_view(), name='registration'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('logout/', auth_view.LogoutView.as_view(template_name='index.html'), name='logout'),
    path('confirmation/<int:pk>', UpdateProfileView.as_view(), name='update')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)