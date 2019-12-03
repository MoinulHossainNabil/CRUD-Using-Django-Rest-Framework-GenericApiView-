from django.urls import path

from .views import (
    ArticleView,
    SingleArticleView,
    UpdateSingleArticle,
    GetUpdateDelete,
    PostView
)


app_name = "articles"


urlpatterns = [
    path('articles/', ArticleView.as_view()),
    path('article/<int:pk>', SingleArticleView.as_view()),
    path('article/update/<int:pk>', UpdateSingleArticle.as_view()),
    path('article/delete/<int:pk>', GetUpdateDelete.as_view()),
    path('article/post/', PostView.as_view()),
]
