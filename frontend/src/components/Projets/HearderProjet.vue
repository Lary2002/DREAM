<template>
  <header class="wrapper">
            <div class="fifa">
                <div style="display: flex;" class="chris">
                    <router-link to="/Accueil" class="acc">
                        <p> Accueil </p>
                    </router-link>
                    <router-link to="/Connexion" class="acc">
                        <p class="map">Inscription/Connexion</p>
                    </router-link>
                </div>
                <img src="@/assets/Logo2.png" alt="" class="ima">
                <div style="display: flex;">
                    <router-link to="/Styliste" class="noir">
                        <p class="tyl"> Styliste </p>
                    </router-link>
                    <router-link to="/Apropos" class="noir">
                        <p> Apropos </p>
                    </router-link>
                    
                    <router-link to="" class="noir">
                        <p> Discussion</p>
                    </router-link>
                    <router-link to="/Panier" class="noir">
                        <p> Panier</p>
                    </router-link>
                </div>
            </div>
        </header>
</template>

<script>
export default {

    

}
</script>

<style>

@import url(@/styles/style.css) 
</style>