from .serializers import ArticleSerializer

from .models import Article, Author

from rest_framework import mixins

from django.shortcuts import get_object_or_404, render

from rest_framework.mixins import ListModelMixin, CreateModelMixin

from rest_framework.generics import (
    GenericAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    RetrieveUpdateDestroyAPIView,
    GenericAPIView
    )


class ArticleView(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def perform_create(self, serializer):
        author = get_object_or_404(Author, id=self.request.data.get('author_id'))
        return serializer.save(author=author)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

# for getting a single element by id

class SingleArticleView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

# for updating a single element by id 

class UpdateSingleArticle(RetrieveUpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

# get , delete, update a single element by id

class GetUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    
# for posting a single element

class PostView(mixins.CreateModelMixin, GenericAPIView, mixins.ListModelMixin):

    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)