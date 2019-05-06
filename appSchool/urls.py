-from django.urls import path
+from django.urls import include, path
from .views import RegistrationAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
+   path('api/', include('conduit.apps.authentication.urls', namespace='authentication')),
]