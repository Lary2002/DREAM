<template>
  
    <transition-group name="fade" tag="div" >
      <div class="muha">
      <div v-for="i in [currentIndex]" :key="i">
        <img :src="currentImg"  />
      </div>
  </div>

    </transition-group>
    <a class="prev" @click="prev" href="#">&#10094; Previous</a>
    <a class="next" @click="next" href="#">&#10095; Next</a>
</template>

<script>
import img1 from "@/assets/combinaison.jpg"
import img2 from "@/assets/combinaiso.jpg"
import img3 from "@/assets/combinais.jpg"
import img4 from "@/assets/combinai.jpg"
export default {
  name: "CarosselProjet",
  data() {
    return {
      images: [img1, img2, img3, img4],
      timer: null,
      currentIndex: 0
    };
  },

  mounted: function() {
    this.startSlide();
  },

  methods: {
    startSlide: function() {
      this.timer = setInterval(this.next, 4000);
    },

    next: function() {
      this.currentIndex += 1;
    },
    prev: function() {
      this.currentIndex -= 1;
    }
  },

  computed: {
    currentImg: function() {
      return this.images[Math.abs(this.currentIndex) % this.images.length];
    }
  }
};
</script>

<style>



.fafa{
  margin-left:35%;
  
  
}

.fade-enter-active,
.fade-leave-active {
  transition: all 0.9s ease;
  overflow: hidden;
  visibility: visible;
  position: absolute;
  width:500px;
  opacity: 1;
}

.fade-enter,
.fade-leave-to {
  visibility: hidden;
  width:500px;
  opacity: 0;
}

img {
  height:500px;
  width:500px
}

.prev, .next {
  cursor: pointer;
  position: absolute;
  top: 60%;
  width: auto;
  padding: 16px;
  color: white;
  font-weight: bold;
  font-size: 18px;
  transition: 0.7s ease;
  border-radius: 0 4px 4px 0;
  text-decoration: none;
  user-select: none;
}

.next {
  right: 32.7%;
}

.prev {
  left: 30%;
}

.prev:hover, .next:hover {
  background-color: rgba(0,0,0,0.9);
}

</style>