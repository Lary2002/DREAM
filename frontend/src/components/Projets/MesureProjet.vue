<template>
		<!-- <p>en tete</p> -->
<div class="moi">
<form class="review-form">
	<hearder-projet/>
	<div class="flexx">
			<div class="boutton" type="submit" @click="action"><i> Homme</i></div>
			<div class="boubon" type="submit" @click="faire"><i> Femme</i></div>
	</div>
	<br>
	<div class=" infor" v-if="etat3">
			<p class="titr"><i>Veuillez renseignez vos mesures</i></p>
			<img src="@/assets/1587.jpg" alt="" class="imag">

			<!-- <p>Femme</p> -->

		<div>
				<div class="input-nom-prenom">
						<div class="titre-input1">
								<p class="titre"  ><i> Dos:</i></p>
								<input type="number" v-model="dos" id="name" required class="toto"
										name="Prenom">
						</div>
						<div class="titre-input2">
								<p class="titre"> <i>Poitrine:</i></p>
								<input type="number" v-model="poitrine" class="toto" required name="Nom">

						</div>
				</div>
				<div class="input-nom-prenom">
						<div class="titre-input1">
								<p class="titre"><i> Hauteur Poitrine:</i></p>
								<input v-model="haut_poitrine" type="number" id="name" required class="toto"
										name="Prenom">
						</div>
						<div class="titre-input2">
								<p class="titre"> <i>Longueur sous seins:</i></p>
								<input v-model="long_sous_seins" type="number" class="toto" required name="Nom">

						</div>
				</div>
				<div class="input-nom-prenom">
						<div class="titre-input1">
								<p class="titre"><i> Sous seins:</i></p>
								<input v-model="sous_seins" type="number" id="name" required class="toto"
										name="Prenom">
						</div>
						<div class="titre-input2">
								<p class="titre"> <i>Longueur taille:</i></p>
								<input v-model="long_taille" type="number" class="toto" required name="Nom">

						</div>
				</div>
				<div class="input-nom-prenom">
						<div class="titre-input1">
								<p class="titre"><i> Ecart-Poitrine:</i></p>
								<input v-model="ecart_poitrine" type="number" id="name" required class="toto"
										name="Prenom">
						</div>
						<div class="titre-input2">
								<p class="titre"> <i>Ventre:</i></p>
								<input v-model="ventre" type="number" class="toto" required name="Nom">

						</div>
				</div>
				<div class="input-nom-prenom">
						<div class="titre-input1">
								<p class="titre"><i> Cou:</i></p>
								<input v-model="cou" type="number" id="name" required class="toto"
										name="Prenom">
						</div>
						<div class="titre-input2">
								<p class="titre"> <i>Longueur Manche:</i></p>
								<input v-model="long_manche" type="number" class="toto" required name="Nom">

						</div>
				</div>
				<div class="input-nom-prenom">
						<div class="titre-input1">
								<p class="titre"><i> Tour de bras:</i></p>
								<input v-model="tour_bras" type="number" id="name" required class="toto"
										name="Prenom">
						</div>
						<div class="titre-input2">
								<p class="titre"> <i>Longueur Corsage:</i></p>
								<input v-model="long_corsage" type="number" class="toto" required name="Nom">

						</div>
				</div>
				<div class="input-nom-prenom">
						<div class="titre-input1">
								<p class="titre"><i> Longueur chemise:</i></p>
								<input v-model="long_chemise" type="number" id="name" required class="toto"
										name="Prenom">
						</div>
						<div class="titre-input2">
								<p class="titre"> <i>Longueur Bomba:</i></p>
								<input v-model="long_bomba" type="number" class="toto" required name="Nom">

						</div>
				</div>
				<div class="input-nom-prenom">
						<div class="titre-input1">
								<p class="titre"><i> Longueur goodluck:</i></p>
								<input v-model="long_goodluck" type="number" id="name" required class="toto"
										name="Prenom">
						</div>
						<div class="titre-input2">
								<p class="titre"> <i>Longueur Agbada:</i></p>
								<input v-model="long_agbada" type="number" class="toto" required name="Nom">

						</div>
				</div>
				<div class="input-nom-prenom">
						<div class="titre-input1">
								<p class="titre"><i> Largueur Agbada:</i></p>
								<input v-model="larg_abgada" type="number" id="name" required class="toto"
										name="Prenom">
						</div>
						<div class="titre-input2">
								<p class="titre"> <i>Longueur Veste:</i></p>
								<input v-model="long_veste" type="number" class="toto" required name="Nom">

						</div>
				</div>
				<div class="input-nom-prenom">
						<div class="titre-input1">
								<p class="titre"><i> Cambrure:</i></p>
								<input v-model="cambrure" type="number" id="name" required class="toto"
										name="Prenom">
						</div>
						<div class="titre-input2">
								<p class="titre"> <i>Hanche pantalon:</i></p>
								<input v-model="hanche_pantalon" type="number" class="toto" required name="Nom">


						</div>
				</div>
				<div class="input-nom-prenom">
						<div class="titre-input1">
								<p class="titre"><i> Hanche chemise:</i></p>
								<input v-model="hanche_chemise" type="number" id="name" required class="toto"
										name="Prenom">
						</div>
						<div class="titre-input2">
								<p class="titre"> <i>Cuisse:</i></p>
								<input v-model="cuisse" type="number" class="toto" required name="Nom">


						</div>
				</div>
				<div class="input-nom-prenom">
						<div class="titre-input1">
								<p class="titre"><i>Longueur genou:</i></p>
								<input v-model="long_genou" type="number" id="name" required class="toto"
										name="Prenom">
						</div>
						<div class="titre-input2">
								<p class="titre"> <i>Longeur pantalon:</i></p>
								<input v-model="long_pantalon" type="number" class="toto" required name="Nom">


						</div>
				</div>
				<div class="input-nom-prenom">
						<div class="titre-input1">
								<p class="titre"><i>Tour genou:</i></p>
								<input v-model="tour_genou" type="number" id="name" required class="toto"
										name="Prenom">
						</div>
						<div class="titre-input2">
								<p class="titre"> <i>Longeur robe:</i></p>
								<input v-model="long_robe" type="number" class="toto" required name="Nom">


						</div>
				</div>
				<div class="input-nom-prenom">
						<div class="titre-input1">
								<p class="titre"><i>Longueur jupe:</i></p>
								<input v-model="long_jupe" type="number" id="name" required class="toto"
										name="Prenom">
						</div>
						<div class="titre-input2">
								<p class="titre"> <i>Longeur Combinaison:</i></p>
								<input v-model="long_combine" type="number" class="toto" required name="Nom">


						</div>
				</div>
				<div class="input-nom-prenom">
						<div class="titre-input1">
								<p class="titre"><i>Enfouchure:</i></p>
								<input v-model="enfourchure" type="number" id="name" required class="toto"
										name="Prenom">
						</div>
						<div class="titre-input2">
								<p class="titre"> <i>Longeur taille dos:</i></p>
								<input v-model="long_taille_dos" type="number" class="toto" required name="Nom">


						</div>
				</div>
				<div class="input-nom-prenom">
						<div class="titre-input1">
								<p class="titre"><i>Longeur taille devant:</i></p>
								<input v-model="long_taille_devant" type="number" id="name" required class="toto"
										name="Prenom">
						</div>
						<div class="titre-input2">
								<p class="titre"> <i>Mollet:</i></p>
								<input v-model="mollet" type="number" class="toto" required name="Nom">


						</div>
				</div>


				<router-link to="/Connexion" class="none">
						<div class="buton" v-on:click="valeurRecord()" ><i> Envoyez</i></div>
				</router-link>


		</div>
</div>

<!-- <p>Homme</p> -->

<div class=" infor" v-if="etat4">
		<p class="titr"><i>Veuillez renseignez vos mesures</i></p>
		<img src="@/assets/1587.jpg" alt="" class="imag">
		<div>
				<div>
				<div class="input-nom-prenom">
						<div class="titre-input1">
								<p class="titre"  ><i> Dos:</i></p>
								<input type="number" v-model="dos" id="name" required class="toto"
										name="Prenom">
						</div>
						<div class="titre-input2">
								<p class="titre"> <i>Poitrine:</i></p>
								<input type="number" v-model="poitrine" class="toto" required name="Nom">

						</div>
				</div>
				<div class="input-nom-prenom">
						<div class="titre-input1">
								<p class="titre"><i> Hauteur Poitrine:</i></p>
								<input v-model="haut_poitrine" type="number" id="name" required class="toto"
										name="Prenom">
						</div>
						
						<div class="titre-input2">
								<p class="titre"> <i>Longueur taille:</i></p>
								<input v-model="long_taille" type="number" class="toto" required name="Nom">

						</div>
				</div>
				<div class="input-nom-prenom">
						<div class="titre-input1">
								<p class="titre"><i> Ecart-Poitrine:</i></p>
								<input v-model="ecart_poitrine" type="number" id="name" required class="toto"
										name="Prenom">
						</div>
						<div class="titre-input2">
								<p class="titre"> <i>Ventre:</i></p>
								<input v-model="ventre" type="number" class="toto" required name="Nom">

						</div>
				</div>
				<div class="input-nom-prenom">
						<div class="titre-input1">
								<p class="titre"><i> Cou:</i></p>
								<input v-model="cou" type="number" id="name" required class="toto"
										name="Prenom">
						</div>
						<div class="titre-input2">
								<p class="titre"> <i>Longueur Manche:</i></p>
								<input v-model="long_manche" type="number" class="toto" required name="Nom">

						</div>
				</div>
				<div class="input-nom-prenom">
						<div class="titre-input1">
								<p class="titre"><i> Tour de bras:</i></p>
								<input v-model="tour_bras" type="number" id="name" required class="toto"
										name="Prenom">
						</div>
						<div class="titre-input2">
								<p class="titre"> <i>Longueur Corsage:</i></p>
								<input v-model="long_corsage" type="number" class="toto" required name="Nom">

						</div>
				</div>
				<div class="input-nom-prenom">
						<div class="titre-input1">
								<p class="titre"><i> Longueur chemise:</i></p>
								<input v-model="long_chemise" type="number" id="name" required class="toto"
										name="Prenom">
						</div>
						<div class="titre-input2">
								<p class="titre"> <i>Longueur Bomba:</i></p>
								<input v-model="long_bomba" type="number" class="toto" required name="Nom">

						</div>
				</div>
				<div class="input-nom-prenom">
						<div class="titre-input1">
								<p class="titre"><i> Longueur goodluck:</i></p>
								<input v-model="long_goodluck" type="number" id="name" required class="toto"
										name="Prenom">
						</div>
						<div class="titre-input2">
								<p class="titre"> <i>Longueur Agbada:</i></p>
								<input v-model="long_agbada" type="number" class="toto" required name="Nom">

						</div>
				</div>
				<div class="input-nom-prenom">
						<div class="titre-input1">
								<p class="titre"><i> Largueur Agbada:</i></p>
								<input v-model="larg_abgada" type="number" id="name" required class="toto"
										name="Prenom">
						</div>
						<div class="titre-input2">
								<p class="titre"> <i>Longueur Veste:</i></p>
								<input v-model="long_veste" type="number" class="toto" required name="Nom">

						</div>
				</div>
				<div class="input-nom-prenom">
						<div class="titre-input1">
								<p class="titre"><i> Cambrure:</i></p>
								<input v-model="cambrure" type="number" id="name" required class="toto"
										name="Prenom">
						</div>
						<div class="titre-input2">
								<p class="titre"> <i>Hanche pantalon:</i></p>
								<input v-model="hanche_pantalon" type="number" class="toto" required name="Nom">


						</div>
				</div>
				<div class="input-nom-prenom">
						<div class="titre-input1">
								<p class="titre"><i> Hanche chemise:</i></p>
								<input v-model="hanche_chemise" type="number" id="name" required class="toto"
										name="Prenom">
						</div>
						<div class="titre-input2">
								<p class="titre"> <i>Cuisse:</i></p>
								<input v-model="cuisse" type="number" class="toto" required name="Nom">


						</div>
				</div>
				<div class="input-nom-prenom">
						<div class="titre-input1">
								<p class="titre"><i>Longueur genou:</i></p>
								<input v-model="long_genou" type="number" id="name" required class="toto"
										name="Prenom">
						</div>
						<div class="titre-input2">
								<p class="titre"> <i>Longeur pantalon:</i></p>
								<input v-model="long_pantalon" type="number" class="toto" required name="Nom">


						</div>
				</div>
				<div class="input-nom-prenom">
						<div class="titre-input1">
								<p class="titre"><i>Tour genou:</i></p>
								<input v-model="tour_genou" type="number" id="name" required class="toto"
										name="Prenom">
						</div>
						<div class="titre-input2">
								<p class="titre"> <i>Longeur robe:</i></p>
								<input v-model="long_robe" type="number" class="toto" required name="Nom">


						</div>
				</div>
				<div class="input-nom-prenom">
						<div class="titre-input1">
								<p class="titre"><i>Longueur jupe:</i></p>
								<input v-model="long_jupe" type="number" id="name" required class="toto"
										name="Prenom">
						</div>
						<div class="titre-input2">
								<p class="titre"> <i>Longeur Combinaison:</i></p>
								<input v-model="long_combine" type="number" class="toto" required name="Nom">


						</div>
				</div>
				<div class="input-nom-prenom">
						<div class="titre-input1">
								<p class="titre"><i>Enfouchure:</i></p>
								<input v-model="enfourchure" type="number" id="name" required class="toto"
										name="Prenom">
						</div>
						<div class="titre-input2">
								<p class="titre"> <i>Longeur taille dos:</i></p>
								<input v-model="long_taille_dos" type="number" class="toto" required name="Nom">


						</div>
				</div>
				<div class="input-nom-prenom">
						<div class="titre-input1">
								<p class="titre"><i>Longeur taille devant:</i></p>
								<input v-model="long_taille_devant" type="number" id="name" required class="toto"
										name="Prenom">
						</div>
						<div class="titre-input2">
								<p class="titre"> <i>Mollet:</i></p>
								<input v-model="mollet" type="number" class="toto" required name="Nom">


						</div>
				</div>


				<router-link to="/Accueil" class="none">
						<div class="buton" v-on:click="valeurRecord()"><i> Envoyez</i></div>
				</router-link>
			</div>

		</div>
	</div>

</form>

<br>
	<br>
		</div>




<FooterProjet/>



</template>

<script>
import FooterProjet from '../Projets/FooterProjet.vue';
import HearderProjet from '../Projets/HearderProjet.vue'
import { ref } from "vue";
import axios from 'axios';
export default {
	name: "MesureProjet",
	components :{
	HearderProjet,
	FooterProjet
	},

	data (){

		return {
			dos: '',
			poitrine: '',
			haut_poitrine: '',
			long_sous_seins: '',
			sous_seins: '',
			long_taille: '',
			ecart_poitrine: '',
			ventre: '',
			cou: '',
			long_manche: '',
			tour_bras: '',
			long_corsage: '',
			long_chemise: '',
			long_bomba: '',
			long_goodluck: '',
			long_agbada: '',
			larg_agbada: '',
			long_vest: '',
			cambrure: '',
			hanche_pantalon: '',
			hanche_chemise: '',
			cuisse: '',
			long_genou: '',
			long_pantalon: '',
			tour_genou: '',
			long_robe: '',
			long_jupe: '',
			long_combine: '',
			enfouchure: '',
			long_taille_dos: '',
			long_taille_devant: '',
			mollet: '',

		}
	},

	setup() {

		let etat3 = ref(true)
		let etat4 = ref(false)

		const action = function () {
			etat3.value = false
			etat4.value = true
		}
		const faire = function () {
			etat3.value = true
			etat4.value = false
		}

		return {
			action,
			faire,
			etat3,
			etat4
		}
	},

	methods: {
		valeurRecord(){
			
			axios.post('http://127.0.0.1:8000/api/valeur/', {
				idMesure: 3,
				idTypeMesure: 1,
				valeur: this.dos
			})

			 axios.post('http://127.0.0.1:8000/api/valeur/', {
				idMesure: 1,
				idTypeMesure: 2,
				valeur: this.poitrine
			})

			axios.post('http://127.0.0.1:8000/api/valeur/', {
				idMesure: 1,
				idTypeMesure: 3,
				valeur: this.haut_poitrine
			})

			axios.post('http://127.0.0.1:8000/api/valeur/', {
				idMesure: 1,
				idTypeMesure: 4,
				valeur: this.long_sous_seins
			})

			axios.post('http://127.0.0.1:8000/api/valeur/', {
				idMesure: 1,
				idTypeMesure: 5,
				valeur: this.sous_seins
			})

			axios.post('http://127.0.0.1:8000/api/valeur/', {
				idMesure: 1,
				idTypeMesure: 6,
				valeur: this.long_taille
			})

			axios.post('http://127.0.0.1:8000/api/valeur/', {
				idMesure: 1,
				idTypeMesure: 7,
				valeur: this.ecart_poitrine
			})
			
			axios.post('http://127.0.0.1:8000/api/valeur/', {
				idMesure: 1,
				idTypeMesure: 8,
				valeur: this.ventre
			})

			axios.post('http://127.0.0.1:8000/api/valeur/', {
				idMesure: 1,
				idTypeMesure: 9,
				valeur: this.cou
			})

			axios.post('http://127.0.0.1:8000/api/valeur/', {
				idMesure: 1,
				idTypeMesure: 10,
				valeur: this.long_manche
			})

			axios.post('http://127.0.0.1:8000/api/valeur/', {
				idMesure: 1,
				idTypeMesure: 11,
				valeur: this.tour_bras
			})

			axios.post('http://127.0.0.1:8000/api/valeur/', {
				idMesure: 1,
				idTypeMesure: 12,
				valeur: this.long_corsage
			})

			axios.post('http://127.0.0.1:8000/api/valeur/', {
				idMesure: 1,
				idTypeMesure: 13,
				valeur: this.long_chemise
			})

			axios.post('http://127.0.0.1:8000/api/valeur/', {
				idMesure: 1,
				idTypeMesure: 14,
				valeur: this.long_bomba
			})

			axios.post('http://127.0.0.1:8000/api/valeur/', {
				idMesure: 1,
				idTypeMesure: 15,
				valeur: this.long_goodluck
			})

			axios.post('http://127.0.0.1:8000/api/valeur/', {
				idMesure: 1,
				idTypeMesure: 16,
				valeur: this.long_agbada
			})

			axios.post('http://127.0.0.1:8000/api/valeur/', {
				idMesure: 1,
				idTypeMesure: 17,
				valeur: this.long_vest
			})

			axios.post('http://127.0.0.1:8000/api/valeur/', {
				idMesure: 1,
				idTypeMesure: 18,
				valeur: this.cambrure
			})

			axios.post('http://127.0.0.1:8000/api/valeur/', {
				idMesure: 1,
				idTypeMesure: 19,
				valeur: this.hanche_pantalon
			})

			axios.post('http://127.0.0.1:8000/api/valeur/', {
				idMesure: 1,
				idTypeMesure: 20,
				valeur: this.hanche_chemise
			})

			axios.post('http://127.0.0.1:8000/api/valeur/', {
				idMesure: 1,
				idTypeMesure: 21,
				valeur: this.cuisse
			})

			axios.post('http://127.0.0.1:8000/api/valeur/', {
				idMesure: 1,
				idTypeMesure: 22,
				valeur: this.long_genou
			})

			axios.post('http://127.0.0.1:8000/api/valeur/', {
				idMesure: 1,
				idTypeMesure: 23,
				valeur: this.long_pantalon	
			})

			axios.post('http://127.0.0.1:8000/api/valeur/', {
				idMesure: 1,
				idTypeMesure: 24,
				valeur: this.tour_genou
			})

			axios.post('http://127.0.0.1:8000/api/valeur/', {
				idMesure: 1,
				idTypeMesure: 25,
				valeur: this.long_robe
			})

			axios.post('http://127.0.0.1:8000/api/valeur/', {
				idMesure: 1,
				idTypeMesure: 26,
				valeur: this.long_jupe
			})

			axios.post('http://127.0.0.1:8000/api/valeur/', {
				idMesure: 1,
				idTypeMesure: 27,
				valeur: this.long_combine
			})

			axios.post('http://127.0.0.1:8000/api/valeur/', {
				idMesure: 1,
				idTypeMesure: 28,
				valeur: this.long_taille
			})

			axios.post('http://127.0.0.1:8000/api/valeur/', {
				idMesure: 1,
				idTypeMesure: 29,
				valeur: this.long_taille_dos
			})

			axios.post('http://127.0.0.1:8000/api/valeur/', {
				idMesure: 1,
				idTypeMesure: 30,
				valeur: this.long_taille_devant
			})

			axios.post('http://127.0.0.1:8000/api/valeur/', {
				idMesure: 1,
				idTypeMesure: 31,
				valeur: this.mollet
			})

			axios.post('http://127.0.0.1:8000/api/valeur/', {
				idMesure: 1,
				idTypeMesure: 32,
				valeur: this.larg_agbada
			}) 
		}
	}
}
</script>

<style>
@import url(@/styles/style.css) ;
</style>