<template>
  <div class="hello">
      <h1>{{ msg }}</h1>
      <h2>我是测试页面</h2>
      <input type="button" @click="get()" value="按钮">
  </div>
</template>

<script>
export default {
  name: 'helloworld',
  data () {
    return {
      msg: '欢迎进入vue的世界'
    };
  },

  components: {},

  computed: {},

  methods: {
    get: function () {
      this.$http.jsonp('https://sug.so.360.cn/suggest',{word:'a'},{jsonp:'callback'}).then(function(res){
        alert(res.data);
      },function(res){
        console.log(res.status);
      });
    }
  }
}

</script>
<style scoped>
h1,h2 {font-weight: normal;color: #42b983}
</style>