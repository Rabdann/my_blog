from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField("Название", max_length=150)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Article(models.Model):
    title = models.CharField("Название", max_length=150)
    description = models.TextField("Описание")
    picture = models.ImageField("Картинка")
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="articles",
        verbose_name="Категория",
    )

    author = models.ForeignKey(
        User, models.CASCADE, related_name="articles", verbose_name="Автор"
    )

    def __str__(self) -> str:
        return f"{self.title}:{self.description}"

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
