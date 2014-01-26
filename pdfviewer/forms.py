from django import  forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from pdfviewer.models import *
#from django.core.validators import  *
class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields=['pdf_file']

