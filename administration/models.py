from django.db import models

# Create your models here.
class user_details(models.Model):
	username=models.CharField(max_length=30)
	address=models.CharField(max_length=150)
	phone=models.CharField(max_length=20)
	age=models.CharField(max_length=10)
	gender=models.CharField(max_length=10)
	bloodgroup=models.CharField(max_length=10)
	email=models.CharField(max_length=30)
	login_id=models.CharField(max_length=10)
	approval=models.CharField(max_length=10)

class specilizatin(models.Model):
	specilization=models.CharField(max_length=20)


class doctor_details(models.Model):
	username=models.CharField(max_length=30)
	regno=models.CharField(max_length=30)
	email=models.CharField(max_length=30)
	place=models.CharField(max_length=150)
	phone=models.CharField(max_length=30)
	specialization=models.CharField(max_length=30)
	photo=models.ImageField(upload_to = 'photo')
	login_id=models.CharField(max_length=10)
	active_days=models.CharField(max_length=15)
	consolt_fee=models.CharField(max_length=20)
	appoint_limit=models.CharField(max_length=10)
	time_slots=models.CharField(max_length=20)
	approval=models.CharField(max_length=10)


class medical_details(models.Model):
	name=models.CharField(max_length=30)
	address=models.TextField()
	phone=models.CharField(max_length=30)
	pincode=models.CharField(max_length=30)

class appointment(models.Model):
	user_ref_id=models.CharField(max_length=10)
	doctor_ref_id=models.CharField(max_length=10)
	slot_id=models.CharField(max_length=10)
	date=models.CharField(max_length=10)



class prescription(models.Model):
	user_ref_id=models.CharField(max_length=10)
	doctor_ref_id=models.CharField(max_length=10)
	date=models.CharField(max_length=10)
	prescription=models.TextField()
	diets_tips=models.TextField()

class results(models.Model):
	user_ref_id=models.CharField(max_length=10)
	result= models.ImageField(upload_to = 'result')

class rating(models.Model):
	doc_id=models.CharField(max_length=10)
	rating=models.CharField(max_length=15)
	review= models.TextField()

class payments(models.Model):
	Amount=models.CharField(max_length=10)
	cardno=models.CharField(max_length=10)
