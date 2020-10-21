from django.db import models

# Create your models here.

class Position(models.Model):
    #id = models.IntegerField(primary_key=True)
    language_1 = models.CharField(max_length=100)    #, null=True
    language_2 = models.CharField(max_length=100)    #, null=True
    email = models.EmailField(max_length=254, unique=False)
    a1 = models.TextField(blank=True, null=True)    #, null=True
    a2 = models.TextField(blank=True, null=True)    #, null=True
    a3 = models.TextField(blank=True, null=True)    #, null=True
    a4 = models.TextField(blank=True, null=True)    #, null=True
    a5 = models.TextField(blank=True, null=True)    #, null=True
    a6 = models.TextField(blank=True, null=True)    #, null=True

    REQUIRED_FIELDS = ['language_1', 'language_2', 'email', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6']

    def __str__(self):
        return '%s %s %s %s %s %s %s %s %s' % (self.language_1, self.language_2, self.email, self.a1, self.a2, self.a3, self.a4, self.a5, self.a6)



