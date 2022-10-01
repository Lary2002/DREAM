"""dream_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from dream_back import views

#from dream_back import views

from django.conf.urls.static import static
from . import settings
from django.conf.urls import include

router = routers.DefaultRouter()
router.register(r'mesure', views.MesureView, 'mesure')
router.register(r'typemesure', views.TypeMesureView, 'typemesure')
router.register(r'valeur', views.ValeurView, 'valeur')
router.register(r'utilisateur', views.UtilisateurView, 'utilisateur')
router.register(r'professionnel', views.ProfessionnelView, 'professionnel')
router.register(r'post', views.PostView, 'post')
router.register(r'administrateur', views.AdministrateurView, 'administrateur')
router.register(r'appreciation', views.AppreciationView, 'appreciation')
router.register(r'categorie', views.CategorieView, 'categorie')
router.register(r'article', views.ArticleView, 'article')
router.register(r'contenu', views.ContenuView, 'contenu')
router.register(r'facture', views.FactureView, 'facture')
router.register(r'commande', views.CommandeView, 'commande')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('savefile/', views.saveFile)

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
