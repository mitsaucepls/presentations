---
# You can also start simply with 'default'
theme: seriph
# random image from a curated Unsplash collection by Anthony
# like them? see https://unsplash.com/collections/94734566/slidev
background: plastic-ocean-background-2.jpg
# some information about your slides (markdown enabled)
# title: Müllrecycling in Deutschland auf Kosten anderer Länder?
# info: |
#  Idk bro
# apply unocss classes to the current slide
class: text-center
# https://sli.dev/features/drawing
drawings:
  persist: false
# slide transition: https://sli.dev/guide/animations.html#slide-transitions
transition: slide-left
# enable MDC Syntax: https://sli.dev/features/mdc
mdc: true
# take snapshot for each slide in the overview
overviewSnapshots: true
hideInToc: true
---

<h1>Müllrecycling in Deutschland<br>auf Kosten anderer Länder?</h1>

#### Von Markus Siegert

<style>
h1 {
  all: initial;
  font-size: 2em !important;
  line-height: 1.2 !important;
}

h4 {
  font-size: 1em !important;
}
</style>


<!--
The last comment block of each slide will be treated as slide notes. It will be visible and editable in Presenter Mode along with the slide. [Read more in the docs](https://sli.dev/guide/syntax.html#notes)
-->

---
transition: fade-out
hideInToc: true
---

# Gliederung

<Toc minDepth="1" maxDepth="2" :listStyle="['upper-alpha', 'lower-alpha']"></Toc>

<style>
h1 {
  background-color: #2B90B6;
  background-image: linear-gradient(45deg, #4EC5D4 10%, #146b8c 20%);
  background-size: 100%;
  -webkit-background-clip: text;
  -moz-background-clip: text;
  -webkit-text-fill-color: transparent;
  -moz-text-fill-color: transparent;
}
</style>

---
transition: slide-up
---

# Plastikmüll in Deutschland
<img src="./kunststoffabfaelle-2021.jpeg" alt="heh" width="75%" height="75%" class="center">

<style>
.center {
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 75%;
}
</style>

<!-- hier sind normale stats wie viel allgemein in deutschland und dann nochmal wie viel plastik und dann wie viel plastik exportiert wird -->
<!-- https://www.umweltbundesamt.de/daten/ressourcen-abfall/abfallaufkommen (Allgemeine Stats) -->
<!-- https://www.nabu.de/umwelt-und-ressourcen/abfall-und-recycling/26205.html (Stats zu exporten und plastik) -->
<!-- https://www.greenpeace.de/engagieren/nachhaltiger-leben/plastikmuellexporte-deutschland (experte am werk) -->

<!-- plastik exportiert zu 'anerkannten' recycling stationen im ausland zaehlt zur deutschen recycling quote. ( 2 ) -->
<!-- cool story firma in de exportiert nach tuerkei illegalen muell und geht insolvent. Muell bleibt in Tuerkei. ( 3 ) -->
<!-- 2.8% des Plastikmuells wird recycled. ( 3 ) -->
<!-- Basler Konvention -->
<!-- Die Recycling Luege -->
<!-- min 7 Expertenargument gegen Recycling warum es nicht funktionieren kann -->
<!-- min 8.15 6 millionene tonnen plastik muell -->
<!-- min 15 2.8% (3) - 5% aus dem gelben Sack werden wieder zu verwendbaren plastik gemacht. Grund ist zu schmutzige sachen wie Chips, Joghurt und gemuese schalen. -->
<!-- min 16 grosse firmen nehmen lieber billigeres material was direkt aus der produktion kommt. anstatt teures recyclestes material. -->
<!-- min 16.20 400 millionen neu plastik durch eine Produktionsstaette | geschaetzt 20% des Oels fuer plastik -->
<!-- min 19 Mischkunststoffe koennen nicht recycled werden. Man kann nicht aus Scheisse Gold machen, ausserdem stinkt das Zeug. Es gibt aber anwendungen dafuer naemlich z.b. eisenbahnschwellen. Aber selbst das ist nicht profitabel. -->
<!-- min 24 so verschmutzt dass eine stoffliche recyclung nicht mehr stattfinden kann und thermisch verwertet wird. Erstmal zerhackt und dann als ersatzbrennstoff genutzt. 70% des Brennstoffs von Zementherstellung wird so gewonnen. -->
<!-- min 26 Zementherstellung hat 3 mal mehr THG ausstoss als Flugzeuge betrieb -->
<!-- min 29 Energiegewinnung aus Restmuell und deswegen gruen. Nicht weil es umweltfreundlich ist, sondern weil es das Plastikproblem teilweise loest. -->
<!-- min 31 Exportierter Muell gilt auch als recycled -->
<!-- min 32 China hat dicht gemacht und jetzt andere laender wie Malaisia, Phillipinen usw aber die beschraenken jetzt auch. (Merkt man an der Quelle nabu in dem einen Jahr waren es 170 Tonnen in dem anderen nur noch 65 tonnen) -->
<!-- min 32.5 Tuerkei als haupt importer. und illegal ohne filter verbrannt. -->
<!-- min 45 es wird immer schwerer Mischkunststoffe zu exportieren (illegal) -->
<!-- Recycling ist die Illusion man hat ein Problem und Technologie loest sie aus Zauberhand. -->
<!-- Durch diese Fehlannahme wird es zu keiner wirklichen loesung kommen koennen denn es ist ja schon faelschlicherweise geloest. -->

<!-- |     |     | -->
<!-- | --- | --- | -->
<!-- | <kbd>right</kbd> / <kbd>space</kbd>| next animation or slide | -->
<!-- | <kbd>left</kbd>  / <kbd>shift</kbd><kbd>space</kbd> | previous animation or slide | -->
<!-- | <kbd>up</kbd> | previous slide | -->
<!-- | <kbd>down</kbd> | next slide | -->

<!-- <!-1- https://sli.dev/guide/animations.html#click-animation -1-> -->
<!-- <img -->
<!--   v-click -->
<!--   class="absolute -bottom-9 -left-7 w-80 opacity-50" -->
<!--   src="https://sli.dev/assets/arrow-bottom-left.svg" -->
<!--   alt="" -->
<!-- /> -->
<!-- <p v-after class="absolute bottom-23 left-45 opacity-30 transform -rotate-10">Here!</p> -->

---
transition: slide-up
---

# Der Grüne Punkt
<v-switch class="midl">
  <template #0>
    <img src="./canvas(3).png" alt="heh" width="50%" height="50%" class="center">
  </template>
  <template #1>
    <div class="vertical-center">
      <ul>
        <li><strong>Existiert seit</strong>: 90er Jahren.</li>
        <li><strong>Verwertung</strong>: 5,67t also 99,4% davon werden Verwertet.</li> % 99,4 stimmt nicht mit der Graphik davor ueberein aber so sagt es das UBA
      </ul>
    </div>
    <Footer />
  </template>
</v-switch>

<style>
.midl {
  position: relative;
  height: 70%;
}

.vertical-center {
  margin: 0;
  position: absolute;
  top: 50%;
  -ms-transform: translateY(-50%);
  transform: translateY(-50%);
  width: 100%;
}

.center {
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 75%;
}
</style>
