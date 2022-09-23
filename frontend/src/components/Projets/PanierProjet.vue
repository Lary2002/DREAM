<template>
  <hearder-projet />
  
  <div class="togbo" v-if="etat">

    <div class="executer">
      <div class="flex">

        <img src="@/assets/combin.jpg" alt="" class="niska">
        <div>
          <h2 class="conr">Short manche longue</h2>
          <br>
          <br>
          <h2 class="conr">Prix: 10000f</h2>
          <img src="@/assets/delete.svg" alt="" @click="bello" class="nis">
          <img src="@/assets/love.png" alt="" class="nis">
          <router-link to="/Accueil">
            <p class="fovivo">Ajouter</p>
          </router-link>
        </div>
      </div>
      <hr>
    </div>
    <div class="execut">
      <h2>
        Total Des Commandes
      </h2>
      <hr>
      <div class="floa">
        <p>
          Short manche longue
        </p>
        <div>
          <p>
            10000f
          </p>
        </div>
      </div>
      <hr>
      <div class="floa">
        <p>
          Total
        </p>
        <div>
          <p>
            10000f
          </p>
        </div>
      </div>

      <router-link to="/payement" class="noir">
        <div class="rovou">Passer la commande</div>
      </router-link>

    </div>

  </div>



  <div class="togbo" v-if="etat2">

    <div class="executer">
      <div class="flex">
        <router-link to="/Acceuil">
          <p class="fovivo">Ajouter</p>
        </router-link>
      </div>
    </div>
    <hr>
  </div>
  <div class="execut" v-if="etat2">
    <h2>
      Total Des Commandes
    </h2>
    <hr>
  </div>



  <div class="arder">
    <router-link to="/Commande" class="noir">
      <div class="rovi">Statistiques/Commandes</div>
    </router-link>
    <router-link to="" class="noir">
      <div class="rova">Livraison</div>
    </router-link>
  </div>
  <FooterProjet />
</template>

<script>
import { ref } from 'vue'
import FooterProjet from '../Projets/FooterProjet.vue';
import HearderProjet from './HearderProjet.vue';
export default {

  name: "PanierProjet",

  components: { HearderProjet, FooterProjet },

  setup() {
    let etat = ref(true)
    let etat2 = ref(false)

    const bello = function () {
      etat.value = false
      etat2.value = true
    }
    return {
      bello,
      etat,
      etat2,
    }
  }


}
</script>

<style>
@import url(@/styles/style.css);
</style>