[toc]

# About the repo
 docker + Django + DRF + Vuejs `(vue-cli project)` project.


# 使用流程
第一次使用:
  - `docker-compose build` or `docker-compose up --build`
开始使用容器:
  - `docker-compose up`

Django建表:
  - `docker-compose run backend migrate`

Docker Createsuperuser:
  - `docker exec -ti <对应container id> /bin/bash` 后 `django-admin createsuperuser`即可, container id 可以在用`docker ps`查询

添加如下信息到hosts
```
127.0.0.1 frontend.docker.io
127.0.0.1 backend.docker.io
127.0.0.1 production.docker.io
```


# 目录结构

  - 文件 `docker-compose.yml`: containers settings
  - 目录 `dockerfiles`: 
    -  `backend`: Django + DRF
    -  `vuejs`: Vuejs + Webpack + NPM ==
    -  `nginx`: 即nginx相关
  - 文件 `Pipfile` 和 `Pipfile.lock`: [Pipenv](https://pipenv.readthedocs.io/en/latest/) 文件
  - 目录 `src`:
    - 目录 `backend`: Django + DRF project.
    - 目录 `frontend`: Vuejs webpack project.   
   - 目录 `nginx`:
    - 文件 `backend.conf`: 转发8002端口.  
    - 文件 `frontend_develop`: 转发8080端口.  
    - 文件 `frontend_production`: 挂载`npm run build`的文件.  

# 关于后端


## Django 相关

  > Question:  如何运行`manage.py` 相关指令
  - Answer: 

    `docker-compose run backend <any manage.py option >`

    如 你想运行 `manage.py` help, 则应该输入

    `docker-compose run backend help`

   类似的

  `docker-compose run backend showmigrations`

   `python manage.py shell` =>  
    `docker-compose run backend shell`

  > Question: 如何运行 `django-admin`相关指令 
  - Answer: 

    同上, `docker-compose run backend django-admin <options>`
	
	
# 关于项目使用

## 关于前端

- 使用`127.0.0.1:8080`或者 `frontend.docker.io`(hosts配置)访问网页

- 该网页包含用户注册 登录 写留言 注销 查看留言 点赞点踩等操作

- 注意，用户写留言需要在留言版页面的最左侧点击Tabs切换 

- 查看留言详细部分需要点击相应版块才能展开查看，我写了留言的详细信息哦，一定要点击对应部分展开才能看到详细信息

- 注销按键在右上角

- 点赞点踩按钮一定要在页面展开后才可以看到！

## 关于后端

- 可以利用url测试api端口，因为采用了GET的数据传输方式!

## 关于项目启动

见上面项目的构建方式
