from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.utils import timezone
from mystrictapplicationformapp.models import Reference


class ReferenceSerializer(serializers.ModelSerializer):
    """Сериализатор по модели Reference."""

    # article_comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # Reference_comments = CommentSerializer(many=True)

    # author = serializers.CharField(source='author.username', default=None)
    # author = UserSerializer()

    class Meta:
        model = Reference
        # fields = "__all__"
        # fields = ("id", "title", "content", "author")
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

    # def validate_date_of_changes(self, value):
    #     if value not in list_of_reasons:
    #         raise serializers.ValidationError("цель должна быть одна из списка системы")
    #     return value
    #
    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation["_request_data_method"] = self.context["request"]._request.method
    #     representation["_request_data_url"] = self.context["request"]._request.path
    #     return representation

    # def create(self, validated_data):
    #     if not validated_data.get("author"):
    #         User = get_user_model()
    #         validated_data["author"] = User.objects.first()
    #     return super().create(validated_data)

    def update(self, instance):
        instance.date_of_changes = timezone.now()
        # new_comment = Comment(to_article=instance, author=author, coment="Изменено")
        # new_comment.save()
        return super().update(instance)
