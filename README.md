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


# How to mount data(MySQL 5.6)  
mysql> create database nekko;      # 创建数据库  
mysql> use nekko;                  # 使用已创建的数据库  
mysql> set names utf8;             # 设置编码  
mysql> source xxx.sql;             # 导入备份数据库  
