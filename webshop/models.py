from django.db import models

# Create your models here.
class Commodity(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.TextField()
	type = models.TextField()
	introduce = models.TextField()
	img_url = models.TextField()
	thumb_url = models.TextField()
	price = models.DecimalField(max_digits=8,decimal_places=2)
	stock = models.IntegerField()
	def __str__(self):
		return self.name
class Thumb(models.Model):
	id = models.AutoField(primary_key=True)
	itemid = models.IntegerField()
	imgurl = models.TextField()
	def __str__(self):
		return self.imgurl
class Option(models.Model):
	id = models.AutoField(primary_key=True)
	itemid = models.IntegerField()
	name = models.TextField()
	def __str__(self):
		return self.name
		
		