from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile


# Extending this so we have more fields in the signup page
class SignUpForm(UserCreationForm):
    # username = forms.CharField(max_length=100, help_text='')

    class Meta:
        model = User
        # help_texts = {'username': None}
        fields = ('username', 'password1', 'password2')


class UserProfileForm(forms.ModelForm):         # 5:06

    class Meta:
        model = UserProfile
        fields = ('current_city',)

# By default form tries to CREATE on post. this form is null because of this process. Edit form is calling on form 
# class EditProfileForm(forms.ModelForm):

#     class Meta:
#         model = UserProfile
#         fields = ('current_city',)


class LogInForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'password')
