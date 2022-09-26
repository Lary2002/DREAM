from django.db import models


#1 classe Mesure
class Mesure(models.Model):
    n_ieme_mesure = models.IntegerField(null=True)
    def __str__(self):
        return str(self.n_ieme_mesure)

#2 classe TypeMesure
class TypeMesure(models.Model):
    typeMesure = models.CharField(max_length=50)

#3 classe Valeur
class Valeur(models.Model):
    idMesure = models.ForeignKey(Mesure, null=True, on_delete=models.CASCADE)
    idTypeMesure = models.ForeignKey(TypeMesure, null=True, on_delete=models.CASCADE)
    valeur = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return str(self.idMesure)

    def __str__(self):
        return str(self.idTypeMesure)


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
    idMesure = models.ForeignKey(Mesure, null=True, on_delete=models.CASCADE)




#5 classe Message


#6 classe Professionnel
class Professionnel(models.Model):
    class Niveau(models.TextChoices):
        Mauvais= 'Mauvais'
        Moyen = 'Moyen'
        Bon = 'Bon'
        TresBon = 'TresBon'
        Excellent = 'Excellent'

    productivite = models.CharField(choices=Niveau.choices, max_length=20)
    idUtilisateur = models.ForeignKey(Utilisateur, null=True, on_delete=models.CASCADE)

#7 classe Administrateur
class Administrateur(Utilisateur):
    idUtilisateurs = models.ForeignKey(TypeMesure, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.idUtilisateurs)

#8 classe Catégorie
class Categorie(models.Model):
    categorie = models.CharField(max_length=30)
    img = models.FileField(upload_to= 'photos')


#9 classe Article
class Article(models.Model):
    libelle = models.CharField(max_length=30)
    prix = models.IntegerField()
    disponible = models.BooleanField()
    idCategorie = models.ForeignKey(Categorie, null=True, on_delete=models.CASCADE) 
    photo = models.FileField(upload_to='photos')
 

#10 classe Post 
class Post(models.Model):
    idProfessionnel = models.ForeignKey(Professionnel, null=True, on_delete=models.CASCADE)
    idArticle = models.ForeignKey(Article, null=True, on_delete=models.CASCADE)
    description = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return str(self.idProfessionnel)

    def __str__(self):
        return str(self.idArticle)


#11 classe Appreciation
class Appreciation(models.Model):
    idProfessionnel = models.ForeignKey(Professionnel, null=True, on_delete=models.CASCADE)
    idPost = models.ForeignKey(Post, null=True, on_delete=models.CASCADE)
    commentaire = models.TextField(null=True, blank=True)
    date = models.DateTimeField

    def __str__(self):
        return str(self.idPost)

    def __str__(self):
        return str(self.idProfessionnel)

#12 classe commande
class Commande(models.Model):
    nombreArticle = models.IntegerField()
    prix = models.IntegerField()
    date = models.DateTimeField()
    dateLivraison = models.DateTimeField()
    idUtilisateur = models.ForeignKey(Utilisateur, null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.idUtilisateur)

#13 class contenu
class Contenu(models.Model):
    idCommande = models.ForeignKey(Commande, null=True, on_delete=models.CASCADE)
    idArticle = models.ForeignKey(Article, null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.idArticle)

    def __str__(self):
        return str(self.idCommande)

#14 classe Facture
class Facture(models.Model):
    idUtilisateur = models.ForeignKey(Utilisateur, null=True, on_delete=models.CASCADE)
    idCommande = models.ForeignKey(Commande, null=True, on_delete=models.CASCADE)
    prix = models.IntegerField()
    date = models.DateTimeField()

    def __str__(self):
        return str(self.idCommande)

    def __str__(self):
        return str(self.idUtilisateur)
 