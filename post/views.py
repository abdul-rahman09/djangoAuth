from rest_framework import viewsets
from .models import MyPost
from .serializer import MyPostSerializer


# Create your views here.
class MyPostView(viewsets.ModelViewSet):
    queryset = MyPost.objects.all()
    serializer_class = MyPostSerializer

