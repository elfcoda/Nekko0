# Nekko0

# command in docker elfcoda/django:1.0.5 on vps
0] start
1] run3 &

# to start the docker
docker run -ti --network=host 97 bash (97 is image id)
# and attach
docker attach 3d  (3d is container id)

# to stop the server
0] ps aux | grep python3 |grep runserver | awk '{print $2}' | xargs | xargs kill -9
