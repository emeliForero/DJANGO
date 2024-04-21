from django.db import models

class Animal(models.Model):
    animal_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45)
    age = models.IntegerField()
    species = models.CharField(max_length=10)
    url_image = models.CharField(max_length=500)
    state = models.IntegerField()
    shelter = models.CharField(max_length=50)
    class Meta:
        # Nombre de la tabla personalizado
        db_table = 'animal'

class Contact(models.Model):
    contacts_id = models.AutoField(primary_key=True)  # AutoField
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    cell_phone = models.CharField(max_length=20)
    message = models.CharField(max_length=500)
    class Meta:
        # Nombre de la tabla personalizado
        db_table = 'contact'