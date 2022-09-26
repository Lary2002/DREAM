<template>

   <hearder-projet />
   <form v-if="etat" class="review-form">
      <div class="card">
         <input type="recherche" class="cherche" required name="recherche" placeholder="Recherche...">
         <br>
         <br>
      </div>

      <div>

         <p class="bobo"> A</p>
         <ul class="bibi">
            <hr>
            <div class="flo">
               <div @click="hide">
                  <li>A Emery</li>
               </div>

               <img src="@/assets/love.png" alt="" class="lo">
               <!-- <img src="@/assets/heart.png" alt="" class="lo"> -->
            </div>
            <hr>
            <div class="flo">
               <li>A.L.C</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>aaizél</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>AARMY</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Abysse</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Acheval Pampa</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Acne Studios</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Act+ Acre</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Adam Lippes</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>adidas by Stella McCartney</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>adidas Originals</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>AERIN </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>AERIN Beauty</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Aesop </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li> aeyde</li>
               <hr>
            </div>
            <div class="flo">
               <li>African Botanics</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Agent Nateur</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
         </ul>
         <p class="bobo"> B</p>
         <hr>
         <ul class="bibi">
            <div class="flo">
               <li>B SIDES</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bala </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Balenciaga </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Balmain</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bamford </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bang  & Olufsen</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Baobab Collection</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Barbour</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Baserange</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bassike Bassike</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Batsheva </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Baudoin & Lange</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bayco </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>BBB London</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bea Bongiasca</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>BeautyStat Cosmetics DESOUZA</li><img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Begum Khan</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
         </ul>
         <hr>
         <p class="bobo"> C</p>
         <ul class="bibi">
            <div class="flo">
               <li>B SIDES</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bala </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Balenciaga </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Balmain</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bamford </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bang  & Olufsen</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Baobab Collection</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Barbour</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Baserange</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bassike Bassike</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Batsheva </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Baudoin & Lange</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bayco </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>BBB London</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bea Bongiasca</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>BeautyStat Cosmetics DESOUZA</li><img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Begum Khan</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
         </ul>
         <p class="bobo"> D</p>
         <ul class="bibi">
            <div class="flo">
               <li>B SIDES</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bala </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Balenciaga </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Balmain</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bamford </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bang  & Olufsen</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Baobab Collection</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Barbour</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Baserange</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bassike Bassike</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Batsheva </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Baudoin & Lange</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bayco </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>BBB London</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bea Bongiasca</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>BeautyStat Cosmetics DESOUZA</li><img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Begum Khan</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
         </ul>
         <p class="bobo"> E</p>
         <ul class="bibi">
            <div class="flo">
               <li>B SIDES</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bala </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Balenciaga </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Balmain</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bamford </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bang  & Olufsen</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Baobab Collection</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Barbour</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Baserange</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bassike Bassike</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Batsheva </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Baudoin & Lange</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bayco </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>BBB London</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bea Bongiasca</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>BeautyStat Cosmetics DESOUZA</li><img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Begum Khan</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
         </ul>
         <p class="bobo"> F</p>
         <ul class="bibi">
            <div class="flo">
               <li>B SIDES</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bala </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Balenciaga </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Balmain</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bamford </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bang  & Olufsen</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Baobab Collection</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Barbour</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Baserange</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bassike Bassike</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Batsheva </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Baudoin & Lange</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bayco </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>BBB London</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bea Bongiasca</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>BeautyStat Cosmetics DESOUZA</li><img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Begum Khan</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
         </ul>
         <p class="bobo"> G</p>
         <ul class="bibi">
            <div class="flo">
               <li>B SIDES</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bala </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Balenciaga </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Balmain</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bamford </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bang  & Olufsen</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Baobab Collection</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Barbour</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Baserange</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bassike Bassike</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Batsheva </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Baudoin  & Lange</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bayco </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>BBB London</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bea Bongiasca</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>BeautyStat Cosmetics DESOUZA</li><img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Begum Khan</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
         </ul>
         <p class="bobo"> H</p>
         <ul class="bibi">
            <div class="flo">
               <li>B SIDES</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bala </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Balenciaga </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Balmain</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bamford </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bang  & Olufsen</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Baobab Collection</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Barbour</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Baserange</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bassike Bassike</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Batsheva </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Baudoin & Lange</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bayco </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>BBB London</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bea Bongiasca</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>BeautyStat Cosmetics DESOUZA</li><img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Begum Khan</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
         </ul>
         <p class="bobo"> I</p>
         <ul class="bibi">
            <div class="flo">
               <li>B SIDES</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bala </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Balenciaga </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Balmain</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bamford </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bang  & Olufsen</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Baobab Collection</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Barbour</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Baserange</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bassike Bassike</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Batsheva </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Baudoin  & Lange</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bayco </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>BBB London</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bea Bongiasca</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>BeautyStat Cosmetics DESOUZA</li><img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Begum Khan</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
         </ul>
         <p class="bobo"> J</p>
         <ul class="bibi">
            <div class="flo">
               <li>B SIDES</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bala </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Balenciaga </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Balmain</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bamford </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bang  & Olufsen</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Baobab Collection</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Barbour</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Baserange</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bassike Bassike</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Batsheva </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Baudoin & Lange</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bayco </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>BBB London</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bea Bongiasca</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>BeautyStat Cosmetics DESOUZA</li><img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Begum Khan</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
         </ul>
         <p class="bobo"> K</p>
         <ul class="bibi">
            <div class="flo">
               <li>B SIDES</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bala </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Balenciaga </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Balmain</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bamford </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bang  & Olufsen</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Baobab Collection</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Barbour</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Baserange</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bassike Bassike</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Batsheva </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Baudoin & Lange</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bayco </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>BBB London</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bea Bongiasca</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>BeautyStat Cosmetics DESOUZA</li><img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Begum Khan</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
         </ul>
         <p class="bobo"> L</p>
         <ul class="bibi">
            <div class="flo">
               <li>B SIDES</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bala </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Balenciaga </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Balmain</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bamford </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bang  & Olufsen</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Baobab Collection</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Barbour</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Baserange</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bassike Bassike</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Batsheva </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Baudoin & Lange</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bayco </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>BBB London</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bea Bongiasca</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>BeautyStat Cosmetics DESOUZA</li><img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Begum Khan</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
         </ul>
         <p class="bobo"> M</p>
         <ul class="bibi">
            <div class="flo">
               <li>B SIDES</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bala </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Balenciaga </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Balmain</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bamford </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bang  & Olufsen</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Baobab Collection</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Barbour</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Baserange</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bassike Bassike</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Batsheva </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Baudoin & Lange</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bayco </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>BBB London</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bea Bongiasca</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>BeautyStat Cosmetics DESOUZA</li><img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Begum Khan</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
         </ul>
         <p class="bobo"> N</p>
         <ul class="bibi">
            <div class="flo">
               <li>B SIDES</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bala </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Balenciaga </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Balmain</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bamford </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bang  & Olufsen</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Baobab Collection</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Barbour</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Baserange</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bassike Bassike</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Batsheva </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Baudoin & Lange</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bayco </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>BBB London</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bea Bongiasca</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>BeautyStat Cosmetics DESOUZA</li><img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Begum Khan</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
         </ul>
         <p class="bobo"> O</p>
         <ul class="bibi">
            <div class="flo">
               <li>B SIDES</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bala </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Balenciaga </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Balmain</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bamford </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bang  & Olufsen</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Baobab Collection</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Barbour</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Baserange</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bassike Bassike</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Batsheva </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Baudoin & Lange</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bayco </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>BBB London</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bea Bongiasca</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>BeautyStat Cosmetics DESOUZA</li><img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Begum Khan</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
         </ul>
         <p class="bobo"> P</p>
         <ul class="bibi">
            <div class="flo">
               <li>B SIDES</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bala </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Balenciaga </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Balmain</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bamford </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bang  & Olufsen</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Baobab Collection</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Barbour</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Baserange</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bassike Bassike</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Batsheva </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Baudoin & Lange</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bayco </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>BBB London</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bea Bongiasca</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>BeautyStat Cosmetics DESOUZA</li><img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Begum Khan</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
         </ul>
         <p class="bobo"> Q</p>
         <ul class="bibi">
            <div class="flo">
               <li>B SIDES</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bala </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Balenciaga </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Balmain</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bamford </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bang  & Olufsen</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Baobab Collection</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Barbour</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Baserange</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bassike Bassike</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Batsheva </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Baudoin & Lange</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bayco </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>BBB London</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bea Bongiasca</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>BeautyStat Cosmetics DESOUZA</li><img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Begum Khan</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
         </ul>
         <p class="bobo"> R</p>
         <ul class="bibi">
            <div class="flo">
               <li>B SIDES</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bala </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Balenciaga </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Balmain</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bamford </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bang  & Olufsen</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Baobab Collection</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Barbour</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Baserange</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bassike Bassike</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Batsheva </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Baudoin & Lange</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bayco </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>BBB London</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bea Bongiasca</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>BeautyStat Cosmetics DESOUZA</li><img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Begum Khan</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
         </ul>
         <p class="bobo"> S</p>
         <ul class="bibi">
            <div class="flo">
               <li>B SIDES</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bala </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Balenciaga </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Balmain</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bamford </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bang  & Olufsen</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Baobab Collection</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Barbour</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Baserange</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bassike Bassike</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Batsheva </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Baudoin & Lange</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bayco </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>BBB London</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bea Bongiasca</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>BeautyStat Cosmetics DESOUZA</li><img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Begum Khan</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
         </ul>
         <p class="bobo"> T</p>
         <ul class="bibi">
            <div class="flo">
               <li>B SIDES</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bala </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Balenciaga </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Balmain</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bamford </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bang  & Olufsen</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Baobab Collection</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Barbour</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Baserange</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bassike Bassike</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Batsheva </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Baudoin & Lange</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bayco </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>BBB London</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bea Bongiasca</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>BeautyStat Cosmetics DESOUZA</li><img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Begum Khan</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
         </ul>
         <p class="bobo"> U</p>
         <ul class="bibi">
            <div class="flo">
               <li>B SIDES</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bala </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Balenciaga </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Balmain</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bamford </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bang  & Olufsen</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Baobab Collection</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Barbour</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Baserange</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bassike Bassike</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Batsheva </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Baudoin & Lange</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bayco </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>BBB London</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bea Bongiasca</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>BeautyStat Cosmetics DESOUZA</li><img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Begum Khan</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
         </ul>
         <p class="bobo"> V</p>
         <ul class="bibi">
            <div class="flo">
               <li>B SIDES</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bala </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Balenciaga </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Balmain</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bamford </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bang  & Olufsen</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Baobab Collection</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Barbour</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Baserange</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bassike Bassike</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Batsheva </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Baudoin & Lange</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bayco </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>BBB London</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bea Bongiasca</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>BeautyStat Cosmetics DESOUZA</li><img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Begum Khan</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
         </ul>
         <p class="bobo"> W</p>
         <ul class="bibi">
            <div class="flo">
               <li>B SIDES</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bala </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Balenciaga </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Balmain</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bamford </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bang  & Olufsen</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Baobab Collection</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Barbour</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Baserange</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bassike Bassike</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Batsheva </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Baudoin & Lange</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bayco </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>BBB London</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bea Bongiasca</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>BeautyStat Cosmetics DESOUZA</li><img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Begum Khan</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
         </ul>
         <p class="bobo"> X</p>
         <ul class="bibi">
            <div class="flo">
               <li>B SIDES</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bala </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Balenciaga </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Balmain</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bamford </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bang  & Olufsen</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Baobab Collection</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Barbour</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Baserange</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bassike Bassike</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Batsheva </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Baudoin & Lange</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bayco </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>BBB London</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bea Bongiasca</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>BeautyStat Cosmetics DESOUZA</li><img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Begum Khan</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
         </ul>
         <p class="bobo"> Y</p>
         <ul class="bibi">
            <div class="flo">
               <li>B SIDES</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bala </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Balenciaga </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Balmain</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bamford </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bang  & Olufsen</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Baobab Collection</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Barbour</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Baserange</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bassike Bassike</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Batsheva </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Baudoin & Lange</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bayco </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>BBB London</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bea Bongiasca</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>BeautyStat Cosmetics DESOUZA</li><img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Begum Khan</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
         </ul>
         <p class="bobo"> Z</p>
         <ul class="bibi">
            <div class="flo">
               <li>B SIDES</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bala </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Balenciaga </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Balmain</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bamford </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bang  & Olufsen</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Baobab Collection</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Barbour</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Baserange</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bassike Bassike</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Batsheva </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Baudoin & Lange</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bayco </li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>BBB London</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Bea Bongiasca</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>BeautyStat Cosmetics DESOUZA</li><img src="@/assets/love.png" alt="" class="lo">
            </div>
            <hr>
            <div class="flo">
               <li>Begum Khan</li>
               <img src="@/assets/love.png" alt="" class="lo">
            </div>
         </ul>
      </div>

   </form>
   <br>
   <div class="graph">
   
      <div v-if="etat2" class="infor">
         <div class="carte">
            <img src="@/assets/carto.jpg" alt="" class="ronde">
            <hr class="vu">
            <div>
               <p class="en">Emery</p>
               <p class="en">Dollar Fashion</p>
               <p>dollar24@gmail.com</p>
               <hr>
               <p class="mini">Couture dame</p>
            </div>

         </div>
         <!-- <p class="eme">A Emery</p> -->
         <div class="pron">
            <p>15Postes</p>
            <p>75Collections</p>
            <p>10Prospects</p>
         </div>
         <hr class="vo">
         <div class="proo">
            <p class="coro">Postes</p>
            <hr>
            <p class="coro">Colletions</p>
         </div>
      </div>
   </div>
   <FooterProjet />
</template>

<script>
import FooterProjet from '../Projets/FooterProjet.vue';
import HearderProjet from '../Projets/HearderProjet.vue';
import { ref } from "vue"
export default {
   name: "StylisteProjet",
   components: {
      HearderProjet, FooterProjet
   },
   setup() {
      let etat = ref(true)
      let etat2 = ref(false)

      const hide = function () {
         etat.value = false
         etat2.value = true
      }
      return {
         hide,
         etat,
         etat2
      }
   }

}
</script>

<style>
.lo {
   height: 3%;
   width: 2%;
}

.flo {
   display: flex;
   justify-content: space-between;
}

.coro {
   background-color: blue;
   height: 30px;
   width: 110px;
   text-align: center;
   border-radius: 20px;
   
}

.vo {
   height: 5px;
}

.vu {
   width: 5px;
}

.mini {
   color: rgb(59, 59, 182)
}

.carte {
   display: flex;
}

.proo {
   display: flex;
   justify-content: space-around;
   justify-content:space-around;
}

.pron {
   display: flex;
   justify-content: space-between;
}

.en {
   font-weight: bolder;
   font-size: 1.5rem;
}

.eme {
   font-weight: bolder;
   font-size: 1.5rem;
   margin-left: 25%;
}

.bobo {
   font-weight: bolder;
   font-size: 1.7rem;
}

.bibi {

   font-size: 1rem;
   cursor: pointer;
}

.pop {

   color: blue;
   text-decoration: none;
}

.graph{
   margin-top: 90px;
   margin-bottom: 60px;

}
.ronde {
   border: 1px solid black;
   border-radius: 200px;
   width: 190px;
   height: 180px;
   margin-left: 20%;
}
</style>