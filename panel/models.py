from django.db import models

# Create your models here.

class A1(models.Model):
    id = models.IntegerField(primary_key=True)
    category = models.CharField(max_length=100, null=True)
    text = models.TextField(blank=True, null=True)

    REQUIRED_FIELDS = ['id', 'category', 'text']

    def __str__(self):
        return '%s %s %s' % (self.id, self.category, self.text)

class A2(models.Model):
    id = models.IntegerField(primary_key=True)
    category = models.CharField(max_length=100, null=True)
    text = models.TextField(blank=True, null=True)

    REQUIRED_FIELDS = ['id', 'category', 'text']

    def __str__(self):
        return '%s %s %s' % (self.id, self.category, self.text)

class A3 (models.Model):
    id = models.IntegerField(primary_key=True)
    category = models.CharField(max_length=100)
    text = models.TextField(blank=True, null=True)

    REQUIRED_FIELDS = ['id', 'category', 'text']

    def __str__(self):
        return '%s %s %s' % (self.id, self.category, self.text)

class A4 (models.Model):
    id = models.IntegerField(primary_key=True)
    category = models.CharField(max_length=100)
    text = models.TextField(blank=True, null=True)

    REQUIRED_FIELDS = ['id', 'category', 'text']

    def __str__(self):
        return '%s %s %s' % (self.id, self.category, self.text)

class A5 (models.Model):
    id = models.IntegerField(primary_key=True)
    category = models.CharField(max_length=100)
    text = models.TextField(blank=True, null=True)

    REQUIRED_FIELDS = ['id', 'category', 'text']

    def __str__(self):
        return '%s %s %s' % (self.id, self.category, self.text)

class A6 (models.Model):
    id = models.IntegerField(primary_key=True)
    category = models.CharField(max_length=100)
    text = models.TextField(blank=True, null=True)

    REQUIRED_FIELDS = ['id', 'category', 'text']

    def __str__(self):
        return '%s %s %s' % (self.id, self.category, self.text)