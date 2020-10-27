from django.db import models

# Create your models here.
class VotingDetails(models.Model):
    name = models.CharField(max_length=100)
    votes =models.IntegerField()
    
    class Meta:
        db_table = "votingdcdetails"
