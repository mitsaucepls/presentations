<template>
  <v-timeline direction="horizontal">
    <v-timeline-item
      dot-color="#187B3C"
    >
      <template v-slot:opposite>
        <strong>Performics Germany GmbH</strong>
      </template>
      <div>
        <div class="text-h6">Praktikum</div>
        <p>
          Erstes mal eine Vision von Teamwork im Arbeitsumfeld. Website Programmierung.
        </p>
      </div>
    </v-timeline-item>

    <v-timeline-item
      dot-color="#96131B"
    >
      <template v-slot:opposite>
        <strong>OSZ IMT</strong>
      </template>
      <div>
        <div class="text-h6">Abitur mit IT Leistungskurs</div>
        <p>
          Erste Erfahrungen mit einer richtigen Programmiersprache. Leidenschaft entfacht.
        </p>
      </div>
    </v-timeline-item>

    <v-timeline-item
      dot-color="#E20074"
    >
      <template v-slot:opposite>
        <strong>Deutsche Telekom IT Gigabit Hub</strong>
      </template>
      <div>
        <div class="text-h6">Onboarding</div>
        <p>
          Einführung in den Workflow eines Fullstack Engineers.
        </p>
      </div>
    </v-timeline-item>

    <v-timeline-item
      dot-color="#E20074"
    >
      <template v-slot:opposite>
        <strong>Deutsche Telekom IT B2B Solutions API Hub</strong>
      </template>
      <div>
        <div class="text-h6">Praktische Erfahrungen</div>
        <p>
          Neue Einblicke und tiefere Erfahrung in DevOps Workflows.
        </p>
      </div>
    </v-timeline-item>
  </v-timeline>
</template>

<style>
html:not(.dark) .v-timeline-divider__before, html:not(.dark) .v-timeline-divider__after {
  background: black;
}

html.dark .v-timeline-divider__before, html.dark .v-timeline-divider__after {
  background: white;
}

</style>
