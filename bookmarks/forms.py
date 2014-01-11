from django import  forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
#from django.core.validators import  *



class RegistrationForm(forms.Form):

  username = forms.CharField(label='name')
  email = forms.EmailField(label='Email')
  password1 = forms.CharField(
    label='Password',
    widget=forms.PasswordInput()
  )
  password2 = forms.CharField(
    label='Password (Again)',
    widget=forms.PasswordInput(),
    error_messages={'invalid':'Please enter a valid Password.'}

  )

  def cleaned_username(self):
    username = self.cleaned_data['username']
    print username
    if not re.search(r'^\w+$', username):
        raise forms.ValidationError('Username can only contain alphanumeric characters and the underscore.')
    try:
        User.objects.get(username=username)
    except:
        return username
    raise forms.ValidationError('Username is already taken.')

  def cleaned_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2:
                return password2
            raise forms.ValidationError('Passwords do not match.')


class BookmarkSaveForm(forms.Form):
  url = forms.URLField(
    label='URL',
    widget=forms.TextInput(attrs={'size': 64})
  )
  title = forms.CharField(
    label='Title',
    required=False,
    widget=forms.TextInput(attrs={'size': 64})
  )
  tags = forms.CharField(
    label='Tags',
    required=False,
    widget=forms.TextInput(attrs={'size': 64})
  )
  share = forms.BooleanField(
   label='Share on the main page', 
   required=False
  )

class SearchForm(forms.Form):
  query = forms.CharField(
      label='Enter a keyword to search for',
      widget=forms.TextInput(attrs={'size': 32})
  )
class StatusForm(forms.Form):
  status = forms.CharField(
      label='is',
      widget=forms.TextInput(attrs={'size': 32})
  )


