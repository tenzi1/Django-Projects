from django.db import models

class EmpDetails(models.Model):
    Name = models.CharField(max_length=150)
    Email = models.EmailField()
    Contact = models.CharField(max_length=15)
    
    class Meta:
        db_table = "Employee Details"

