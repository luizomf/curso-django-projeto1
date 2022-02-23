from django.apps import AppConfig


class RecipesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'recipes'

    def ready(self, *args, **kwargs) -> None:
        import recipes.signals  # noqa
        super_ready = super().ready(*args, **kwargs)
        return super_ready
