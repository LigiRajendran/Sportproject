from.import views
from django.urls import path
app_name='sportsapp'
urlpatterns=[
    path('sports', views.sports, name='sports'),
    path('sports/<int:sports_id>', views.details, name='details'),
    path('add/', views.add, name='add'),
    path('update/<int:sports_id>', views.update, name='update'),
    path('delete/<int:sports_id>', views.delete, name='delete'),

]