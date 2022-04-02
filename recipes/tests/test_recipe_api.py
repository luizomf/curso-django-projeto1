from unittest.mock import patch

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

    @patch('recipes.views.api.RecipeAPIv2Pagination.page_size', new=7)
    def test_recipe_api_list_loads_correct_number_of_recipes(self):
        wanted_number_of_recipes = 7
        self.make_recipe_in_batch(qtd=wanted_number_of_recipes)

        response = self.client.get(
            reverse('recipes:recipes-api-list') + '?page=1'
        )
        qtd_of_loaded_recipes = len(response.data.get('results'))

        self.assertEqual(
            wanted_number_of_recipes,
            qtd_of_loaded_recipes
        )
