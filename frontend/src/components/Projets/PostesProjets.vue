<template>
  <div class="mo">
          <div class="danx"><h1 >Bienvenue sur notre site!!!</h1></div>
          <div class="flex">
          <router-link to="/Connexion" class="pro">
            <p> Se Connecter </p>
          </router-link>
        </div>
      </div>
</template>

<script>
export default {

}
</script>

<style>

.danx{
  margin-bottom: 80px;
  text-align:center;
  font-size:3rem;
  color:white;
  padding-top:50px;
}

.mo {
  background-image: url("@/assets/top.jpg");
  height: 100vh;
  width: 100%;
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center;
}



.pro {
  margin-left: 40%;
  background-color: blue;
  color: black;
  font-weight: bold;
  width: 200px;
  border-radius: 30px;
  font-size: 1.3rem;
  cursor: pointer;
  text-decoration: none;
}


.flex {
  display: flex;
  text-align:center;

}

.muri {
  font-size: 1.4rem;
  width: 500px;
  margin: auto;
  padding: 15px;
  background-color: white;
}


</style>