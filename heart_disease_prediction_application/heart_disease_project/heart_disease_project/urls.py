from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore
from django.http import HttpResponseRedirect # type: ignore

urlpatterns = [
    path('admin/', admin.site.urls),
    path('prediction/', include('prediction.urls')),
    path('', lambda request: HttpResponseRedirect('/prediction/')),  # Redirect root to prediction
]
