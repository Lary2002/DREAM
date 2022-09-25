<template>
  <div class="moi">
    <hearder-projet />

    <!-- <p>Formulaire de connexion</p> -->
    <form class="review-form" enctype="multipart/form-data">
      <div class="information">
        <img src="@/assets/user.svg" alt="" class="imag" />
        <div class="titre-input">
          <p class="titre"><i> Email:</i></p>
          <input
            type="email"
            name="mail"
            class="toto"
            required
            v-model="email"
            placeholder="you@gmail.com"
            pattern="(^[a-z0-9]+)@([a-z0-9])+(\.)([a-z]{2,4})"
          />
          <span v-if="msg.email" class="vert">{{ msg.email }} </span>
        </div>
        <div class="titre-input">
          <p class="titre"><i> Mot de passe:</i></p>
          <input
            type="password"
            class="toto"
            v-model="password"
            required
            name="mot de passe"
          />
          <span v-if="msg.password" class="vert">{{ msg.password }} </span>
          <br />
          <router-link :to="lien" class="none">
            <div class="bou" v-on:click="connexion()">
              <p>Se connecter</p>
            </div>
          </router-link>
          <router-link to="/Reinitialisation">
            <div class="ble">
              <p>Mot de passe oublé?</p>
            </div>
          </router-link>
          <hr />
          <div class="texe">
            <h2>
              <p>Vous n'avez pas encore un compte?</p>
            </h2>
            <router-link to="/Inscription" class="vo">
              <p class="vous">Inscrivez-vous!</p>
            </router-link>
          </div>
        </div>
      </div>
    </form>
    <br />
    <br />
  </div>
  <FooterProjet />
</template>

<script>
import axios from "axios";
import FooterProjet from "../Projets/FooterProjet.vue";
import HearderProjet from "../Projets/HearderProjet.vue";
import router from "@/router";
export default {
  components: {
    HearderProjet,
    FooterProjet,
  },

  data() {
    let lien = "#";
    return {
      email: "",
      msg: [],
      lien,
      password: "",
    };
  },
  mounted() {
    console.log(localStorage.getItem("page"));
    localStorage.setItem("page", "connexion");
  },
  watch: {
    email(value) {
      this.email = value;
      this.validateEmail(value);
    },

    password(value) {
      this.password = value;
      this.validatePassword(value);
    },
  },

  methods: {
    validateEmail(value) {
      let reg = /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/;

      if (reg.test(value)) {
        this.msg["email"] = "";
      } else {
        this.msg["email"] = "Votre address E-mail est incorrecte!";
      }
    },
    show(message) {
      if ((this.msg["email"] == "") & (this.msg["password"] == "")) {
        localStorage.setItem("connecter", "yes");

        if (localStorage.getItem("connecter") == "yes") {
          router.push("/Accueil");
        }
      } else {
        alert(message);
      }
    },

    validatePassword(value) {
      let difference = 10 - value.length;

      if (value.length < 10) {
        this.msg["password"] =
          "Sa doit contenir au moins dix caractère!" +
          difference +
          " caractères restantes";
      } else {
        this.msg["password"] = "";
      }
    },

    connexion() {
      let login = {
        email: this.email,
        password: this.password,
      };
      console.log(login);

      axios.get("http://127.0.0.1:8000/api/utilisateur").then((users) => {
        let logins = users.data;
        console.log(logins);
        let datas;
        let compter =0
        for (const donnee of logins) {
            let mail = donnee["email"];
            let passe = donnee["motDePasse"];
            datas = { mail, passe };
            console.log(datas);
            //let compter;
            if (datas.mail == login.email && datas.passe == login.password) {
                compter++;
            }
        }
        console.log(compter);
        if (compter >= 1) {
            alert("Connexion réussie");
        } else {
            alert("Connexion échouée");
        }
        
      });
    },
  },
};
</script>

<style>
@import url(@/styles/style.css);
</style>