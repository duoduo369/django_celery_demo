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
