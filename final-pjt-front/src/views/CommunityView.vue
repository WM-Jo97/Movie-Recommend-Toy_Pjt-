<template>
  <b-container class=" mt-3 bv-example-row animate__animated animate__fadeInRight" >
    <div id="board" class="card">
      <div class="card-header text-center"> 
       <b-row align-v="center"> 
        <b-col></b-col>
        <b-col class="" cols="8"> <h2 class="p-2 mb-0">자유게시판</h2></b-col>
        <b-col class="text-right" ><router-link :to="{name : 'ArticleCreateView'} "><b-button pill variant="outline-secondary">글 쓰기</b-button></router-link></b-col>
       </b-row>
      </div>
      <div class="card-body">
        <b-row>
          <b-col cols="12">
          <b-list-group class="text-left" id="articlelist" 
            :per-page="perPage"
            :current-page="currentPage"
            
            >
            <b-list-group-item>
              <b-row>
                <b-col class="text-center" cols="11"> 제 목 </b-col>
                <b-col class="text-right" cols="1">작성자</b-col>
              </b-row>
            </b-list-group-item >
            <b-list-group-item v-for="article in itemForArticles" :key="article.x" :articles="article">
              <b-row>
              <b-col cols="8">
              <router-link :to="{name : 'ArticleDetailView', params:{articleid : article.id} }">
                {{ article.title }} 
              </router-link>
              </b-col>
              <b-col class="text-right" cols="4"> {{ article.user.nickname }} </b-col>
              </b-row>
            </b-list-group-item>         
          </b-list-group>
          </b-col>
        </b-row>
        <b-pagination
          pills
          class="mt-4"
          v-model="currentPage"
          :total-rows="rows"
          :per-page="perPage"
          size="sm"
          align="center"
          aria-controls="aritclelist"
        ></b-pagination>
      </div>
    </div>
  </b-container>
</template>
<script>
import axios from 'axios'
export default {
  name: 'CommunityView',
  data() {
    return {
      articles: [],
      currentPage : 1,
      perPage : 10,
    }
  },
  methods : {
    getArticles(){
      const API_URL = process.env.VUE_APP_API_URL
      axios({
        method : 'get',
        url: `${API_URL}/api/v1/community/getarticles/`,
        headers: {
          Authorization: `Bearer ${this.$store.getters.getToken}`
        }
      })
        .then((res) => {
          this.articles = res.data
        })
        .catch((error) => {
          console.log(error)
        })
    },
  },
  created(){
    return this.getArticles()
  },
  computed : {
    rows(){
      return this.articles.length
    },
    itemForArticles(){
      return this.articles.slice((this.currentPage - 1) * this.perPage,this.currentPage * this.perPage)
    }
  }
}
</script>
<style scoped>
#board{
  min-height: 600px;
}
.animate__animated.animate__fadeInRight {
  --animate-duration: 0.8s;
}
</style>