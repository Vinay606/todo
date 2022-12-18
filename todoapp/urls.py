from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('delete/<str:pk>',views.delete,name='delete'),
    path('update/<str:pk>/',views.update,name='update'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('logout/',views.logout,name='logout'),
    path('login2/',views.login2,name='login2'),
    path('signup2/',views.signup2,name='signup2'),
    path('search/',views.search,name='search'),
    path('completed/<str:task_id>/',views.completed,name='completed')
]
