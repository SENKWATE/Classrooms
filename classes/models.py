from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Classroom(models.Model):
	name = models.CharField(max_length=120)
	subject = models.CharField(max_length=120)
	year = models.IntegerField()
	teacher = models.ForeignKey(User, default=1, on_delete=models.CASCADE)

	def get_absolute_url(self):
		return reverse('classroom-detail', kwargs={'classroom_id':self.id})


gender_choices = (
	('Male','Male'),
	('Female','Female'),
	)

class Student(models.Model):
	name = models.CharField(max_length=30)
	date_of_birth=models.DateField()
	gender = models.CharField(max_length=10, choices = gender_choices)
	exam_grade = models.FloatField(default=65)
	classroom = models.ForeignKey(Classroom, default=1, on_delete=models.CASCADE)


