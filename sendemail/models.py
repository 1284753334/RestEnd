from django.db import models

class Grade(models.Model):
    g_name = models.CharField(max_length=16, unique=True)
    g_position = models.CharField(max_length=20)

    def __str__(self):
        return self.g_name


class Student(models.Model):
    s_name= models.CharField(max_length=64,unique=True)
    s_age = models.IntegerField(default=15)
    s_sex = models.BooleanField(default=False)
    s_height = models.FloatField(default=1.66)
    s_weight = models.FloatField(default=50)
    s_grade = models.ForeignKey(Grade,on_delete=models.CASCADE)

    def __str__(self):
        return self.s_name






