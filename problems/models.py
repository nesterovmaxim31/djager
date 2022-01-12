from django.db import models
from django.urls import reverse

class Listproblems(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class List(models.Model):
    title = models.CharField(max_length=250)
    link = models.CharField(max_length=250)
    code = models.CharField(max_length=1000)
    explanation = models.CharField(max_length=3000)

    def __str__(self):
        return self.title

class List2(models.Model):
    title = models.CharField(max_length=250)
    link = models.CharField(max_length=250)
    code = models.CharField(max_length=1000)
    slug = models.SlugField(max_length=100, unique=True)
    explanation = models.CharField(max_length=3000)
    def __str__(self):
        return self.title

    def geturl(self):
        return reverse('iter', args=[self.slug])


class List3(models.Model):
    title = models.CharField(max_length=250)
    link = models.CharField(max_length=250)
    code = models.TextField()
    slug = models.SlugField(max_length=100, unique=True)
    explanation = models.CharField(max_length=3000)

    def __str__(self):
        return self.title

    def geturl(self):
        return reverse('iter', args=[self.slug])

class List4(models.Model):
    title = models.CharField(max_length=250)
    link = models.CharField(max_length=250)
    text = models.TextField()
    code = models.TextField()
    slug = models.SlugField(max_length=100, unique=True)
    explanation = models.CharField(max_length=3000)

    def __str__(self):
        return self.title

    def geturl(self):
        return reverse('iter', args=[self.slug])

class List5(models.Model):
    title = models.CharField(max_length=250)
    link = models.CharField(max_length=250)
    text = models.TextField()
    code = models.TextField()
    slug = models.SlugField(max_length=100, unique=True)
    explanation = models.TextField()
    def __str__(self):
        return self.title

    def geturl(self):
        return reverse('iter_2', args=[self.slug])