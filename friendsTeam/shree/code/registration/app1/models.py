from django.db import models

# Create your models here.

class New_Registration(models.Model):
    fullname = models.CharField(max_length=25)
    age = models.IntegerField()
    dob = models.DateTimeField()
    Email = models.EmailField(unique=True)
    register_password = models.CharField(max_length=20,unique=True)

    class Meta():
        db_table = "register_info"
    #
    # def __str__(self):
    #     return f'''{self.fullname}'''
