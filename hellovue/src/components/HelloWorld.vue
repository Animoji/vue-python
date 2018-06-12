<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <router-link to="/test"><h2>前往test页面</h2></router-link>
    <router-link to="/book"><h2>前往book管理页面</h2></router-link>
    <i class="icon-shenfenzheng"></i>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Hello World!'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
a {
  color: #42b983;
}
</style>
