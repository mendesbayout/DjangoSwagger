from django.db import models
import uuid


class Cheff(models.Model):
    id = models.CharField(primary_key=True, max_length=20, verbose_name="ID_Cheff")
    direction = models.CharField(max_length=120, verbose_name="Direction")
    phone = models.IntegerField()

    def __str__(self):
        return self.id


class Recipe(models.Model):
    id = models.CharField(max_length=120, primary_key=True, verbose_name="Nome")
    
    cheff = models.ForeignKey(Cheff, on_delete=models.CASCADE, verbose_name="Cheff")
    type = models.CharField(max_length=20,
                            choices=[('Receita', 'Receita'), ('Lanche', 'Lanche')])
    thumbnail = models.ImageField(upload_to="recipe_thumbnails", default="recipe_thumbnails/default.png")
    name = models.CharField(max_length=120, unique=True, verbose_name="Receita")

    def __str__(self):
        return self.id


#class Ingredient(models.Model):
    #id = models.CharField(primary_key=True, max_length=20, verbose_name="Ingredientes")
    #recipe = models.ManyToManyField(Recipe)
    #name = models.CharField(max_length=120, unique=True, verbose_name="Name")

    #def __str__(self):
        #return self.id
