# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

# they are common field.
# we need to make it remove redundancy
'''
class common():
	input_id = models.CharField(max_length=45)
	input_ip = models.CharField(max_length=45)
	input_date = models.TimeField(auto_now_add=True)
	update_id = models.CharField(max_length=45)
	update_ip = models.CharField(max_length=45)
	update_date = models.TimeField(auto_now=True)
'''

# You can see follow address for checking schema
# https://github.com/BJ-Lim/Capstone_Design/blob/master/database/db_schema_v2.PNG


#class subject(models.Model, common):
class subject(models.Model):
	pri_key = models.AutoField(primary_key=True)
	year = models.CharField(max_length=4, null=False)
	semester = models.IntegerField(null=False)
	subject_cd = models.CharField(max_length=20, null=False)
	classes = models.CharField(max_length=2, null=False)

	title = models.CharField(max_length=100)
	grade = models.IntegerField()

	# we need to make it remove redundancy
	input_id = models.CharField(max_length=45)
	input_ip = models.CharField(max_length=45)
	input_date = models.TimeField(auto_now_add=True)
	update_id = models.CharField(max_length=45)
	update_ip = models.CharField(max_length=45)
	update_date = models.TimeField(auto_now=True)
	class Meta:
		unique_together = ('year', 'semester', 'subject_cd', 'classes')


class student(models.Model):
	student_id = models.CharField(max_length=10, primary_key=True)
	student_name = models.CharField(max_length=45)

	# we need to make it remove redundancy
	input_id = models.CharField(max_length=45)
	input_ip = models.CharField(max_length=45)
	input_date = models.TimeField(auto_now_add=True)
	update_id = models.CharField(max_length=45)
	update_ip = models.CharField(max_length=45)
	update_date = models.TimeField(auto_now=True)


class professor(models.Model):
	professor_id = models.CharField(max_length=10, primary_key=True)
	professor_name = models.CharField(max_length=45)

	# we need to make it remove redundancy
	input_id = models.CharField(max_length=45)
	input_ip = models.CharField(max_length=45)
	input_date = models.TimeField(auto_now_add=True)
	update_id = models.CharField(max_length=45)
	update_ip = models.CharField(max_length=45)
	update_date = models.TimeField(auto_now=True)

class signup_class(models.Model):
	# Table must have one key in Django
	not_use_pri_key = models.AutoField(primary_key=True)
	# sub_seq same as year, semester, subject_cd, classes
	sub_seq = models.ForeignKey(subject, on_delete=models.CASCADE)
	student = models.ForeignKey(student, on_delete=models.CASCADE)

	# we need to make it remove redundancy
	input_id = models.CharField(max_length=45)
	input_ip = models.CharField(max_length=45)
	input_date = models.TimeField(auto_now_add=True)
	update_id = models.CharField(max_length=45)
	update_ip = models.CharField(max_length=45)
	update_date = models.TimeField(auto_now=True)

class subject_has_professor(models.Model):
	# Table must have one key in Django
	not_use_pri_key = models.AutoField(primary_key=True)
	# sub_seq same as year, semester, subject_cd, classes
	sub_seq = models.ForeignKey(subject, on_delete=models.CASCADE)
	professor = models.ForeignKey(professor, on_delete=models.CASCADE)
	represent_yn = models.BooleanField(default=False)

	# we need to make it remove redundancy
	input_id = models.CharField(max_length=45)
	input_ip = models.CharField(max_length=45)
	input_date = models.TimeField(auto_now_add=True)
	update_id = models.CharField(max_length=45)
	update_ip = models.CharField(max_length=45)
	update_date = models.TimeField(auto_now=True)


class assignment(models.Model):
	sequence = models.IntegerField(null=False, primary_key=True)
	# sub_seq same as year, semester, subject_cd, classes
	sub_seq = models.ForeignKey(subject, on_delete=models.CASCADE)
	assignment_name = models.CharField(max_length=100)
	assignment_desc = models.TextField()
	
	# we need to make it remove redundancy
	input_id = models.CharField(max_length=45)
	input_ip = models.CharField(max_length=45)
	input_date = models.TimeField(auto_now_add=True)
	update_id = models.CharField(max_length=45)
	update_ip = models.CharField(max_length=45)
	update_date = models.TimeField(auto_now=True)

class submit(models.Model):
	# Table must have one key in Django
	not_use_pri_key = models.AutoField(primary_key=True)
	assign_seq = models.ForeignKey(subject, on_delete=models.CASCADE)
	student = models.ForeignKey(student, on_delete=models.CASCADE)
	source = models.TextField()
	# Is it required?
	comment = models.CharField(max_length=100)
	score = models.IntegerField()
