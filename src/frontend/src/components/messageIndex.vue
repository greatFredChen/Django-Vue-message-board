<template>
    <el-container>
        <el-header>
            <el-button type="primary" class='log-out-button' @click="Logout()">
                欢迎:<i class="el-icon-user-solid"></i>{{this.$store.state.user_name}}&nbsp;&nbsp;注销
            </el-button>
        </el-header>
        <el-main>
            <el-tabs :tab-position="tabPosition" style="height:80%;">
                <el-tab-pane label="留言板">
                    <div class="board-container">
                        <el-collapse v-model="activeNames" v-for="item in message_list.slice((currentPage-1)*pagesize,currentPage*pagesize)">
                            <el-collapse-item :title="item.title" :name='item.id'>
                                <div class="collapse-title">{{item.title}}</div>
                                <div class="collapse-content"><i class="el-icon-edit-outline"></i>留言内容:{{item.content}}</div>
                                <div class="collapse-author"><i class="el-icon-user-solid"></i>{{item.created_by}}</div>
                                <div class="collapse-created-time"><i class="el-icon-date"></i>{{item.created_at}}</div>
                                <el-row>
                                    <div class="thump-char"><i class="el-icon-success"></i>{{item.thump_up_count}}</div>
                                    <div class="thump-char"><i class="el-icon-error"></i>{{item.thump_down_count}}</div>
                                </el-row>
                                <el-row>
                                    <el-button type="primary" @click="thump_up(item.id)">
                                        点赞
                                    </el-button>
                                    <el-button type="danger" @click="thump_down(item.id)">
                                        点踩
                                    </el-button>
                                </el-row>
                            </el-collapse-item>
                        </el-collapse>
                        <el-pagination
                            @size-change="handleSizeChange"
                            @current-change="handleCurrentChange"
                            :current-page="currentPage"
                            :page-sizes="[3, 6, 9, 12]"
                            :page-size="pagesize"         
                            layout="total, sizes, prev, pager, next, jumper"
                            :total="message_list.length"> 
                    </el-pagination>
                    </div>
                </el-tab-pane>
                <el-tab-pane label="写留言">
                    <el-card class='box-card'> 
                        <div class="text item"> 
                        <el-input
                        type="text"
                        placeholder="请输入你的标题"
                        v-model="message_title"
                        maxlength="10"
                        show-word-limit
                        >
                        </el-input>
                        </div>
                        <div class="text item">
                        <el-input
                        type="textarea"
                        placeholder="请输入你的留言"
                        autosize
                        v-model="message_content"
                        maxlength="250"
                        show-word-limit
                        >
                        </el-input>
                        </div>
                        <el-row>
                            <el-button type="primary" @click="messageSubmit()">
                                提交
                            </el-button>
                            <el-button type="info" @click="messageClear()">
                                清空
                            </el-button>
                        </el-row>
                    </el-card>
                </el-tab-pane>
            </el-tabs>
        </el-main>
    </el-container>
</template>

<style scoped>
    .el-main {
        background-color: #E9EEF3;
        color: #333;
        text-align: center;
        line-height: 160px;
    }
    
    .el-header {
        background-color: #B3C0D1;
        color: #333;
        text-align: center;
        line-height: 60px;
    }
    
    .el-tab-pane {
        width: 90%;
    }
    
    .log-out-button {
        float: right;
        margin-top: 10px;
    }
    
    .board-container {
        text-align: center;
    }
    
    .el-collapse-item {
        text-align: center;
    }
    
    .collapse-title {
        font-size: 30px;
    }
    
    .collapse-content {
        font-size: 18px;
    }
    
    .collapse-author {
        font-size: 18px;
        color: #888888;
    }
    
    .collapse-created-time {
        font-size: 18px;
        color: #888888;
    }
    
    .thump-char {
        font-size: 18px;
        display: inline-block;
        margin-left: 15px;
    }
    
    .text {
        font-size: 14px;
    }
    
    .item {
        margin-bottom: 18px;
    }
    
    .box-card {
        width: 480px;
    }
    
    .el-main {
        line-height: 30px;
    }
</style>

<script>
    const axios = require('axios')
    export default {
        name: 'MessageIndex',
        data() {
            return {
                message_list: [],
                tabPosition: 'left',
                currentPage: 1,
                pagesize: 3,
                activeNames: ['1'],
                message_title: '',
                message_content: ''
            }
        },
        created() {
            // TOPO 读入数据
            var that = this
            axios({
                url: "http://backend.docker.io/BoardMessages/MessageIndex",
                method: 'get',
                params: {}
            }).then(res => {
                console.log(res.data)
                that.message_list = res.data.message_list
            }).catch(err => {
                console.log('message_list error!!')
            })
        },
        methods: {
            handleSizeChange: function(size) {
                this.pagesize = size
                console.log(this.pagesize)
            },
            handleCurrentChange: function(currentPage) {
                this.currentPage = currentPage
                console.log(this.currentPage)
            },
            thump_up: function(Message_id) {
                var that = this
                console.log(Message_id)
                console.log(that.$store.state.user_id)
                axios({
                    url: 'http://backend.docker.io/BoardMessages/Like',
                    method: 'get',
                    params: {
                        message_id: Message_id,
                        user_id: that.$store.state.user_id
                    }
                }).then(res => {
                    console.log(res.data)
                    if (res.data.messageSuccess === '1') {
                        // 注册成功
                        this.$message('点赞成功!')
                        window.location.reload()
                    } else if (res.data.messageSuccess == '2') {
                        this.$message('你已经点过赞或者踩，不可以再点啦!')
                    } else {
                        this.$message('点赞失败!')
                    }
                }).catch(err => {
                    console.log('thump-up error!')
                    console.log(err)
                })
            },
            thump_down: function(Message_id) {
                var that = this
                console.log(Message_id)
                console.log(that.$store.state.user_id)
                axios({
                    url: 'http://backend.docker.io/BoardMessages/Dislike',
                    method: 'get',
                    params: {
                        message_id: Message_id,
                        user_id: that.$store.state.user_id
                    }
                }).then(res => {
                    console.log(res.data)
                    if (res.data.messageSuccess === '1') {
                        // 注册成功
                        this.$message('点踩成功!')
                        window.location.reload()
                    } else if (res.data.messageSuccess == '2') {
                        this.$message('你已经点过赞或者踩，不可以再点啦!')
                    } else {
                        this.$message('点踩失败!')
                    }
                }).catch(err => {
                    console.log('thump-down error!')
                    console.log(err)
                })
            },
            messageSubmit: function() {
                var that = this
                axios({
                    url: 'http://backend.docker.io/BoardMessages/WriteMessage',
                    method: 'get',
                    params: {
                        title: that.message_title,
                        content: that.message_content,
                        user_id: that.$store.state.user_id
                    }
                }).then(res => {
                    console.log(res.data)
                    if (res.data.writeSuccess) {
                        // 成功写入信息
                        this.$message('提交成功!')
                        window.location.reload()
                    } else {
                        this.$message('提交失败!')
                    }
                }).catch(err => {
                    console.log('write error!!')
                })
            },
            messageClear: function() {
                var that = this
                that.message_title = ''
                that.message_content = ''
            },
            Logout: function() {
                // TOPO 登出
                // 清空sessionStorage
                sessionStorage.clear()
                    // 清空全局变量!
                this.$store.dispatch('actionLogout')
                axios({
                    url: 'http://backend.docker.io/BoardUsers/userLogout',
                    method: 'get',
                    params: {}
                }).then(res => {
                    console.log(res.data)
                    if (res.data.logoutSuccess) {
                        // 成功登出
                        this.$message('注销成功!')
                    } else {
                        this.$message('注销失败!')
                    }
                }).catch(err => {
                    console.log('logout error!!')
                })
            }
        }
    }
</script>