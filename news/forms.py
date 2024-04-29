from django import forms

from .models import News, Category, Comment, User


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'rasm']

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']

class PasswordForm(forms.Form):
    password_1 = forms.CharField(max_length=15)
    password_2 = forms.CharField(max_length=15)

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'text', 'rasm', 'tur']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['izoh']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)

