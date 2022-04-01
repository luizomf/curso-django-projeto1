from django.urls import reverse
from recipes.tests.test_recipe_base import RecipeMixin
from rest_framework import test


class RecipeAPIv2Test(test.APITestCase, RecipeMixin):
    def test_recipe_api_list_returns_status_code_200(self):
        api_url = reverse('recipes:recipes-api-list')
        response = self.client.get(api_url)
        self.assertEqual(
            response.status_code,
            200
        )
