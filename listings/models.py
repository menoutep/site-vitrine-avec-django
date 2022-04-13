from django.db import models


# Create your models here.

class Images(models.Model):
    title=models.CharField(max_length=155)
    imgP=models.CharField(max_length=155)
    imgS=models.CharField(max_length=155,null=True)
    imgT=models.CharField(max_length=155,null=True)
    
    def __str__(self):
        return self.title
    
class Icone(models.Model):
    title=models.CharField(max_length=100)
    code=models.CharField(max_length=80)
    
    def __str__(self):
        return self.title
    

      
class Service(models.Model):
    icone=models.ForeignKey(Icone,on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    description=models.TextField()
    
    def __str__(self):
        return self.title
    
class Team(models.Model):
    nom=models.CharField(max_length=140)
    role=models.CharField(max_length=140)
    photo=models.ForeignKey(Images,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nom
    

class Portfolio(models.Model):
    title=models.CharField(max_length=155)
    description=models.TextField(null=True)
    image=models.ForeignKey(Images, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    

class Message(models.Model):
    expediteur=models.CharField(max_length=200)
    email=models.EmailField()
    subject=models.CharField(max_length=255)
    message=models.TextField()
    
    
    def __str__(self):
        return self.expediteur
    
    
