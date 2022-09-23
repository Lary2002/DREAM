<template>

    <div class="parent">
        <div class="features">
            <!-- <p>nom et image</p> -->
            <img :src="info_valeur.img" alt="" class="mode">
            <div class="prie">
                <div class="selector">
                    <h3> {{ info_valeur.name }} </h3>
                    <p class="prix"><span class="spa">{{ info_valeur.price }}f</span>
                    </p>
                </div>

            </div>
            <router-link :to="{ name: 'Decouvrir', params: { namePers: info_valeur.name } }" class="tm">
                <div>
                    <p class="tmc">
                        Découvrir
                    </p>
                </div>
            </router-link>
        </div>
    </div>



</template>

<script>
export default {
    name: "CombinaisonPhoto",
    props: {
        info_valeur: Object
    },


}
</script>

<style>
@import url(@/styles/style.css)
</style>