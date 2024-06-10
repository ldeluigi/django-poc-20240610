from django.db import models


class AModel1(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    modified1 = models.DateTimeField(auto_now=True)
    created1 = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class AModel2(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    modified2 = models.DateTimeField(auto_now=True)
    created2 = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class AModel3(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    modified3 = models.DateTimeField(auto_now=True)
    created3 = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class AModel4(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    modified4 = models.DateTimeField(auto_now=True)
    created4 = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class AModel5(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    modified5 = models.DateTimeField(auto_now=True)
    created5 = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
