from django.db import models

# Create your models here.
    


class Programme(models.Model):
    id = models.AutoField(primary_key=True)
    programe_photo = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=150)
    price = models.IntegerField()
    feature1 = models.CharField(max_length=150 ,null=True, blank=True)
    feature2 = models.CharField(max_length=150, null=True, blank=True)
    feature3 = models.CharField(max_length=150 ,null=True, blank=True)
    feature4 = models.CharField(max_length=150 ,null=True, blank=True)
    feature5 = models.CharField(max_length=150 ,null=True, blank=True)

    def __str__(self):
      return self.title
    
    

class Praticiene(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(null=True , blank=True)
    praticien_name = models.CharField(max_length=50)
    specialization = models.CharField(max_length=100)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.praticien_name
    

class Testimonial(models.Model):
    id = models.AutoField(primary_key=True)
    patient_image = models.ImageField(null=True, blank=True)
    testimonial = models.TextField(max_length=1000)
    patient_name = models.CharField(max_length=50, null=True, blank=True)
    profession = models.CharField(max_length=50 , null=True , blank=True)

    def __str__(self):
        return self.patient_name 
    


class Message(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15 , null=True, blank=True)
    subject = models.TextField()
    message = models.TextField()

    def __str__(self):
        return self.name
    