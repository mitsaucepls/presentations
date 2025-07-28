<script>
function onEnter(el, done) {
  console.log("enter")
}

function onLeave(el, done) {
  console.log("leave")
}
</script>

<template>
  <Transition
    name="hyprspace"
    @enter="onEnter"
    @leave="onLeave">
    <slot></slot>
  </Transition>
</template>

<style>
</style>
