from django.db import models

class Recipe(models.Model):
    foodName = models.CharField(max_length=100)
    foodDescription = models.TextField(max_length=100)
    foodRating = models.IntegerField()  
    foodIngredients = models.CharField(max_length=200)
    foodRecipe = models.CharField(max_length=500)
    foodImage = models.ImageField(upload_to='food_images/')
    
class RecipeRequest(models.Model):
    foodName = models.CharField(max_length=100)
    foodDescription = models.TextField(max_length=100)
    foodRating = models.IntegerField()  
    foodIngredients = models.CharField(max_length=200)
    foodRecipe = models.CharField(max_length=500)
    foodImage = models.ImageField(upload_to='food_images/')