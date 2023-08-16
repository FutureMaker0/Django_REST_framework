from django.urls import path

from api import views


# api 처리하는 urls
# 이런 url들을 api end point라고 한다.
app_name = 'api'
urlpatterns = [
    path('post/list/', views.ApiPostLV.as_view(), name='post_list'),
    path('post/<int:pk>/', views.ApiPostDV.as_view(), name='post_detail'),
    path('catetag/', views.ApiCateTagView.as_view(), name='catetag_list'),
    path('like/<int:pk>/', views.ApiPostLikeDV.as_view(), name='post_like'),
    path('comment/create/', views.ApiCommentCV.as_view(), name='comment_create'),
]
