<template>
    <HearderProjet />
    <div class="dio">
        <div class="studio">
            <CommandeInfo :image="val.img" :contenu="val" v-for="(val, i)  in champs" :key="i" />
        </div>
    </div>
    <FooterProjet />
</template>

<script>
import FooterProjet from '../Projets/FooterProjet.vue';
import HearderProjet from './HearderProjet.vue';
import CommandeInfo from './CommandeInfo.vue';
import * as Images from '@/assets/belle'
export default {
    components: { HearderProjet, CommandeInfo, FooterProjet },

    data() {

        //let images = [img1,img2]
        
        return {
            Images,
            champs: [
                {
                    Nom: "James Brodeur",
                    titre: "Good luck",
                    date: "07/07/2022",
                    niveau: "Encours",
                    img: Images.img2,
                },

                {
                    Nom: "Emelie Tovas",
                    titre: "Chemise",
                    date: "22/11/2019",
                    niveau: "Encours",
                    img: Images.img1,
                },
                {
                    Nom: "Gael Dupont",
                    titre: "Veste",
                    date: "20/09/2005",
                    niveau: "Archevé",
                    img: Images.img1,
                },
                {
                    Nom: "James Babes",
                    titre: "Demi saison",
                    date: "02/05/2009",
                    niveau: "Encours",
                    img: Images.img2,
                },
                {
                    Nom: "Enrique Brodeur",
                    titre: "Agbada",
                    date: "10/01/2010",
                    niveau: "Archevé",
                    img: Images.img1,
                },

            ]

        }
    }


}
</script>

<style>
@import url(@/styles/style.css)
</style>