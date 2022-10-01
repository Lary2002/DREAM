from rest_framework import serializers
from .models import *

class MesureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mesure
        fields = "__all__"

class TypeMesureSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeMesure
        fields = "__all__"


class ValeurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Valeur
        fields = "__all__"


class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = "__all__"


class ProfessionnelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professionnel
        fields = "__all__"


class AdministrateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrateur
        fields = "__all__"


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"

class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = "__all__"

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class ContenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contenu
        fields = "__all__"

class AppreciationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appreciation
        fields = "__all__"

class CommandeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commande
        fields = "__all__"

class FactureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facture
        fields = "__all__"
