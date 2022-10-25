from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from mystrictapplicationformapp.models import Reference
import json


class ReferenceModelTestCase(TestCase):
    """Тест ReferenceModel."""

    def setUp(self) -> None:
        """Переопределение подготовительных мер перед тестом."""
        print("SET UP!")
        self.reference = Reference(first_name="Андрей", last_name="Ищк", purpose="нужно", quantity=2)
        self.reference.save()
        return super().setUp()

    def test_reference_positive(self) -> None:
        """Положительный тест проверки модели Reference."""
        self.assertEqual("Андрей", self.reference.first_name)
        self.assertEqual("Ищк", self.reference.last_name)
        self.assertEqual("нужно", self.reference.purpose)
        self.assertEqual(2, self.reference.quantity)


class ViewTestCase(TestCase):
    """Тест представления с отправкой запроса в приложение."""

    def setUp(self) -> None:
        """Переопределение подготовительных мер перед тестом."""
        print("SET UP!")
        self.reference = Reference(first_name="Андрей", last_name="Ищк", purpose="нужно", quantity=2)
        self.reference.save()
        return super().setUp()

    def test_view_update_positive(self):
        """Выполнение запроса update."""
        url = reverse("reference-detail", args=[1])
        data = {
            "first_name": "Михаил",
            "last_name": "Ищк",
            "purpose": "нужно",
            "quantity": 2
        }
        response = self.client.put(url, data=json.dumps(data), content_type="application/json")
        # self.assertEqual(200, response.status_code)
        responseJson = response.json()
        self.assertEqual(data["first_name"], responseJson["first_name"])
        self.assertEqual(data["last_name"], responseJson["last_name"])
        self.assertEqual(data["purpose"], responseJson["purpose"])
        self.assertEqual(data["quantity"], responseJson["quantity"])
        self.assertEqual(str(timezone.now().date()), responseJson["date_of_changes"])

    def test_view_create_positive(self):
        """Выполнение запроса create."""
        url = reverse("reference-list")
        data = {
            "first_name": "Михаил",
            "last_name": "Ищк",
            "purpose": "нужно",
            "quantity": 2
        }
        response = self.client.post(url, data=json.dumps(data), content_type="application/json")
        responseJson = response.json()
        self.assertEqual(data["first_name"], responseJson["first_name"])
        self.assertEqual(data["last_name"], responseJson["last_name"])
        self.assertEqual(data["purpose"], responseJson["purpose"])
        self.assertEqual(data["quantity"], responseJson["quantity"])
        # self.assertIsNone(responseJson["date_of_changes"])
        self.assertEqual(str(timezone.now().date()), responseJson["date_of_changes"])