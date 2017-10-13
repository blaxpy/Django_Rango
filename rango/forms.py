from django import forms
from django.contrib.auth.models import User
from rango.models import Category, Page, UserProfile


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'views', 'likes')
        help_texts = {
            'name': "Please enter the category name:"
        }

        widgets = {
            'views': forms.HiddenInput(),
            'likes': forms.HiddenInput(),
        }


class PageForm(forms.ModelForm):
    category = forms.ModelChoiceField(widget=forms.HiddenInput, queryset=Category.objects.all())

    class Meta:
        model = Page
        fields = ('category', 'title', 'url', 'views')

        help_texts = {
            'title': "Please enter the title of the page:",
            'url': "Please enter the URL of the page:",
        }

        widgets = {
            'views': forms.HiddenInput(),
        }

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        if url and not (url.startswith('http://') or url.startswith('https://')):
            url = 'http://' + url
            cleaned_data['url'] = url

            return cleaned_data


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

        widgets = {
            'password': forms.PasswordInput(),
        }


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')
