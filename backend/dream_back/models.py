from unicodedata import name
from django.db import models


#4 class utilisateur
class Utilisateur(models.Model):
    class Sexe(models.TextChoices):
        Feminin = 'Féminin'
        Masculin = 'Masculin'

    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    sexe = models.CharField(choices=Sexe.choices, max_length=100)
    telephone = models.IntegerField()
    pays = models.CharField(max_length=100)
    photo = models.FileField(upload_to='photos', null=True, blank=True)
    adresse = models.CharField(max_length=255)
    motDePasse = models.CharField(max_length=100)
    #idMesure = models.ForeignKey(Mesure, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return (self.email)

class Mesure(models.Model):
    auteur = models.ForeignKey(Utilisateur,null=True, blank=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.auteur)
#1 classe Mesure


#2 classe TypeMesure
class TypeMesure(models.Model):
    typeMesure = models.CharField(max_length=50)

    def __str__(self):
        return self.typeMesure

#3 classe Valeur
class Valeur(models.Model):
    idMesure = models.ForeignKey(Mesure, null=True, on_delete=models.CASCADE)
    idTypeMesure = models.ForeignKey(TypeMesure, null=True, on_delete=models.CASCADE)
    valeur = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return str(self.valeur)

  






#6 classe Professionnel
class Professionnel(Utilisateur):
    class Niveau(models.TextChoices):
        Mauvais= 'Mauvais'
        Moyen = 'Moyen'
        Bon = 'Bon'
        TresBon = 'TresBon'
        Excellent = 'Excellent'

    #ID = models.ForeignKey(Utilisateur, null=True, on_delete=models.CASCADE)
    productivite = models.CharField(choices=Niveau.choices, max_length=20)
    def __str__(self):
        return str(self.email)

#7 classe Administrateur
class Administrateur(Utilisateur):
    def __str__(self):
        return str(self.email)

#8 classe Catégorie
class Categorie(models.Model):
    categorie = models.CharField(max_length=30)
    img = models.FileField(upload_to= 'photos')
    def __str__(self):
        return self.categorie

#9 classe Article
class Article(models.Model):
    libelle = models.CharField(max_length=30)
    prix = models.IntegerField()
    disponible = models.BooleanField()
    idCategorie = models.ForeignKey(Categorie, null=True, on_delete=models.CASCADE) 
    photo = models.FileField(upload_to='photos')
 
    def __str__(self):
        return self.libelle
#10 classe Post 
class Post(models.Model):
    idProfessionnel = models.ForeignKey(Professionnel, null=True, on_delete=models.CASCADE)
    idArticle = models.ForeignKey(Article, null=True, on_delete=models.CASCADE)
    description = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return str(self.date)




#11 classe Appreciation
class Appreciation(models.Model):
    idProfessionnel = models.ForeignKey(Professionnel, null=True, on_delete=models.CASCADE)
    idPost = models.ForeignKey(Post, null=True, on_delete=models.CASCADE)
    commentaire = models.TextField(null=True, blank=True)
    date = models.DateTimeField

    def __str__(self):
        return str(self.date)


#12 classe commande
class Commande(models.Model):
    nombreArticle = models.IntegerField()
    prix = models.IntegerField()
    date = models.DateTimeField()
    dateLivraison = models.DateTimeField()
    idUtilisateur = models.ForeignKey(Utilisateur, null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.date)

#13 class contenu
class Contenu(models.Model):
    idCommande = models.ForeignKey(Commande, null=True, on_delete=models.CASCADE)
    idArticle = models.ForeignKey(Article, null=True, on_delete=models.CASCADE)
    



#14 classe Facture
class Facture(models.Model):
    idUtilisateur = models.ForeignKey(Utilisateur, null=True, on_delete=models.CASCADE)
    idCommande = models.ForeignKey(Commande, null=True, on_delete=models.CASCADE)
    prix = models.IntegerField()
    date = models.DateTimeField()

    def __str__(self):
        return str(self.date)


 