from django.urls import path
from . import views


urlpatterns = [
    path('contents/',views.get_contents,name="get_contents"),
    path('contents/create/',views.create_content,name="create_content"),
    path('contents/<int:pk>',views.content_detail,name="content_detail")
]