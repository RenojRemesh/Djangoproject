from django import forms
from .models import Registration, Registratione
# GalleryDetails
class RegistrationForm(forms.ModelForm):
	Password = forms.CharField(widget=forms.PasswordInput,min_length=8,max_length=8)
	ConfirmPassword = forms.CharField(widget=forms.PasswordInput,min_length=8,max_length=8)
	class Meta():
		model=Registration
		fields = '__all__'

class LoginForm(forms.ModelForm):
	Password = forms.CharField(widget = forms.PasswordInput)
	class Meta():
		model = Registration
		fields = ('Email','Password',)


class UpdateForm(forms.ModelForm):
	class Meta():
		model = Registration
		fields = ('Firstname','Lastname','Email','Age')


class ChangePass(forms.Form):
	oldpassword = forms.CharField(required = True,min_length=0,max_length=50,widget=forms.PasswordInput(attrs={'class':'form_control'}))
	newpassword = forms.CharField(required = True,min_length=0,max_length=50,widget=forms.PasswordInput(attrs={'class':'form_control'}))
	confirm_password = forms.CharField(required = True,min_length=0,max_length=50,widget=forms.PasswordInput(attrs={'class':'form_control'}))

class RegistrationForme(forms.ModelForm):
	class Meta():
		model=Registratione
		fields = '__all__'