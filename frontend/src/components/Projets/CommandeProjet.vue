<template>
    <HearderProjet />
    <div class="dio">
        <div class="studio">
            <CommandeInfo :contenu="val" v-for="(val, i)  in champs" :key="i" />
        </div>
    </div>
    <FooterProjet />
</template>

<script>
import FooterProjet from '../Projets/FooterProjet.vue';
import HearderProjet from './HearderProjet.vue';
import CommandeInfo from './CommandeInfo.vue';
import img1 from "@/assets/check.svg"
import img2 from "@/assets/h.svg"
export default {
    components: { HearderProjet, CommandeInfo, FooterProjet },

    data() {

        let images = [img1,img2]
        
        return {
            champs: [
                {
                    Nom: "James Brodeur",
                    titre: "Good luck",
                    date: "07/07/2022",
                    niveau: "Encours",
                    images: img1,
                },

                {
                    Nom: "Emelie Tovas",
                    titre: "Chemise",
                    date: "22/11/2019",
                    niveau: "Encours",
                    img: images[img2],
                },
                {
                    Nom: "Gael Dupont",
                    titre: "Veste",
                    date: "20/09/2005",
                    niveau: "Archevé",
                    
                },
                {
                    Nom: "James Babes",
                    titre: "Demi saison",
                    date: "02/05/2009",
                    niveau: "Encours",
                    
                },
                {
                    Nom: "Enrique Brodeur",
                    titre: "Agbada",
                    date: "10/01/2010",
                    niveau: "Archevé",
                    
                },

            ]

        }
    }


}
</script>

<style>
@import url(@/styles/style.css)
</style>