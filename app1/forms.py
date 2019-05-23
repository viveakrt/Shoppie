from django import forms
from .models import *


class LoginForms(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': "Enter your Email", }), )
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': "Password"}), )

    class Meta:
        model = Shopkeeper
        fields = ['email', 'password']


class UserForms(forms.ModelForm):
    shopkeeper_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Enter your Name"}), )
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': "Password"}), )
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': "Enter your Email"}), )

    class Meta:
        model = Shopkeeper
        fields = ['shopkeeper_name', 'email', 'password']


class ShopkeeperData(forms.ModelForm):
    shopkeeper_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Enter your Name"}), )
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': "Password"}), )
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': "Enter your Email"}), )
    phone_no = forms.IntegerField()
    photo = forms.ImageField()
    address = forms.Textarea()

    class Meta:
        model = Shopkeeper
        fields = ['shopkeeper_name', 'email', 'password','photo','phone_no','address']


class Search(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name']
        widgets = {'product_name': forms.TextInput(attrs={'type':'search', 'name':'Search', 'placeholder':'Search for a Product...', 'required':''})}