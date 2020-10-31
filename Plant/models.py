from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import User
from account.models import customUser
from django.urls import reverse

# Create your models here.
class Plant(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	q_avail = models.IntegerField(default=0)
	price = models.FloatField(default=0.0)
	manager = models.ForeignKey(customUser, on_delete=models.CASCADE)
	plant_image = models.ImageField(default='default.jpg', upload_to='plant_pics')

	def __str__(self):
		return f'{self.name} , available : {self.q_avail}'

	def get_absolute_url(self):
		return reverse('plant-detail', kwargs={'pk':self.pk})

class Orders(models.Model):
	plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
	seller = models.CharField(max_length=100)
	buyer = models.CharField(max_length=100)
	quantity = models.IntegerField(default=1)
	status = models.BooleanField(default=False)

	def __str__(self):
		return f'[ plant:{ self.plant.name}, seller:{self.seller}, buyer={self.buyer} for {self.quantity} ]'

	def get_absolute_url(self):
		return reverse('myorders',kwargs={ 'pk' : self.pk })