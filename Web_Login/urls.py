from django.urls import path, include
from Web_Login import views

app_name = 'Web_Login'

urlpatterns = [
    path('signup/', views.sign_up, name='signup'),
    path('editprofile', views.edit_profile, name='edit_profile'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/<int:pk>/', views.profile_view, name='profile'),
    path('item/list/', views.listTool, name='listTool'),
    path('item/<int:pk>/', views.item_view, name='itempage'),
    path('messages/', views.user_messages, name='messages')
    # path('', views.profile_view.as_view(), name='user'),
]