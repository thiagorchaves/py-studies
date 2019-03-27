#!/usr/bin/env python3

import docker

docker_con = docker.DockerClient("tcp://0.0.0.0:2376")

for container in docker_con.containers.list(all=True):
    print(container)