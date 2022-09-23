<template>
  <!-- <p>Page de garde</p> -->
  <div class="dream">
    <div class="info">
      <div class="aubi">
        <img src="@/assets/trans.png" alt="" class="UAC">

        <div class="ceuil">
          <router-link to="/Accueil" class="boo">
            <div class="vi">Acceuil</div>
          </router-link>
          <router-link to="/Apropos" class="boo">
            <div> Apropos </div>
          </router-link>

          <div class="boo">Contacts</div>
        </div>
      </div>
      <div class="noi">
        <h2 style="text-align: justify;"> 
          Découvrez une nouvelle expérience digitale avec la mode.
        </h2>
      </div>
      <router-link to="/Accueil" class="button"> <i> Réjoignez-nous!</i>
      </router-link>
    </div>
  </div>
</template>

<script>
export default {
  mounted(){
    var lien=document.querySelector(".boo");
    lien.onclick=()=>{
      lien.style.color="blue";

    }

    
      // Animation sur le texte
        var text = document.querySelector(".noi h2");
        var content = text.innerHTML;
        text.innerHTML = "";
        text.style.letterSpacing = "8px";
        var i = 0, taille = content.length;
        function AnimeText() {
            if (i < taille) {
                text.innerHTML += `${content[i]}`;
                i += 1;
            }
            else {
                if (taille > 0) {
                    taille -= 1;
                    text.innerHTML = content.substring(0, taille);
                }
                else {
                    i = 0;
                    taille = content.length;
                }
            }
        }
        setInterval(AnimeText, 100);
    }


}
</script>
<style>
@import url(@/styles/style.css) 

</style>