from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
    	full_name = self.first_name + ' ' + self.last_name
    	return full_name

# class Posts(models.Model):
#     question = models.CharField(max_length=200)
#     a_text = models.CharField(max_length=200)
#     b_text = models.CharField(max_length=200)
#     uid = models.foreignKey

#     def __str__(self):
#     	full_name = self.first_name + ' ' + self.last_name
#     	return full_name