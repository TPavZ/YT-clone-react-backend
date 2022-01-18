from django.urls import path
from comments import views

urlpatterns = [
    path('all/<str:video_id>/', views.get_all_comments),
    path('addcomment/', views.user_comments),
    path('editcomment/<int:comment_id>/', views.update_comment),
    path('replies/<int:comment_id>/', views.user_replies),
    path('deletereply/<int:reply_id>/', views.delete_reply),
    path('deletecomment/<int:comment_id>/', views.delete_comment)
]