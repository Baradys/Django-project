from django.urls import path
from . import views

urlpatterns = [
    path('', views.FeedBackViewCreate.as_view()),
    path('done/', views.DoneView.as_view()),
    path('<int:pk>', views.FeedBackViewUpdate.as_view()),
    path('list/', views.ListFeedBackView.as_view()),
    path('list/<int:pk>', views.DetailFeedBack.as_view(), name='feedback_detail'),
]
