<template>

    <HearderProjet />
    <div class="seal">
        <div class="font">
            <h1 class="passe">Récupération d'un mot de passe</h1>
            <input type="email" name="mail" class="to" v-model="email" required placeholder="Adresse e-mail">
            <span v-if="msg.email" class="vert">{{ msg.email }}</span>
            <router-link :to="lien">
                <div class="on" v-on:click="show('Veuillez entrez un email valide')"> Réinitialiser le mot de passe
                </div>
            </router-link>
        </div>
    </div>
    <FooterProjet />
</template>

<script>
import FooterProjet from '../Projets/FooterProjet.vue';
import HearderProjet from './HearderProjet.vue';
export default {
    components: { HearderProjet, FooterProjet },

    data() {
        let lien = "#"
        return {
            email: '',
            msg: [],
            lien
        }
    },
    watch: {
        email(value) {
            this.email = value;
            this.validateEmail(value);
        }
    },

    methods: {
        validateEmail(value) {
            let reg = /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/
            
            if (reg.test(value)) {
                this.msg['email'] = '';
            } else {
                this.msg['email'] = 'Votre address E-mail est incorrecte!';
            }
        },

        show(message) {
            
            if(this.msg['email'] == '')
            {
                this.lien = "/panier";
            }
            else {
                alert(message); 
                this.lien = "/Reinitialiser";
            }

        }

    }

}
</script>

<style>
@import url(@/styles/style.css) ;


</style>