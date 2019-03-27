#!/usr/bin/env python3

import docker

docker_con = docker.DockerClient("tcp://0.0.0.0:2376")

learn_container = docker_con.containers.get("learn")
print(learn_container.exec_run("ls -la"))