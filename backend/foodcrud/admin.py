from django.contrib import admin
from .models import Recipe, RecipeRequest

class RecipeRequestAdmin(admin.ModelAdmin):
    list_display = ('foodName', 'approvalStatus')   
    actions = ['approveRecipeRequest']  

    def approveRecipeRequest(self, request, queryset):   
        for recipeRequest in queryset:
            if recipeRequest.approvalStatus == 'pending':       
                Recipe.objects.create(
                    foodName=recipeRequest.foodName,
                    foodDescription=recipeRequest.foodDescription,
                    foodRating=recipeRequest.foodRating,
                    foodIngredients=recipeRequest.foodIngredients,
                    foodRecipe=recipeRequest.foodRecipe,
                    foodImage=recipeRequest.foodImage,
                )
                recipeRequest.delete()
                
        self.message_user(request, "Selected recipe requests have been approved and moved to Recipe.")

    approveRecipeRequest.short_description = 'Approve selected recipe requests and move to Recipe'

admin.site.register(RecipeRequest, RecipeRequestAdmin)
admin.site.register(Recipe)
