from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import viewsets
from django.http.response import JsonResponse
from .models import *
from .serializers import *

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.core.files.storage import default_storage




class MesureView(viewsets.ModelViewSet):
    serializer_class = MesureSerializer
    queryset = Mesure.objects.all()


class TypeMesureView(viewsets.ModelViewSet):
    serializer_class = TypeMesureSerializer
    queryset = TypeMesure.objects.all()


class ValeurView(viewsets.ModelViewSet):
    serializer_class = ValeurSerializer
    queryset = Valeur.objects.all()


class UtilisateurView(viewsets.ModelViewSet):
    serializer_class = UtilisateurSerializer
    queryset = Utilisateur.objects.all()


class ProfessionnelView(viewsets.ModelViewSet):
    serializer_class = ProfessionnelSerializer
    queryset = Professionnel.objects.all()


class AdministrateurView(viewsets.ModelViewSet):
    serializer_class = AdministrateurSerializer
    queryset = Administrateur.objects.all()


class PostView(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class AppreciationView(viewsets.ModelViewSet):
    serializer_class = AppreciationSerializer
    queryset = Appreciation.objects.all()


class CategorieView(viewsets.ModelViewSet):
    serializer_class = CategorieSerializer
    queryset = Categorie.objects.all()


class ArticleView(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


class CommandeView(viewsets.ModelViewSet):
    serializer_class = CommandeSerializer
    queryset = Commande.objects.all()


class ContenuView(viewsets.ModelViewSet):
    serializer_class = ContenuSerializer
    queryset = Contenu.objects.all()


class FactureView(viewsets.ModelViewSet):
    serializer_class = FactureSerializer
    queryset = Facture.objects.all()


def saveFile(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name, safe= False)
    return JsonResponse(file_name, safe=False)




#registration
@csrf_exempt
def inscription(request):
    if request.method == "POST":
        datas = JSONParser().parse(request)
        nouvelUtilisateur = Utilisateur.objects.create(nom = datas['nom'], prenom = datas['prenom'] ,
         email = datas['email'], sexe = datas['sexe'] , telephone = datas['numero'] , pays = datas['pays'], adresse = datas['adresse'] ,
         motDePasse = datas['password'],  photo = datas['photo'])

        nouvelUtilisateur.save()
    return JsonResponse("Vous êtes bien enregistré!")

#connexion
@csrf_exempt
def connexion(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        user = authenticate(request, email = data['email'], passsword = data['password'])
        if user is not None and user.is_active:
            login(request, user)
            return JsonResponse( "Bienvenu")
        else:
            return JsonResponse("Identifiants incorrects, Veuillez réessayer")

#déconnexion
@login_required
def deconnexion(request):
    logout(request)
     
 