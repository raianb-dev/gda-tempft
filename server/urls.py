
from django.contrib import admin
from django.urls import path
from quiz import views as q_view
urlpatterns = [
    path('', q_view.init, name='quiz'),
    path('webhook/', q_view.webhook_view, name='webhook'),
    path('admin/', admin.site.urls),
]
