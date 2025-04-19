from rest_framework import generics
from .models import RecipeRequest
from .serializers import RecipeRequestSerializer

class RecipeCreateView(generics.CreateAPIView):
    queryset = RecipeRequest.objects.all()
    serializer_class = RecipeRequestSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class RecipeRequestListView(generics.ListAPIView):
    serializer_class = RecipeRequestSerializer

    def get_queryset(self):
         return RecipeRequest.objects.filter(user=self.request.user)
