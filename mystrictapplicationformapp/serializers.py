from rest_framework import serializers
from django.utils import timezone
from mystrictapplicationformapp.models import Reference


class ReferenceSerializer(serializers.ModelSerializer):
    """Сериализатор по модели Reference."""

    class Meta:
        model = Reference
        fields = ("id", "first_name", "patronymic", "last_name", "purpose", "quantity", "comment", "date_of_changes")

    def validate_first_name(self, value):
        if value != value.capitalize():
            raise serializers.ValidationError("Название должно быть с заглавной буквы")
        return value

    def validate_patronymic(self, value):
        if value != value.capitalize():
            raise serializers.ValidationError("Название должно быть с заглавной буквы")
        return value

    def validate_last_name(self, value):
        if value != value.capitalize():
            raise serializers.ValidationError("Название должно быть с заглавной буквы")
        return value

    def validate_purpose(self, value):
        list_of_reasons = ["нужно", "пожалуйста", "по месту требования"]
        if value not in list_of_reasons:
            raise serializers.ValidationError("цель должна быть одна из списка системы")
        return value

    def update(self, instance, validated_data):
        instance.date_of_changes = timezone.now().date()
        # new_comment = Comment(to_article=instance, author=author, coment="Изменено")
        # new_comment.save()
        return super().update(instance, validated_data)
