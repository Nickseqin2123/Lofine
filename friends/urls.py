from django.urls import path
from friends import views


app_name = 'friends'


urlpatterns = [
    path('friends-search/', views.SearchView.as_view(), name='search_friends'),
    path('friends-user/', views.friends_user, name='friends_user'),
    path('friends-people/<slug:tag_user>', views.OtherUserProfile.as_view(), name='user-click'),
    path('add_friend', views.add_friend, name='add_frind'),
    path('del_friend', views.del_friend, name='del_frind'),
]