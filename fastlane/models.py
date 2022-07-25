from django.db import models

# Create your models here.
class Partner(models.Model):
    partner_name=models.CharField(max_length=50)
    logo=models.ImageField(upload_to="partner_logo/%y")
    def __str__(self) :
        return self.partner_name
    
class Feedback(models.Model):
    feedback_profile=models.ImageField(upload_to="feedback_profile/%y")
    name=models.CharField(max_length=50)
    info=models.CharField(max_length=50)
    statement=models.TextField()
    def __str__(self) :
        return self.name
    
class Team(models.Model):
    name=models.CharField(max_length=50)
    position=models.CharField(max_length=50)
    profile=models.ImageField(upload_to="team_profile/%y")
    def __str__(self) :
        return self.name
    
class OjtTeam(models.Model):
    name=models.CharField(max_length=50)
    position=models.CharField(max_length=50)
    ojtprofile=models.ImageField(upload_to="ojt_profile/%y")
    def __str__(self) :
        return self.name