from rest_framework import serializers
from .models import *

class MesureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mesure
        fields = ['n_ieme_mesure']

class TypeMesureSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeMesure
        fields = [ 'typeMesure' ]


class ValeurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Valeur
        fields = ['idMesure', 'idTypeMesure','valeur']


class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = ['nom', 'prenom', 'sexe', 'email', 'telephone','pays', 'photo', 'adresse', 'motDePasse', 'idMesure']



class ProfessionnelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professionnel
        fields = ['productivite', 'idUtilisateur']


class AdministrateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrateur
        fields = ['idUtilisateurs']


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['libelle', 'prix', 'disponible', 'idCategorie', 'photo']
        

class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = ['categorie']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['idProfessionnel', 'idArticle','description', 'date']


class ContenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contenu
        fields = ['idCommande', 'idArticle']


class AppreciationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appreciation
        fields = ['idProfessionnel', 'idPost', 'commentaire', 'date']

class CommandeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commande
        fields = ['nombreArticle', 'prix', 'date','dateLivraison', 'idUtilisateur']


class FactureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facture
        fields = ['idUtilisateur', 'idCommande', 'prix', 'date' ]
