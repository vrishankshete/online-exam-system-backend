from django.db import models

# Create your models here.

#no need of primary key to student, teacher, quetions table
class RegisterForm(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    login_id = models.CharField(max_length=100)
    password = models.CharField(max_length=15)
    id_photo = models.ImageField(default="")
    year = models.CharField(max_length=15)
    dept = models.CharField(max_length=6)
    roll_no = models.CharField(max_length=4)

class Teacher_details(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    login_id = models.CharField(max_length=100)
    password = models.CharField(max_length=15)


class Exam_details(models.Model):
    exam_id = models.CharField(max_length=8)
    subject_id = models.CharField(max_length=8)
    exam_date = models.DateField()
    exam_time = models.TimeField()

class Subjective_ques(models.Model):
    exam_id = models.ForeignKey("Exam_details", on_delete=models.CASCADE)
    ques_text = models.CharField(max_length=500)
    mark = models.IntegerField()

class Objective_ques(models.Model):
    exam_id = models.ForeignKey("Exam_details" , on_delete=models.CASCADE)
    ques_text = models.CharField(max_length=500)
    option1 = models.CharField(max_length=500)
    option2 = models.CharField(max_length=500)
    option3 = models.CharField(max_length=500)
    option4 = models.CharField(max_length=500)
    correct_ans = models.IntegerField()
    mark = models.IntegerField()
       
