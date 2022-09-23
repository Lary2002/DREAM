<template>
  <HearderProjet />
  <div class="shell">
    <h1>Vous pouvez choisir un mode de payement!!!</h1>
  </div>
  <div class="sholl">
    <img src="@/assets/mtnmoney.jpg" alt="" class="wani">
    <img src="@/assets/moovmoney.png" alt="" class="wano">
    <img src="@/assets/cartebancaire.png" alt="" class="wane">
  </div>
  <FooterProjet />
</template>

<script>
import FooterProjet from '../Projets/FooterProjet.vue';
import HearderProjet from './HearderProjet.vue';
export default {
  components: { HearderProjet, FooterProjet },
  mounted() {
    console.log(localStorage.getItem('page'));
    localStorage.setItem('page', 'payement');
  }
}
</script>

<style>
.wani {
  height: 8%;
  width: 29%;
  cursor: pointer;
}

.wane {
  height: 80%;
  width: 29%;
  cursor: pointer;
  /* box-shadow: 7px 5px 5px darkgrey; */
}

.wano {
  height: 80%;
  width: 25%;
  cursor: pointer;
}

.sholl {
  display: flex;
  justify-content: space-between;
  margin-bottom: 30px;
}

.shell {
  margin-top: 10%;
  text-align: center;
}
</style>