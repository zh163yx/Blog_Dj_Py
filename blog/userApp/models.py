from django.db import models

# Create your models here.
class User(models.Model):
    userName = models.CharField(max_length=10)
    passWord = models.CharField(max_length=100)
    email = models.EmailField()
    emailCode = models.CharField(max_length=10,blank=True)
    emailCodeTime = models.DateTimeField(blank=True)

    def __str__(self):
        return "userName:%s; email:%s" % (self.userName,str(self.email))
