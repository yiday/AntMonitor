# -*- coding=utf-8 -*-
from django import forms
from profiles.models import User, UserProfile
from django.contrib.auth.forms import UserCreationForm

class ColorForm(forms.Form):
    color = forms.CharField(label=u'set color', max_length=10)


class UserForm(UserCreationForm):
    username = forms.CharField(max_length=20,
                               label=u"用户名",
                               widget=forms.TextInput(attrs={'placeholder':u"请输入用户名"}))
    email = forms.CharField(max_length=110,
                               label=u"电子邮箱",
                               widget=forms.TextInput(attrs={'placeholder':u"请输入Email"}))

    password1 = forms.CharField(max_length=50, label=u"密码",
                               widget=forms.PasswordInput(attrs={"placeholder":u"请输入密码"})
                               )
    password2 = forms.CharField(max_length=50, label=u"确认密码",
                               widget=forms.PasswordInput(attrs={"placeholder":u"请再次输入密码"})
                               )
    class Meta:
        model = User
        fields = ["username"]


class UserProfileForm(forms.ModelForm):
    nickname = forms.CharField(max_length=20,
                               label=u"昵称",
                               required=False,
                               widget=forms.TextInput(attrs={'placeholder':u"请输入昵称"}))

    class Meta:
        model = UserProfile
        fields = ['nickname',]