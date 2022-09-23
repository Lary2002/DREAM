<template>
  <HearderProjet/>
  <div>
    <p class="site">DreamSite est une application réaliser pour la digitalisation de la mode. Grace a cet applications ,
      vous pouvez faire des commandes tenue chez n'importe qu'elle styliste et vous faire livré en un temps record quel
      que soit votre situation géographique. </p>
  </div>
  <FooterProjet/>
</template>

<script>
import HearderProjet from './HearderProjet.vue';
import FooterProjet from '../Projets/FooterProjet.vue';
export default {
    components: { HearderProjet, FooterProjet }
}
</script>

<style>

@import url(@/styles/style.css) ;

</style>