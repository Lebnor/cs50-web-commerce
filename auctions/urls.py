from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("all", views.show_all, name="all"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create, name="create"),
    path("myposts", views.my_posts, name="myposts"),
    path("category/<str:category>", views.category, name="category"),
    path("<str:uuid>/<str:title>", views.listing, name="listing")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
