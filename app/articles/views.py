from rest_framework import viewsets, permissions, response

from articles.models import Article
from articles.serializers import ArticleAllSerializer
from articles.tasks import add_method


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleAllSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        add_method.delay(5, 6)
        return response.Response(data=serializer.data)
