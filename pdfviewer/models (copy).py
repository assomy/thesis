from django.db import models
from django.db.models.signals import pre_save
from django.conf import settings
from pyPdf import PdfFileReader
import os, os.path
import shutil, subprocess

PDF_PATH = getattr(settings, "PDF_PATH", "pdfs")
PDF_IMAGE_PATH = getattr(settings, "PDF_IMAGE_PATH", "pdfimages")

class city(models.Model):
   name = models.CharField(blank=True, null=True,max_length=255)
   country = models.CharField(blank=True, null=True,max_length=255)
   

class aminites(models.Model):
   disciption  = models.CharField(blank=True, null=True,max_length=255)
   
class bed(models.Model):
   disciption  = models.CharField(blank=True, null=True,max_length=255)

   
   
class customers(models.Model):
   personalInformation = models.CharField(blank=True, null=True,max_length=255)
   payment = models.CharField(blank=True, null=True,max_length=255)
   childern = models.IntegerField()
   
class hotel(models.Model):
   name = models.CharField(blank=True, null=True,max_length=255)
   address = models.CharField(blank=True, null=True,max_length=255)
   city = models.ForeignKey(city) 
   aminites = models.ForeignKey(aminites) 


   
 class room(models.Model):
   smooking = models.BooleanField(default=True)
   bedtype = models.ForeignKey(bed) 
   hotel = models.ForeignKey(hotel) 
   adult = models.IntegerField()
   
   
 class book(models.Model):
   customer = models.ForeignKey(customers) 
   roomID = models.ForeignKey(room) 
   FROM = models.DateTimeField(auto_now_add=True)
   TO = models.DateTimeField()

   
