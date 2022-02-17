# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/
from . import BASE_DIR

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True

LOCALE_PATHS = [
    BASE_DIR / 'locale',
]
