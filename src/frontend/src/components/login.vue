<template>
    <el-container style="margin-top: 80px;">
        <el-main class="content-center">
            <el-card class="box-card">
                <div slot="header" class="clearfix">
                    <span>登录</span>
                </div>
                <div class="text item">
                    <el-input placeholder="请输入账号" v-model="account" maxlength='18' clearable></el-input>
                </div>
                <div class="text item">
                    <el-input placeholder="请输入密码" v-model="password" maxlength='18' show-password></el-input>
                </div>
                <el-row>
                    <el-button type="primary" @click="userLogin()">
                        登录
                    </el-button>
                    <el-button type="primary" @click="dialogVisible = true">
                        注册
                    </el-button>
                </el-row>
            </el-card>
            <el-dialog title="注册" :visible.sync="dialogVisible" width="30%" :before-close="handleClose">
                <div class="text item">
                    <el-input placeholder="请输入账号(6-18位数字/字母/下划线)" v-model="register_account" maxlength='18' clearable></el-input>
                </div>
                <div class="text item">
                    <el-input placeholder="请输入密码(6-18位数字/字母/下划线)" v-model="register_password" maxlength='18' show-password></el-input>
                </div>
                <div class="text item">
                    <el-input placeholder="请输入用户名(4-20位数字/字母/下划线)" v-model="register_username" maxlength='20' clearable></el-input>
                </div>
                <el-button @click="dialogVisible = false">取 消</el-button>
                <el-button type="primary" @click="userRegister()">确 定</el-button>
            </el-dialog>
        </el-main>
    </el-container>
</template>

<script>
    const axios = require('axios')
    export default {
        name: 'UserLogin',
        data() {
            return {
                account: '',
                password: '',
                dialogVisible: false,
                register_account: '',
                register_password: '',
                register_username: ''
            }
        },
        methods: {
            userLogin: function() {
                var that = this
                axios({
                    url: 'http://backend.docker.io/BoardUsers/userLogin',
                    method: 'get',
                    params: {
                        account: that.account,
                        password: that.password
                    }
                }).then(res => {
                    console.log(res.data)
                    if (res.data.is_login === '1') {
                        this.$store.dispatch('actionLogin', res.data)
                        sessionStorage.setItem("account", res.data.account)
                        sessionStorage.setItem("is_login", res.data.is_login)
                        sessionStorage.setItem("username", res.data.username)
                        sessionStorage.setItem("user_id", res.data.user_id)
                    } else {
                        this.$message('账号或者密码错误!')
                    }
                }).catch(err => {
                    console.log("login error!!")
                })
            },
            userRegister: function() {
                // TOPO 注册按钮
                var that = this;
                axios({
                    url: 'http://backend.docker.io/BoardUsers/userRegister',
                    method: 'get',
                    params: {
                        username: that.register_username,
                        account: that.register_account,
                        password: that.register_password
                    }
                }).then(res => {
                    console.log(res.data)
                    if (res.data.registerSuccess === '1') {
                        // 注册成功
                        this.$message('注册成功!')
                    } else if (res.data.registerSuccess == '0') {
                        this.$message('注册失败!请检查你的账号，密码和用户名格式')
                    } else {
                        this.$message('这个账号已经存在!')
                    }
                }).catch(err => {
                    console.log('register error!')
                })
                that.dialogVisible = false
            }
        }
    }
</script>

<style scoped>
    .content-center {
        display: flex;
        flex-direction: row;
        justify-content: center;
        align-items: center;
    }
    
    .text {
        font-size: 14px;
    }
    
    .item {
        margin-bottom: 18px;
    }
    
    .clearfix:before,
    .clearfix:after {
        display: table;
        content: "";
    }
    
    .clearfix:after {
        clear: both
    }
    
    .box-card {
        width: 480px;
    }
</style>