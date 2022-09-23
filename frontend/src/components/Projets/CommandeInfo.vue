<template>
    <br>
    <div class="pou">
        <div class="flex">
            <p>{{ contenu.titre }}</p>
            <hr class="taille">
            <p>{{ contenu.Nom }}</p>
            <hr class="taille">
            <p>{{ contenu.date }}</p>
            <hr class="taille">
            <p>{{ contenu.niveau }}</p>
            <hr class="taille">
            <div>
                <img src="@/assets/delete.svg" alt="" class="delete">
            </div>
            <hr class="taille">
            <div>
                <img src="@/assets/check.svg" alt="" class="delete">
                <!-- {{ contenu.images }} -->
            </div>
            <hr class="taille">
            <div>
                <img src="@/assets/h.svg" alt="" class="delete">
            </div>
        </div>
    </div>
    <br>
</template>

<script>
export default {

    props: {
        contenu: Object
    }

}
</script>

<style>
@import url(@/styles/style.css)
</style>