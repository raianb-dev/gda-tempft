
from django.contrib import admin
from django.urls import path
from quiz import views as q_view
urlpatterns = [
    path('', q_view.init, name='quiz'),
    path('admin/', admin.site.urls),
]
