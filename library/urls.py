from django.contrib import admin
from django.urls import path, include

from library.book.views import Custom404View

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('library.book.urls')),
]
handler404 = Custom404View.as_view()
