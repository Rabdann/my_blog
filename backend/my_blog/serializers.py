from unicodedata import category
from rest_framework import serializers
from .models import Category, Article


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

    def validate(self, attrs):
        if not (attrs["title"].istitle() and attrs["title"].isalpha()):
            raise serializers.ValidationError(
                "Необходимо ввести текст с большой буквы, содержащий только буквенные символы"
            )
        return super().validate(attrs)


class ArticleSerializer(serializers.ModelSerializer):
    category_title = serializers.ReadOnlyField(source="category.title")
    author_user_name = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Article
        fields = "__all__"
        read_only_fields = ["author"]

    def create(self, validated_data):
        user = self.context["request"].user
        validated_data["author"] = user
        return super().create(validated_data)

    def validate(self, attrs):
        if not (attrs["title"].istitle() and attrs["description"].istitle()):
            raise serializers.ValidationError("Необходимо ввести текст с большой буквы")
        return super().validate(attrs)

    def to_representation(self, instance):
        result = super().to_representation(instance)
        result["user_password"] = instance.author.password
        return result
