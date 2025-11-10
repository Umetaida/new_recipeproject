from django.db import models

class Ingredient(models.Model):
    EXPIRY_TYPE_CHOICES = [
        ('賞味期限', '賞味期限'),
        ('消費期限', '消費期限'),
    ]
    
    name = models.CharField(max_length=100)
    quantity = models.CharField(max_length=50, blank=True, null=True)
    date = models.CharField(max_length=50, blank=True, null=True)
    expiry_type = models.CharField(
        max_length=10,
        choices=EXPIRY_TYPE_CHOICES,
        blank=True,
        null=True,
        verbose_name="期限の種類"
    )

class Condition(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)  # 保存時の日時
    status = models.CharField(max_length=100)

    def __str__(self):#管理画面での表示
        return f"{self.created_at.strftime('%Y-%m-%d %H:%M')} - {self.status}"

class SaveRecipe(models.Model):
    recipeId = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    catch_copy = models.TextField(blank=True, null=True)
    foodImageUrl = models.URLField(blank=True, null=True)
    recipeUrl = models.URLField(blank=True, null=True)
    recipeCost = models.CharField(max_length=100, blank=True, null=True)
    ingredients = models.JSONField(default=list)  # 材料リスト
    instructions = models.JSONField(default=list)  # 手順リスト
    recommendation_reason = models.TextField(blank=True, null=True)
    main_nutrients = models.JSONField(default=list)
    cooking_point = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.IntegerField(default=0)

    def __str__(self):
        return self.title