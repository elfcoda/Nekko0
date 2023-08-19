# Nekko0

# command in docker elfcoda/django:1.0.5 on vps
0] start  
1] run3 &  
2] exec start_do.sh and sbash  

# start the docker & named nekko
docker run -ti --name=nekko --network=host 97 bash  (97 is image id)
# and attach
docker attach 3d  (3d is container id)

# stop the server
0] ps aux | grep python3 |grep runserver | awk '{print $2}' | xargs | xargs kill -9


# How to mount data
MySQL8.0设置远程访问权限 https://zhuanlan.zhihu.com/p/587097435  
修改MySQL配置文件的地址绑定  
修改服务器3306端口访问权限  
修改应用端连接数据库的IP  
高版本的MySQL需要添加skip-ssl在my.cnf然后重启service mysql restart以禁用SSL  
