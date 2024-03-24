from django.db import models  

class Review(models.Model):  
    user = models.CharField(max_length=45)  
    email = models.CharField(max_length=45)  
    message = models.CharField(max_length=60)  
    class Meta:  
        db_table = "Review"  