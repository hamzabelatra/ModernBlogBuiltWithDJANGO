from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth.models import User
from django import forms

class SignUpForms(UserCreationForm):
    first_name = forms.CharField(max_length= 100,widget =  forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length= 100, widget =  forms.TextInput(attrs={'class':'form-control'}))
    email=forms.EmailField(widget= forms.EmailInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields=('username','first_name','last_name','email','password1','password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForms, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'



class EditForm(forms.ModelForm):
    first_name = forms.CharField(max_length= 100,widget =  forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length= 100, widget =  forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length= 100, widget =  forms.TextInput(attrs={'class':'form-control'}))
    is_active = forms.CharField(max_length= 100, widget =  forms.CheckboxInput(attrs={'class':'form-check'}))

    email=forms.EmailField(widget= forms.EmailInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields=('username','first_name','last_name','email','is_active')


class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(max_length= 100,label= 'Old password', widget =  forms.PasswordInput(attrs={'class':'form-control', 'type':'password' }))
    new_password1 = forms.CharField(max_length= 100, label= 'New password',widget =  forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))
    new_password2 = forms.CharField(max_length= 100, label= 'Confirm password',widget =  forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))
    


    class Meta:
        model = User
        fields=('username','first_name','last_name','email','is_active')


