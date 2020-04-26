from django import forms 
from django.contrib.auth import (
    authenticate, 
    get_user_model,
    login,
    logout,
)
from django.contrib.auth.models import User 
class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        # username_qs = User.objects.filter(username=username)
        if username and password:
            user = authenticate(username=username, password = password) 
            if not user:
                raise forms.ValidationError('This user doesnot exist')
            elif not user.check_password(password):
                raise forms.ValidationError('Incorrect password')

        return super(UserLoginForm, self).clean(*args, **kwargs)

class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(label='Email')
    email2 = forms.EmailField(label='Confirm Email')
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User 
        help_texts ={
            'username' : None,
        }
        fields = (
            'username', 
            'email',
            'email2',
            'password'
        )
    def clean_email2(self, *args, **kwargs): 
        email1 = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        
        
        if email1 != email2:
            raise forms.ValidationError('Email must match ') 
        
        email_qs = User.objects.filter(email=email1)
        if email_qs.exists():
            raise forms.ValidationError('This email has already been registered.')
        
        return email1 