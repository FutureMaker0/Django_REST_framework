# from django.urls import path, include
# from rest_framework import routers
# from api2.views import UserViewSet, PostViewSet, CommentViewSet


# # Routers provide an easy way of automatically determining the URL conf.

# # simplerouter, defaultrotuer가 있다.
# router = routers.DefaultRouter()
# router.register(r'user', UserViewSet)
# router.register(r'post', PostViewSet)
# router.register(r'comment', CommentViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
#     # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]

from django.urls import path
from api2 import views

urlpatterns = [
    path('post/', views.PostListAPIView.as_view(), name='post-list'),
    path('post/<int:pk>/', views.PostRetrieveAPIView.as_view(), name='post-detail'),
    path('comment/', views.CommentCreateAPIView.as_view(), name='comment-list'),
    path('post/<int:pk>/like/', views.PostLikeAPIView.as_view(), name='post-like'),
    path('catetag/', views.CateTagAPIView.as_view(), name='catetag'),
]