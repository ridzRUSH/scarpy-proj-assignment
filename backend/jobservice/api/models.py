from django.db import models

class JobData(models.Model):
    
    job_title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    posted_at = models.DateField()
    updated_at = models.DateField()

    location_type = models.JSONField(default=list)  
    compensation = models.JSONField(default=dict)  
    employment_type = models.JSONField(default=list) 
    skills = models.JSONField(default=list)  
    
    job_details = models.TextField()
    
    def __str__(self):
        return self.job_title
