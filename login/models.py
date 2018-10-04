from django.db import models

# Create your models here.
position = (
            ('Admin','Admin'),
            ('Doctor','Doctor'),
            ('Lab','Lab'),
            ('Patient','Patient'),
            )


class users(models.Model):
    user_id=models.AutoField(max_length=11,primary_key=True)
    username = models.CharField(max_length=50)
    password=models.CharField(max_length=35)
    designation=models.CharField(choices=position,max_length=10)
    class Meta:
    	verbose_name_plural="users"
    def __str__(self):
    	return self.username


