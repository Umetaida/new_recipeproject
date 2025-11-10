#データを利用できる形に変換する　Python ⇔ JSON
from rest_framework import serializers
from .models import Ingredient, Condition, SaveRecipe

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'#モデルのすべてのフィールドを対象

class ConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Condition
        fields = ["id", "status", "created_at"]#３つだけを対象

class SaveRecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaveRecipe
        fields = "__all__"