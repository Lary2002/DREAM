import { createApp } from 'vue'
import App from './App.vue'
import router from '@/router'
createApp(App).use(router).mount('#app')


// import {createRouter, createWebHashHistory} from "vue-router"
// import GardeProjet from './components/Projets/GardeProjet.vue'
// import InscriptionProjet from './components/Projets/InscriptionProjet.vue'
// import ConnexionProjet from './components/Projets/ConnexionProjet.vue'
// import AcceuilProjet from './components/Projets/AcceuilProjet.vue'
// import MotProjet from './components/Projets/MotProjet.vue'
// import StylisteProjet from './components/Projets/StylisteProjet.vue'
// import MesureProjet from './components/Projets/MesureProjet.vue'
// import ProposProjets from './components/Projets/ProposProjets.vue'
// import PostesProjets from './components/Projets/PostesProjets.vue'
// import CombinaisonProjet from './components/Projets/CombinaisonProjet.vue'
// import DecouvrirProjet from './components/Projets/DecouvrirProjet.vue'
// import PanierProjet from './components/Projets/PanierProjet.vue'
// import PayementProjet from './components/Projets/PayementProjet.vue'
// import CommandeProjet from './components/Projets/CommandeProjet.vue'
// const routes = [
//     {
//         path: '/',
//          component: GardeProjet 
//      },
//      {
//         path: '/Panier',
//          component: PanierProjet,
//          props: true 
//      },
//      {
//         path: '/payement',
//          component: PayementProjet 
//      },
//      {
//         path: '/Commande',
//          component: CommandeProjet 
//      },

//     {
//             path: '/Inscription',
//              component: InscriptionProjet 
//          },
//          {
//             path: '/postes',
//              component: PostesProjets 
//          },
//          {
//             path: '/Apropos',
//              component: ProposProjets 
//          },
//          {
//              path: '/Connexion',
//              component: ConnexionProjet 
//          },
//          {
//             path: '/Acceuil',
//             component: AcceuilProjet 
//         },
//         {
//             path: '/Reinitialisation',
//             component: MotProjet 
//         },
//         {
//             path: '/Styliste',
//             component: StylisteProjet 
//         },
//         {
//             path: '/mesure',
//             component: MesureProjet 
//         },
//         {
//             name: 'Combinaison', path: '/Combinaison/:nameCombin',
//             component: CombinaisonProjet,
//             props: true
//         },

//         {
//             name: 'Decouvrir',   path: '/Decouverte/:namePers',
//             component: DecouvrirProjet, 
//             props: true
//         }
        
// ]
// const router = createRouter({
//     history: createWebHashHistory(),
//     routes
// })

// let app= createApp(App)
// app.use(router)
// app.mount('#app')
// createApp(App).mount('#app')

// import router from '@/router'
// import { from } from 'core-js/core/array'
// App.use(router)
