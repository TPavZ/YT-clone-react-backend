from django.urls import path
from comments import views

urlpatterns = [
    path('all/<str:video_id>/', views.get_all_comments),
    path('addcomment/', views.user_comments),
    path('replies/<int:comment_id>/', views.user_replies),
]