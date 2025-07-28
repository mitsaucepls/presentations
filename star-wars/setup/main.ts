import { defineAppSetup } from '@slidev/types'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

const customTransitions = {
  'my-transition': {
    name: 'my-transition',
    onEnter: (el, done) => {
      console.log("enter")
      done()
    },
    onLeave: (el, done) => {
      console.log("leave")
      done()
    }
  }
}


export default defineAppSetup(({ app, router }) => {
  // Vue App
  const vuetify = createVuetify({
    components,
    directives,
  })
  app.use(vuetify)

  // Register custom transition
})
