<template>

    <div class="parent">
         <div class="features">         
        <img :src="info_valeur.img" alt="" class="mode">
       
        <div class="price">
            <div><h2 class="chunk">Catégorie:</h2></div>
            <div class="row">
                <p><i>{{ info_valeur.name }}</i></p>
                
            </div>
             </div>
            <router-link  :to="{name: 'Combinaison', params:{nameCombin: info_valeur.name }}" class="toma"><p>Voir plus</p></router-link> 
            <!-- <p class="time">
            {{info_valeur.id}}
        </p> -->
        </div>

    </div>
</template>

<script>
export default {
    name: "ModePhoto",
    props: {
        info_valeur: Object
    },

}
</script>


<style>

@import url(@/styles/style.css) ;
</style>