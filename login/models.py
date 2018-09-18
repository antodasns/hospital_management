from django.db import models

# Create your models here.
position = (
            ('1','Admin'),
            ('2','Doctor'),
            ('3','Lab_tech'),
            ('4','Patient'),
            )
class users(models.Model):
    user_id=models.AutoField(max_length=11,primary_key=True)
    usesrname = models.CharField(max_length=50)
    password=models.CharField(max_length=35)
    designation=models.CharField(choices=position,max_length=1)
    class Meta:
    	verbose_name_plural="users"
    def __str__(self):
    	return self.username