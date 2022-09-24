<template>
<div class="moi">
        <body class="body">
              <hearder-projet/>
                <!-- <p>page d'inscription</p> -->
                <form  class="review-form" enctype="multipart/form-data">
                <div class=" infor">
                   <p class="titr"><i>Inscrivez-vous!!!</i></p>
                    <img src="@/assets/user.svg" alt="" class="imag">
                    <div class="input-nom-prenom">
                        <div class="titre-input1">
                            <p class="titre"><i> Prenom:</i></p>
                            <input v-model="prenom" type="text" id="name" required class="toto" name="Prenom">
                        </div>
                        <div class="titre-input2">
                            <p class="titre"> <i>Nom:</i></p>
                            <input v-model="nom" type="text" class="toto" required name="Nom">

                        </div>
                    </div>
                    <div class="input-nom-prenom">
                        <div class="titre-input1">
                            <p class="titre"><i>Sexe:</i> </p>

                            <select v-model="sexe" name="Sexe" class="toto">
                                <option>-</option>
                                <option>Masculin</option>
                                <option >Féminin</option>
                            </select>
                        </div>
                        <div class="titre-input2">
                            <p class="titre"> <i>Photo (Facultatif):</i></p>
                            <input  type="file"  required name="photo">

                        </div>
                    </div>


                    <div class="titre-input">
                        <p class="titre"><i> Email:</i></p>
                        <input  type="email" name="mail" class="toto" v-model="email" required placeholder="you@gmail.com"
                            pattern="(^[a-z0-9]+)@([a-z0-9])+(\.)([a-z]{2,4})">
                            <span v-if="msg.email" class="vert">{{msg.email}}</span>

                    </div>


                    <div class="titre-input">
                        <p class="titre"><i> Adresse:</i></p>
                        <input v-model="adresse" type="texte" class="toto" required name="Adresse">

                    </div>
                    <div class="input-pays-numero">
                        <div class="pays">
                            <p class="titre"><i> Pays:</i></p>
                            <input v-model="pays" type="text" class="toto" required name="Pays">
                        </div>
                        <div class="numero">
                            <p class="titre"><i> Numero:</i></p>
                            <input v-model="telephone" type="text" class="toto" required name="Numero" placeholder="+229">


                        </div>
                    </div>
                    <div class="titre-input">
                        <p class="titre"><i> Mot de passe:</i></p>
                        <span v-if="msg.password" class="vert">{{msg.password}} </span>
                        <input type="password" name="mot de passe" v-model="password"  class="toto" required placeholder=".......">

                    </div>

                    <div class="titre-input">
                        <p class="titre"><i> Mot de passe(confirmation):</i></p>
                        <input type="password" class="toto" required name="Adresse" v-model="password"  placeholder=".........">

                    </div>
                    <router-link :to="lien" class="none">
                        <div class="buton" v-on:click="createUser()" > <i> S'inscrire </i> </div>
                    </router-link>
                    <div class="compte">
                        <p>Avez vous un compte?</p>
                    </div>
                    <router-link to="/Connexion" class="none">
                        <div class="bleu">
                            <p>Connexion</p>
                        </div>
                    </router-link>
                    <router-link to="/Accueil" class="none">
                        <div class="tex">
                            <p>Plus-tard</p>
                        </div>
                    </router-link>

                </div>


            </form>
        </body>
        
<br>
    <br>
    </div>
    <FooterProjet/>

</template>

<script>
import axios from 'axios'
import FooterProjet from '../Projets/FooterProjet.vue';
import HearderProjet from '../Projets/HearderProjet.vue'
export default {
    components :{
        HearderProjet,
        FooterProjet
    },

    data() {
        let lien = "#"
        return{
            email:'',
            msg: [],
            lien,
            password:'',
            nom: '',
            prenom: '',
            sexe: '',
            adresse: '',
            telephone: '',
            photo: '',
            pays: '',
            
        }
    },
    watch: {
        email(value){
            this.email = value;
            this.validateEmail(value);
        },

         password(value){
            this.password = value;
            this.validatePassword(value);
        }
    },

     methods:{
        validateEmail(value){
            let reg = /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/
            
            if(reg.test(value)){
                this.msg['email'] = '';
            } else{
                this.msg['email'] = 'Votre address E-mail est incorrecte!';
            }      
        },
        show(message) {
            
            if(this.msg['email']  & this.msg['password'] == '')
            {
                this.lien = "/mesure";
            }
            else {
                alert(message); 
                this.lien = "/Inscription";
                
            
            }

        },


        validatePassword(value){
            let difference = 10 - value.length;
            
            if(value.length<10){
                this.msg['password'] = 'Sa doit contenir au moins dix caractère, un chiffre et un symbole!' + difference +' caractères restantes' ;
            } else{
                this.msg['password'] = '';
            }      
        },

       createUser(){
            //let users = []
            let user = {
                nom: this.nom,
                prenom: this.prenom,
                sexe: this.sexe,
                adresse: this.adresse,
                telephone: this.telephone,
                motDePasse: this.password,
                photo: this.photo,
                pays: this.pays,
                email: this.email,
            }
            console.log(user);
            let utilisateurs
            var compter = 0
            axios.get('http://127.0.0.1:8000/api/utilisateur').then(users => {
                utilisateurs = users.data
                console.log(utilisateurs); 
                for (const utilisateur of utilisateurs) {
                    if (user.email === utilisateur.email){
                        compter++

                    }
                }
                if (compter>=1) {
                    alert('Cet utilisateur existe déja')
                }
                else{
                    axios.post('http://127.0.0.1:8000/api/utilisateur/', user)
                }
                })

       }

        
    }
}
</script>

<style>
 @import url(@/styles/style.css) ;
 
</style>
