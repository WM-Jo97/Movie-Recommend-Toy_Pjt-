<template>
  <b-container class="bv-example-row">
    <b-row>
      <b-col class="text-left">{{ comment.user.nickname }}</b-col>
    </b-row>
    <b-row>
      <b-col>
        <span v-if="isEdit">
        <textarea rows="1" v-model.trim="content" @keyup.enter="saveEdit"></textarea>
        </span>
        <span v-else>
          {{ comment.content }}
        </span>
      </b-col>
      <b-col cols="4" class="text-right" v-if="isAuthor">
        <span v-if="isEdit">
          <b-button  @click="saveEdit" size="sm" squared variant="outline-secondary">등록</b-button>
        </span>
        <span v-else>
          <b-button  @click="editComment" size="sm" squared variant="outline-secondary" id="editBtn">수정</b-button>
        </span>
        <b-button @click="deleteComment" size="sm" squared variant="outline-danger">X</b-button>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import axios from 'axios'

export default {
  name: "ArticleDetailComments",
  props: {
    comment: Object,
  },
  data() {
    return {
      isEdit: false,
      content: null,
      isAuthor: false,
    }
  },
  methods: {
    editComment() {
      this.content = this.comment.content
      this.isEdit = !this.isEdit
    },
    saveEdit(){
      const content = this.content
      if (!content) {
        alert("댓글을 입력해주세요")
        return
      } else {
        axios({
          method : 'put',
          url : `${process.env.VUE_APP_API_URL}/api/v1/community/comments/${this.comment.id}/`,
          headers : {
            Authorization : `Bearer ${this.$store.getters.getToken}`
          },
          data : {
            content : content
          }
        })
          .then(()=> {
            this.isEdit = false
            this.$emit('comment-update')
          })
          .catch((err)=> {
            console.log(err)
          })
      }
    },
    deleteComment() {
      axios({
        method: 'delete',
        url: `${process.env.VUE_APP_API_URL}/api/v1/community/comments/${this.comment.id}/`,
        headers : {
          Authorization : `Bearer ${this.$store.getters.getToken}`
        }
      })
        .then(() => {
          this.$emit('comment-update')
        })
        .catch((err) => {
          console.log(err)
        })
    },
    checkAuthor() {
      const user = this.$store.getters.getUser.pk
      const author = this.comment.user.id
      if (user == author) {
        this.isAuthor = true
      }
    },
  },
  created() {
    this.checkAuthor()
  }
}
</script>

<style>
</style>