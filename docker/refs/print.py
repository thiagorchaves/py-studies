#!/usr/bin/env python3

import docker

docker_con = docker.DockerClient("tcp://0.0.0.0:2376")

learn_container = docker_con.containers.get("learn")
# learn_container.stats(stream=False)
learn_container.stop()
# learn_container.start()
# learn_container.attach()
learn_container.remove()
# print(learn_container.stats(stream=False))
