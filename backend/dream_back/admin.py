from django.contrib import admin
from .models import *


admin.site.register(Mesure)             #1
admin.site.register(Utilisateur)        #2
admin.site.register(Professionnel)      #4
admin.site.register(Administrateur)     #5
admin.site.register(Post)               #6
admin.site.register(Appreciation)       #7
admin.site.register(Categorie)          #8
admin.site.register(Article)            #9
admin.site.register(Commande)           #10
admin.site.register(Contenu)            #11
admin.site.register(Facture)            #12
admin.site.register(TypeMesure)         #13
admin.site.register(Valeur)             #14


# Register your models here.
