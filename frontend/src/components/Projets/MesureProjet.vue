<template>
                        <!-- <p>en tete</p> -->
        <div class="moi">
                <form class="review-form">
                        <hearder-projet/>
                        <div class="flexx">
                                <div class="boutton" type="submit" @click="action"><i> Homme</i></div>
                                <div class="boubon" type="submit" @click="faire"><i> Femme</i></div>
                        </div>
                        <br>
                        <div class=" infor" v-if="etat3">
                                <p class="titr"><i>Veuillez renseignez vos mesures</i></p>
                                <img src="@/assets/1587.jpg" alt="" class="imag">

                                <!-- <p>Femme</p> -->

                                <div>
                                        <div class="input-nom-prenom">
                                                <div class="titre-input1">
                                                        <p class="titre"><i> Dos:</i></p>
                                                        <input type="text" id="name" required class="toto"
                                                                name="Prenom">
                                                </div>
                                                <div class="titre-input2">
                                                        <p class="titre"> <i>Poitrine:</i></p>
                                                        <input type="text" class="toto" required name="Nom">

                                                </div>
                                        </div>
                                        <div class="input-nom-prenom">
                                                <div class="titre-input1">
                                                        <p class="titre"><i> Hauteur Poitrine:</i></p>
                                                        <input type="text" id="name" required class="toto"
                                                                name="Prenom">
                                                </div>
                                                <div class="titre-input2">
                                                        <p class="titre"> <i>Longueur sous seins:</i></p>
                                                        <input type="text" class="toto" required name="Nom">

                                                </div>
                                        </div>
                                        <div class="input-nom-prenom">
                                                <div class="titre-input1">
                                                        <p class="titre"><i> Sous seins:</i></p>
                                                        <input type="text" id="name" required class="toto"
                                                                name="Prenom">
                                                </div>
                                                <div class="titre-input2">
                                                        <p class="titre"> <i>Longueur taille:</i></p>
                                                        <input type="text" class="toto" required name="Nom">

                                                </div>
                                        </div>
                                        <div class="input-nom-prenom">
                                                <div class="titre-input1">
                                                        <p class="titre"><i> Ecart-Poitrine:</i></p>
                                                        <input type="text" id="name" required class="toto"
                                                                name="Prenom">
                                                </div>
                                                <div class="titre-input2">
                                                        <p class="titre"> <i>Ventre:</i></p>
                                                        <input type="text" class="toto" required name="Nom">

                                                </div>
                                        </div>
                                        <div class="input-nom-prenom">
                                                <div class="titre-input1">
                                                        <p class="titre"><i> Cou:</i></p>
                                                        <input type="text" id="name" required class="toto"
                                                                name="Prenom">
                                                </div>
                                                <div class="titre-input2">
                                                        <p class="titre"> <i>Longueur Manche:</i></p>
                                                        <input type="text" class="toto" required name="Nom">

                                                </div>
                                        </div>
                                        <div class="input-nom-prenom">
                                                <div class="titre-input1">
                                                        <p class="titre"><i> Tour de bras:</i></p>
                                                        <input type="text" id="name" required class="toto"
                                                                name="Prenom">
                                                </div>
                                                <div class="titre-input2">
                                                        <p class="titre"> <i>Longueur Corsage:</i></p>
                                                        <input type="text" class="toto" required name="Nom">

                                                </div>
                                        </div>
                                        <div class="input-nom-prenom">
                                                <div class="titre-input1">
                                                        <p class="titre"><i> Longueur chemise:</i></p>
                                                        <input type="text" id="name" required class="toto"
                                                                name="Prenom">
                                                </div>
                                                <div class="titre-input2">
                                                        <p class="titre"> <i>Longueur Bomba:</i></p>
                                                        <input type="text" class="toto" required name="Nom">

                                                </div>
                                        </div>
                                        <div class="input-nom-prenom">
                                                <div class="titre-input1">
                                                        <p class="titre"><i> Longueur goodluck:</i></p>
                                                        <input type="text" id="name" required class="toto"
                                                                name="Prenom">
                                                </div>
                                                <div class="titre-input2">
                                                        <p class="titre"> <i>Longueur Agbada:</i></p>
                                                        <input type="text" class="toto" required name="Nom">

                                                </div>
                                        </div>
                                        <div class="input-nom-prenom">
                                                <div class="titre-input1">
                                                        <p class="titre"><i> Largueur Agbada:</i></p>
                                                        <input type="text" id="name" required class="toto"
                                                                name="Prenom">
                                                </div>
                                                <div class="titre-input2">
                                                        <p class="titre"> <i>Longueur Veste:</i></p>
                                                        <input type="text" class="toto" required name="Nom">

                                                </div>
                                        </div>
                                        <div class="input-nom-prenom">
                                                <div class="titre-input1">
                                                        <p class="titre"><i> Cambrure:</i></p>
                                                        <input type="text" id="name" required class="toto"
                                                                name="Prenom">
                                                </div>
                                                <div class="titre-input2">
                                                        <p class="titre"> <i>Hanche pantalon:</i></p>
                                                        <input type="text" class="toto" required name="Nom">


                                                </div>
                                        </div>
                                        <div class="input-nom-prenom">
                                                <div class="titre-input1">
                                                        <p class="titre"><i> Hanche chemise:</i></p>
                                                        <input type="text" id="name" required class="toto"
                                                                name="Prenom">
                                                </div>
                                                <div class="titre-input2">
                                                        <p class="titre"> <i>Cuisse:</i></p>
                                                        <input type="text" class="toto" required name="Nom">


                                                </div>
                                        </div>
                                        <div class="input-nom-prenom">
                                                <div class="titre-input1">
                                                        <p class="titre"><i>Longueur genou:</i></p>
                                                        <input type="text" id="name" required class="toto"
                                                                name="Prenom">
                                                </div>
                                                <div class="titre-input2">
                                                        <p class="titre"> <i>Longeur pantalon:</i></p>
                                                        <input type="text" class="toto" required name="Nom">


                                                </div>
                                        </div>
                                        <div class="input-nom-prenom">
                                                <div class="titre-input1">
                                                        <p class="titre"><i>Tour genou:</i></p>
                                                        <input type="text" id="name" required class="toto"
                                                                name="Prenom">
                                                </div>
                                                <div class="titre-input2">
                                                        <p class="titre"> <i>Longeur robe:</i></p>
                                                        <input type="text" class="toto" required name="Nom">


                                                </div>
                                        </div>
                                        <div class="input-nom-prenom">
                                                <div class="titre-input1">
                                                        <p class="titre"><i>Longueur jupe:</i></p>
                                                        <input type="text" id="name" required class="toto"
                                                                name="Prenom">
                                                </div>
                                                <div class="titre-input2">
                                                        <p class="titre"> <i>Longeur Combinaison:</i></p>
                                                        <input type="text" class="toto" required name="Nom">


                                                </div>
                                        </div>
                                        <div class="input-nom-prenom">
                                                <div class="titre-input1">
                                                        <p class="titre"><i>Enfouchure:</i></p>
                                                        <input type="text" id="name" required class="toto"
                                                                name="Prenom">
                                                </div>
                                                <div class="titre-input2">
                                                        <p class="titre"> <i>Longeur taille dos:</i></p>
                                                        <input type="text" class="toto" required name="Nom">


                                                </div>
                                        </div>
                                        <div class="input-nom-prenom">
                                                <div class="titre-input1">
                                                        <p class="titre"><i>Longeur taille devant:</i></p>
                                                        <input type="text" id="name" required class="toto"
                                                                name="Prenom">
                                                </div>
                                                <div class="titre-input2">
                                                        <p class="titre"> <i>Mollet:</i></p>
                                                        <input type="text" class="toto" required name="Nom">


                                                </div>
                                        </div>


                                        <router-link to="/Connexion" class="none">
                                                <div class="buton"><i> Envoyez</i></div>
                                        </router-link>


                                </div>
                        </div>

                        <!-- <p>Homme</p> -->

                        <div class=" infor" v-if="etat4">
                                <p class="titr"><i>Veuillez renseignez vos mesures</i></p>
                                <img src="@/assets/1587.jpg" alt="" class="imag">
                                <div>
                                        <div class="input-nom-prenom">
                                                <div class="titre-input1">
                                                        <p class="titre"><i> Dos:</i></p>
                                                        <input type="text" id="name" required class="toto"
                                                                name="Prenom">
                                                </div>
                                                <div class="titre-input2">
                                                        <p class="titre"> <i>Longueur taille:</i></p>
                                                        <input type="text" class="toto" required name="Nom">

                                                </div>
                                        </div>

                                        <div class="input-nom-prenom">
                                                <div class="titre-input1">
                                                        <p class="titre"><i> Tour de bras:</i></p>
                                                        <input type="text" id="name" required class="toto"
                                                                name="Prenom">
                                                </div>
                                                <div class="titre-input2">
                                                        <p class="titre"> <i>Ventre:</i></p>
                                                        <input type="text" class="toto" required name="Nom">

                                                </div>
                                        </div>
                                        <div class="input-nom-prenom">
                                                <div class="titre-input1">
                                                        <p class="titre"><i> Cou:</i></p>
                                                        <input type="text" id="name" required class="toto"
                                                                name="Prenom">
                                                </div>
                                                <div class="titre-input2">
                                                        <p class="titre"> <i>Longueur Manche:</i></p>
                                                        <input type="text" class="toto" required name="Nom">

                                                </div>
                                        </div>
                                        <div class="input-nom-prenom">
                                                <div class="titre-input1">
                                                        <p class="titre"><i> Longueur chemise:</i></p>
                                                        <input type="text" id="name" required class="toto"
                                                                name="Prenom">
                                                </div>
                                                <div class="titre-input2">
                                                        <p class="titre"> <i>Longueur Bomba:</i></p>
                                                        <input type="text" class="toto" required name="Nom">

                                                </div>
                                        </div>
                                        <div class="input-nom-prenom">
                                                <div class="titre-input1">
                                                        <p class="titre"><i> Longueur goodluck:</i></p>
                                                        <input type="text" id="name" required class="toto"
                                                                name="Prenom">
                                                </div>
                                                <div class="titre-input2">
                                                        <p class="titre"> <i>Longueur Agbada:</i></p>
                                                        <input type="text" class="toto" required name="Nom">

                                                </div>
                                        </div>
                                        <div class="input-nom-prenom">
                                                <div class="titre-input1">
                                                        <p class="titre"><i> Largueur Agbada:</i></p>
                                                        <input type="text" id="name" required class="toto"
                                                                name="Prenom">
                                                </div>
                                                <div class="titre-input2">
                                                        <p class="titre"> <i>Longueur Veste:</i></p>
                                                        <input type="text" class="toto" required name="Nom">

                                                </div>
                                        </div>
                                        <div class="input-nom-prenom">
                                                <div class="titre-input1">
                                                        <p class="titre"><i> Cambrure:</i></p>
                                                        <input type="text" id="name" required class="toto"
                                                                name="Prenom">
                                                </div>
                                                <div class="titre-input2">
                                                        <p class="titre"> <i>Hanche pantalon:</i></p>
                                                        <input type="text" class="toto" required name="Nom">


                                                </div>
                                        </div>
                                        <div class="input-nom-prenom">
                                                <div class="titre-input1">
                                                        <p class="titre"><i> Hanche chemise:</i></p>
                                                        <input type="text" id="name" required class="toto"
                                                                name="Prenom">
                                                </div>
                                                <div class="titre-input2">
                                                        <p class="titre"> <i>Cuisse:</i></p>
                                                        <input type="text" class="toto" required name="Nom">


                                                </div>
                                        </div>
                                        <div class="input-nom-prenom">
                                                <div class="titre-input1">
                                                        <p class="titre"><i>Longueur genou:</i></p>
                                                        <input type="text" id="name" required class="toto"
                                                                name="Prenom">
                                                </div>
                                                <div class="titre-input2">
                                                        <p class="titre"> <i>Longeur pantalon:</i></p>
                                                        <input type="text" class="toto" required name="Nom">


                                                </div>
                                        </div>
                                        <div class="input-nom-prenom">
                                                <div class="titre-input1">
                                                        <p class="titre"><i>Tour genou:</i></p>
                                                        <input type="text" id="name" required class="toto"
                                                                name="Prenom">
                                                </div>
                                                <div class="titre-input2">
                                                        <p class="titre"> <i>Longeur robe:</i></p>
                                                        <input type="text" class="toto" required name="Nom">
                                                </div>
                                        </div>

                                        <div class="input-nom-prenom">
                                                <div class="titre-input1">
                                                        <p class="titre"><i>Enfouchure:</i></p>
                                                        <input type="text" id="name" required class="toto"
                                                                name="Prenom">
                                                </div>
                                                <div class="titre-input2">
                                                        <p class="titre"> <i>Longeur taille dos:</i></p>
                                                        <input type="text" class="toto" required name="Nom">


                                                </div>
                                        </div>
                                        <div class="input-nom-prenom">
                                                <div class="titre-input1">
                                                        <p class="titre"><i>Longeur taille devant:</i></p>
                                                        <input type="text" id="name" required class="toto"
                                                                name="Prenom">
                                                </div>
                                                <div class="titre-input2">
                                                        <p class="titre"> <i>Mollet:</i></p>
                                                        <input type="text" class="toto" required name="Nom">


                                                </div>
                                        </div>


                                        <router-link to="/Accueil" class="none">
                                                <div class="buton"><i> Envoyez</i></div>
                                        </router-link>


                                </div>
                        </div>

                </form>

<br>
    <br>
        </div>




<FooterProjet/>



</template>

<script>
import FooterProjet from '../Projets/FooterProjet.vue';
import HearderProjet from '../Projets/HearderProjet.vue'
import { ref } from "vue";
export default {
        name: "MesureProjet",
        components :{
        HearderProjet,
        FooterProjet
    },

        setup() {

                let etat3 = ref(true)
                let etat4 = ref(false)

                const action = function () {
                        etat3.value = false
                        etat4.value = true
                }
                const faire = function () {
                        etat3.value = true
                        etat4.value = false
                }

                return {
                        action,
                        faire,
                        etat3,
                        etat4
                }
        }
}
</script>

<style>
@import url(@/styles/style.css) ;
</style>