from django import forms
from django.forms import TextInput, EmailInput, FileInput
from user.models import CustomUser
from django.contrib.auth import get_user_model, login

User = get_user_model()

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email', widget=EmailInput(attrs={'placeholder':'Email', 'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password', 'class':'form-control'}), label='Password', max_length=355)

class RegistrationForm(forms.ModelForm):
    email = forms.EmailField(label='Email', widget=EmailInput(attrs={'placeholder':'Email', 'class':'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password', 'class':'form-control'}), label='Password', max_length=355)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm', 'class':'form-control'}), label='Confirm password', max_length=355)
    name = forms.CharField(widget=TextInput(attrs={'placeholder':'Full name', 'class':'form-control'}), label='name', max_length=355)
    class Meta:
        model = CustomUser
        fields = ['email', 'name', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        usr = User.objects.filter(email=email)
        if usr.exists():
            self.add_error('email', 'Email already exists')
        return email
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 is not None and password1 != password2:
            self.add_error('password2', 'Password does not match')
        return cleaned_data
class UploadForm(forms.ModelForm):
    # reciept = forms.ImageField(widget=forms.FileInput(attrs={'placeholder':'Email', 'class':'form-control'}))
    class Meta:
        model = CustomUser
        fields = ['reciept']





