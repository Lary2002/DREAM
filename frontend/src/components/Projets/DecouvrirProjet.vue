<template>
    <hearder-projet />
    <div class="flex">
        <div class="br">
            <img :src="data_valeur.img" class="muha">
            <!-- <carossel-projet/> -->
            
    </div>
<div>
    <div class="voi">
        <h1>{{namePers }}</h1>
        <p class="sité"> Tenue pour des sorties simple comme la plage,les diner entre amis. </p>
        <h2 class="cour">Prix: <i>{{data_valeur.price}}f </i></h2>
        <br>
        <br>
    </div>
    <div class="julie" @click="mum" v-if="etat7"><i>Ajouter au Panier</i>
    </div>
    <!-- <p>Panier</p> -->
    
    <router-link to="/panier" class="ju">
        <div v-on:click="addToCart(data_valeur)">
            <div class="julie" v-if="etat8">
                <i>Voir le panier</i>
            </div>
        </div>
    </router-link>
    <div v-if="cart.length > 0">
        <h2>Panier</h2>
    </div>
    </div>
    </div>
    <div>
        <h2 class="mix">Détaille par rapport à la livraison </h2>
        <p>Après vos commandes , vous avez la possibilité d'etre livré 7 jour après votre commande quelque soit votre
            position géographique grce à vos renseignement sur le formulaire.
            Et si après la livraison vous avez besoin de modifier quoi que ce soit sur la tenue, vous pouvez contacter
            le styliste ayant pris en compte votre commande. Cette requete sera pris en compte si et seulement si après
            la livraison vous n'avez pas fais une délai de 28jours.
        </p>
    </div>
    <br>
    <br>
<FooterProjet/>
</template>

<script>
// import cookies from 'vue-cookies'
import FooterProjet from '../Projets/FooterProjet.vue';
import HearderProjet from '../Projets/HearderProjet.vue'
import BD from '@/BD.js'
// import CarosselProjet from '../Projets/CarosselProjet.vue'
import { onMounted, ref } from 'vue'
import img1 from "@/assets/combinaison.jpg"
import img2 from "@/assets/combinaiso.jpg"
import img3 from "@/assets/combinais.jpg"
import img4 from "@/assets/combinai.jpg"
import img5 from "@/assets/combina.jpg"
import img6 from "@/assets/combin.jpg"
import img7 from "@/assets/combi.jpg"
import img8 from "@/assets/comb.jpg"
import img9 from "@/assets/com.jpg"
import img10 from "@/assets/co.jpg"
import img11 from "@/assets/c.jpg"
import img12 from "@/assets/pantalon.jpg"
import img13 from "@/assets/pant.jpg"
import img14 from "@/assets/pantal.jpg"
import img15 from "@/assets/panta.jpg"
// import { container } from 'webpack'


export default {
    props: {
        namePers: String,
    },
    components:{
            // CarosselProjet,
            HearderProjet,
            FooterProjet
    },
   

    data: () => {

        return {
            cart: []
        }
    },
    methodes: {
        addToCart(info_valeur) {
            for (let i = 0; i < this.cart.length; i++) {
                if (this.cart[i].name === info_valeur.name) {
                    return this.cart[i].quantity++
                }
            }
            this.cart.push({
                img: info_valeur.img,
                name: info_valeur.name,
                price: info_valeur.price,
                quantity: 1


            })
            // console.log(info_valeur);
        }

    },

    setup(props) {
        console.log(props)
        class Photo {
            constructor(description, price, img, id) {
                this.name = description
                this.price = price
                this.img = img
                this.id = id

            }
        }
        //    <p> Tableau</p>

        let data_valeur = ref([]);
        let images = [img1, img2, img3, img4, img5, img6, img7, img8, img9, img10, img11, img12, img13, img14, img15]
        //let i = 0
        const makeDatavaleur = () => {

            // <p> personnalisation des photo</p>
            let id_combin = RegExp(props.namePers);
            let photos_id = BD.filter(photo => id_combin.test(photo.name));

            for (const Mode of photos_id) {
                let img = images.filter(image => images.indexOf(image)+1 == Mode.id)
                data_valeur.value = new Photo(Mode.name, Mode.price, img[0], Mode.id)



            }
            console.log(data_valeur.value)
        }
        onMounted(makeDatavaleur);

        let etat7 = ref(true)
        let etat8 = ref(false)

        const mum = function () {
            etat7.value = false
            etat8.value = true
        }
        return {
            mum,
            etat7,
            etat8,
            data_valeur,


        }

    }
    




}
</script>

<style>

@import url(@/styles/style.css) 
</style>