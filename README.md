django-celery-demo
===

[celery介绍以及很多有用的文章技巧](https://github.com/duoduo369/skill_issues/blob/master/python/celery.issue.md)

依赖环境
---

    sudo apt-get install rabbitmq-server
    pip install -r requirements.txt # 注意里面可能不全，只是写了主要依赖的版本号

配置rabbitmq
---

查看rabbitmy用户

    sudo rabbitmqctl list_users

添加用户、vhost等

    sudo rabbitmqctl add_user tester tester
    sudo rabbitmqctl add_vhost tester_vhost
    sudo rabbitmqctl set_permissions -p tester_vhost tester ".*" ".*" "."

数据库建表
---
    python manage.py syncdb

单步用法
===

启动django
---

使用9000端口是为了不和flower冲突,当然flower也可以用其他端口

    ./manage runserver 9000

浏览器打开`http://127.0.0.1:9000/admin`,登录后进入`http://127.0.0.1:9000/admin/djcelery/periodictask/`,添加几个任务

启动celery
---

简单的命令

-B代表启动心跳

    ./manage.py celeryd -E -B -l info -c 2


使用flower查看
---

    ./manage.py celery flower --broker=amqp://tester:tester@localhost:5672/tester_vhost

浏览器打开`http://localhost:5555/`

简单用法
===
在这里你可以看到使用多个celeryd为没一个队列配置不同的进数目
注意-n参数可以让你拥有多个worker

    cd 到项目根目录
    sudo ln -s $(pwd) /opt
    cd /opt/django_celery_demo/supervisor
    ./run_supervisor.sh

    ./check_supervisor.sh 如果所有都在RUNNING这个状态下启动成功

    否则先./kill_supervisor.sh 杀掉supervisor进程后
    ps aux | grep python | grep 9000
    ps aux | grep flower
    看看是否有其他运行的进程，如果有则杀掉，重新./run_supervisor.sh

其他事件
===

关于celery beat
---
celery beat是与定时任务有关的
当你使用celery beat时需要启动beat,而主动触发(delay)则不需要

测试关闭celery beat view主动触发是否可以处理任务

    cd /opt/django_celery_demo/supervisor
    ./check_supervisor.sh

    进入supervisorctl后
    stop celerybeat

    curl localhost:9000/test_celery_app
    或者浏览器输入 localhost:9000/test_celery_app

    并在flower中 localhost:5555查看任务情况
