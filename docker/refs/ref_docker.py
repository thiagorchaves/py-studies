#!/usr/bin/env python3

import docker

docker_con = docker.DockerClient("tcp://0.0.0.0:2376")

container = docker_con.containers.run(
    'debian', '/bin/bash',
    name="learn", detach=True,
    tty=True, ports={'5000/tcp':'5000'}
)
print(container.id)
print(container.image.tags[0])
print(container.name)
print(container.short_id)
print(container.status)

#print(docker_con.version())