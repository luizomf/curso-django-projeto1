from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from tag.models import Tag

from ..models import Recipe
from ..serializers import RecipeSerializer, TagSerializer


class RecipeAPIv2Pagination(PageNumberPagination):
    page_size = 2


class RecipeAPIv2List(ListCreateAPIView):
    queryset = Recipe.objects.get_published()
    serializer_class = RecipeSerializer
    pagination_class = RecipeAPIv2Pagination


class RecipeAPIv2Detail(RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.get_published()
    serializer_class = RecipeSerializer
    pagination_class = RecipeAPIv2Pagination

    def patch(self, request, *args, **kwargs):
        pk = kwargs.get('pk')

        recipe = self.get_queryset().filter(pk=pk).first()
        serializer = RecipeSerializer(
            instance=recipe,
            data=request.data,
            many=False,
            context={'request': request},
            partial=True,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            serializer.data,
        )


@api_view()
def tag_api_detail(request, pk):
    tag = get_object_or_404(
        Tag.objects.all(),
        pk=pk
    )
    serializer = TagSerializer(
        instance=tag,
        many=False,
        context={'request': request},
    )
    return Response(serializer.data)
