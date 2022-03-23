from rest_framework import serializers


class RecipeSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=65)
    description = serializers.CharField(max_length=165)
    public = serializers.BooleanField(source='is_published')
    preparation = serializers.SerializerMethodField(
        method_name='any_method_name'
    )

    def any_method_name(self, recipe):
        return f'{recipe.preparation_time} {recipe.preparation_time_unit}'
