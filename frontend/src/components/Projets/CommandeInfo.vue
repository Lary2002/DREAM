<template>
    <br>
    <div class="pou">
        <div class="togboo">
            <p>{{ contenu.titre }}</p>
 
            <p class="nawv">{{ contenu.Nom }}</p>
            <p>{{ contenu.date }}</p>
            <p>{{ contenu.niveau }}</p>
            <img :src="image" alt="..." class="delete">
            <div>
            
            </div>
        </div>
    </div>
    <br>
</template>

<script>
export default {
    name: 'CommnadeInfo',
    props: {
        contenu: Object,
        image: String

    }

}
</script>

<style>
@import url(@/styles/style.css)
</style>