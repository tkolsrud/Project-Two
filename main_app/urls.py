
from django.urls import path

# Add Profile below in future
from .views import Signup, Home, EditProfile
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    # path('accounts/profile/', Profile.as_view(), name="profile"),
    path('accounts/profile/', views.Profile.as_view(), name="profile"),
    path('accounts/signup/', Signup.as_view(), name="signup"),

    path('profile/', views.Profile.as_view(), name="profile"),

    #  path('', views.showslides),

    # Change routes to POSTS
    path('profile/<int:pk>/', views.PostDetail.as_view(), name="post_detail"),

    # path('profile/edit_profile/',
    #      views.EditProfile.as_view(), name="edit_profile"),

    path('profile/edit_profile/<int:pk>/',
         views.EditProfile.as_view(), name="edit_profile"),


]

# path('accounts/', include(django.contrib.auth.urls')),
