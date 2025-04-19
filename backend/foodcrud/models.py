from django.db import models
from django.contrib.auth.models import User

Choices = [
    ('pending', 'Pending'),
    ('approved', 'Approved'),
    ('declined', 'Declined'),
]

class Recipe(models.Model):
    foodName = models.CharField(max_length=100)
    foodDescription = models.TextField(max_length=100)
    foodRating = models.IntegerField()  
    foodIngredients = models.CharField(max_length=200)
    foodRecipe = models.CharField(max_length=500)
    foodImage = models.ImageField(upload_to='food_images/')

    def __str__(self):
        return self.foodName

class RecipeRequest(models.Model):
    foodName = models.CharField(max_length=100)
    foodDescription = models.TextField(max_length=100)
    foodRating = models.IntegerField()  
    foodIngredients = models.CharField(max_length=200)
    foodRecipe = models.CharField(max_length=500)
    foodImage = models.ImageField(upload_to='food_images/')
    approvalStatus = models.CharField(
        max_length=10,
        choices=Choices,
        default='pending',
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Request for {self.foodName} by {self.user.username} ({self.approvalStatus})"
