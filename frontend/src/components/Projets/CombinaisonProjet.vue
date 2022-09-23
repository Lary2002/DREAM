<template>
   
    <hearder-projet />
    <!-- <p>Affichage du nom et des catalogue</p> -->
    <h1 class="br">{{ nameCombin }}</h1>
    <div class="warp" v-for="(five_valeur, i) in data_valeur" :key="i">

        <combinaison-photo v-for="(photo, index) in five_valeur" :info_valeur="photo" :key="index" />
    </div>

<FooterProjet/>

</template>

<script>
import FooterProjet from '../Projets/FooterProjet.vue';
import HearderProjet from '../Projets/HearderProjet.vue';
import CombinaisonPhoto from '../Projets/CombinaisonPhoto.vue';
import BD from '@/BD.js'
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
import img16 from "@/assets/jupe5.jpeg"
import img17 from "@/assets/jupe4.jpeg"
import img18 from "@/assets/jupe3.jpeg"
import img19 from "@/assets/jupe2.jpeg"
import img20 from "@/assets/jupe1.jpeg"
import img21 from "@/assets/jupe0.jpeg"
export default {
    name: "CombinaisonProjetVue",
    props: {
        nameCombin: String,
    },
    components: {
        CombinaisonPhoto,
        HearderProjet,
        FooterProjet
    },

    setup(props) {
        class Photo {
            constructor(description, price, img, type) {
                this.name = description
                this.price = price
                this.img = img
                this.type = type

            }
        }
        //    <p> Tableau</p>

        let data_valeur = ref([]);
        let images = [img1, img2, img3, img4, img5, img6, img7, img8, img9, img10, img11, img12, img13, img14, img15, img16, img17, img18, img19, img20, img21]
        let i = 0
        const makeDatavaleur = () => {
            let five_valeur = [];
           // <p> personnalisation des photo</p>
            let nom_combin = RegExp(props.nameCombin);
            let photos_type = BD.filter(photo => nom_combin.test(photo.type));
            
            for (const Mode of photos_type) {

                const new_valeur = new Photo(Mode.name, Mode.price, images[i], Mode.type)
                i++

                if (five_valeur.length === 3) {
                    five_valeur.push(new_valeur);
                    data_valeur.value.push(five_valeur);
                    five_valeur = [];

                }
                else {
                    five_valeur.push(new_valeur);
                }

                

            }
            console.log(data_valeur)
        }
        onMounted(makeDatavaleur);

        return {
            data_valeur,
        }
    }

}
</script>

<style>
@import url(@/styles/style.css) 
</style>