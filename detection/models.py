from django.db import models

# Create your models here.

class Vehicle(models.Model):
	registration_no = models.CharField(max_length = 200, null = True)
	model = models.CharField(max_length = 200, blank = True)
	color = models.CharField(max_length = 200, null= True)
	chasis_no = models.CharField(max_length = 200, null= True)
	engine_no = models.IntegerField(max_length = 200, null= True)
	mobile = models.IntegerField(max_length = 200, null= True)
	email= models.CharField(max_length = 200, null= True)
	# location= models.CharField(max_length = 200, null = True, default=settings.MEDIA_ROOT)

	def __str__(self):
		return ("Registration_no = "+str(self.registration_no))