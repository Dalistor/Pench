from django.db import models
from django.contrib.auth.models import User

class Folder (models.Model):
	name 		= models.CharField(max_length=50)
	location 	= models.ForeignKey('Folder', on_delete=models.CASCADE, blank=True, null=True)

	def __str__(self):
		return self.name

class File (models.Model):
	name 		= models.CharField(max_length=1000, blank=True)
	file 		= models.FileField(upload_to='data/')
	location 	= models.ForeignKey('Folder', on_delete=models.CASCADE)

	def __str__(self):
		return self.name