# encoding:UTF-8
import boto3
from datetime import datetime
import time

# Instanciando AWS BOTO
boto3.setup_default_session(profile_name='xomp')
client_autoscaling = boto3.client('autoscaling')
# Declaração das variáveis
date_now = str(datetime.now().strftime('%Y%m%d%H%M'))
name_tag_lc = 'eiplus-prod-lc'
name_lc = '{}-{}'.format(name_tag_lc, date_now)
name_asg = 'eiplus-prod-asg-web'
sg_ec2 = ['sg-043cbd2522bfcc730']
user_data = '''
#!/bin/bash
service nginx start
chkconfig nginx on
sudo service amazon-cloudwatch-agent start
sudo chkconfig amazon-cloudwatch-agent on
rm -f /var/tmp/aws-mon/instance-id
service al-agent restart
sudo yum install -y perl-Switch perl-DateTime perl-Sys-Syslog perl-LWP-Protocol-https perl-Digest-SHA.x86_64
curl https://aws-cloudwatch.s3.amazonaws.com/downloads/CloudWatchMonitoringScripts-1.2.2.zip -O
unzip CloudWatchMonitoringScripts-1.2.2.zip && \
rm CloudWatchMonitoringScripts-1.2.2.zip && \
cd aws-scripts-mon
'''
launch_config = None
image = None
INSERVICE = 'InService'


response = client_autoscaling.create_launch_configuration(
    LaunchConfigurationName=name_lc,
    ImageId='ami-00eb20669e0990cb4',
    KeyName='thiagorc',
    SecurityGroups=sg_ec2,
    UserData=user_data,
    InstanceType='t2.micro',
    InstanceMonitoring={
        'Enabled': False
    },
    IamInstanceProfile='teste-ssm',
    AssociatePublicIpAddress=True,
    BlockDeviceMappings=[
        {
            'DeviceName': '/dev/xvda',
            'Ebs':{
                'VolumeSize': 40,
                'VolumeType': 'gp2',
                'DeleteOnTermination': True,
                'Iops': 120,
                'Encrypted': False
            }
        }
    ]
)
print (response)