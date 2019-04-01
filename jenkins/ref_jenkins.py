#!usr/bin/env python3

import jenkins

jenkins_con = jenkins.Jenkins(
    'http://127.0.0.1:8080',
    username= '4linux', password='4linux123'
)

# --Criando job e XML
# jenkins_con.create_job('Python-Job', jenkins.EMPTY_CONFIG_XML)

# --Printando user e versão Jenkins
# print(jenkins_con.get_whoami())
# print(jenkins_con.get_version())

# -- Rodando Job e printando resultado
# queue = jenkins_con.build_job('Python-Job')
# print(jenkins_con.get_queue_item(queue))

# -- Listando Jobs
# print(jenkins_con.get_jobs())

# -- Recuperando Config
# print(jenkins_con.get_job_config('Python-Job'))

# -- Alterar Config Job
jenkins_con.reconfig_job('Python-Job', jenkins.EMPTY_CONFIG_XML)