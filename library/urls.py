from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.urls.base import reverse_lazy
from django.conf.urls.static import static
from django.views.generic.base import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('book.urls')),

]
