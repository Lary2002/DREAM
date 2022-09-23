#from dataclasses import fields
from rest_framework import serializers
from .models import *

class MesureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mesure
        fields = []

class TypeMesureSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeMesure
        fields = ['typeMesure']


class ValeurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Valeur
        fields = ['valeur']


class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = ['nom', 'prenom', 'sexe', 'email', 'telephone', 'adresse', 'motDePasse', 'idMesure']



class ProfessionnelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professionnel
        fields = ['productivite']


class AdministrateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrateur
        fields = []


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['libelle', 'prix', 'vendu', 'patron', 'typeModel', 'photo']
        

class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = ['categorie']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['date', 'idProfessionnel', 'idArticle', 'description']


class ContenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contenu
        fields = ['idCommande', 'idArticle']


class AppreciationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appreciation
        fields = ['date', 'idPost', 'idProfessionnel', 'commentaire']

class CommandeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commande
        fields = ['nombreArticle', 'prix', 'date', 'idUtilisateur']


class FactureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facture
        fields = ['idCommande', 'prix', 'date', 'idUtilisateur']
