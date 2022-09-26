 <template>

    <hearder-projet />
    <!-- <p>Barre de recherhe</p> -->
    <div class="card">
        <h2 class="size">
            Nos Articles
        </h2>
        <div class="rivo">
            <input v-model="user_search_mode" type="text" class="cherche" name="recherche" placeholder="Recherche...">
            <router-link v-for="(Mode, i) in  search_photo" :key="i"
                :to="{ name: 'Combinaison', params: { nameCombin: Mode.name } }">
                <div class="riva">
                    <div class="riva-search">
                        <div class="riva-img">
                            <img :src="Mode.img" alt="" srcset="" class="mira">
                        </div>
                        <p>{{ Mode.name }} </p>
                    </div>

                </div>
            </router-link>
        </div>

        <br>
        <br>
    </div>
    <!-- <p>Affichage catalogue</p> -->
    <div class="warp" v-for="(five_valeur, i) in data_valeur " :key="i">
        <mode-photo v-for="(photo, index)  in five_valeur " :info_valeur="photo" :key="index" />
    </div>

    <FooterProjet />

</template>


<script>
import HearderProjet from '../Projets/HearderProjet.vue';
import FooterProjet from '../Projets/FooterProjet.vue';
import ModePhoto from '../Projets/ModePhoto.vue';
import BDD from '@/BDD.js'
import { onMounted, ref, watch } from 'vue'
import img1 from "@/assets/combine.jpg"
import img2 from "@/assets/Subway.jpg"
import img3 from "@/assets/Momo.jpg"
import img4 from "@/assets/p.jpg"
import img5 from "@/assets/pelagie.jpg"
import img6 from "@/assets/pelagi.jpg"
import img7 from "@/assets/long.jpg"
import img8 from "@/assets/mariage.jpg"
import img9 from "@/assets/femme.jpg"
import img10 from "@/assets/homme.jpg"
import img11 from "@/assets/veste.jpg"
import img12 from "@/assets/baba.jpg"
import img13 from "@/assets/food.png"
import img14 from "@/assets/tenue.jpg"
import img15 from "@/assets/mode.png"
import axios from 'axios';

export default {
    name: "AcceuilProjetVue",

    components: {
        ModePhoto,
        HearderProjet,
        FooterProjet
    },

    setup() {

        class Photo {
            constructor(description, price, img) {
                this.name = description
                this.price = price
                this.img = img


            }
        }
        // <p>tableau qui gere laffichage des images</p>
        let data_valeur = ref([]);
        let all_mode = [];
        let images = [img1, img2, img3, img4, img5, img6, img7, img8, img9, img10, img11, img12, img13, img14, img15]
        let i = 0
        const makeDatavaleur = () => {
            let five_valeur = [];
            for (const Mode of BDD) {

                const new_valeur = new Photo(Mode.name, Mode.price, images[i])
                i++


                all_mode.push(new_valeur);


                if (five_valeur.length === 3) {
                    five_valeur.push(new_valeur);
                    data_valeur.value.push(five_valeur);
                    five_valeur = [];
                }
                else {
                    five_valeur.push(new_valeur);
                }
            }

        };
        //User search mode
        let user_search_mode = ref('');
        let search_photo = ref([]);
        watch(user_search_mode, new_value => {

            let regex = RegExp(new_value.toLowerCase());

            let new_search_photo = all_mode.filter(Mode => regex.test(Mode.name.toLowerCase()));


            if (new_value == 0) {
                search_photo.value = []
            } else {
                search_photo.value = new_search_photo;
            }

            //  new_value==0 ? search_photo.value = [] : search_photo.value  =  new_search_photo.value ;
            console.log(search_photo);
        })
        axios.get('http://127.0.0.1:8000/api/categorie/').then(cat => console.log(cat.data))
        onMounted(makeDatavaleur);
        //return
        return {
            data_valeur,
            user_search_mode,
            search_photo,
        }
    },

}
</script>

<style>
@import url(@/styles/style.css)
</style>