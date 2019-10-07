# encoding:UTF-8
import boto3
from datetime import datetime
import time

# Instanciando AWS BOTO
session = boto3.Session(profile_name='')
ec2 = session.resource('ec2')
client_ec2 = session.client('ec2')
client_autoscaling = session.client('autoscaling')
client_elb = session.client('elb')
client_elbv2 = session.client('elbv2')

# Declaração das variáveis
date_now = str(datetime.now().strftime('%Y%m%d%H%M'))
name_tag_ec2 = 'eiplus-prod-ec2-web'
name_tag_ec2_asg = 'eiplus-prod-ec2-asg-web'
name_tag_lc = 'eiplus-prod-lc'
name_ec2 = '{}-{}'.format(name_tag_ec2, date_now)
name_lc = '{}-{}'.format(name_tag_lc, date_now)
name_asg = 'eiplus-prod-asg-web'
sg_ec2 = ['sg-0edf8a73']

launch_config = None
image = None
INSERVICE = 'InService'


# def create_ami():
#     instances = ec2.instances.filter(
#         Filters=[{'Name': 'tag:Name', 'Values': [name_tag_ec2]}])

#     for instance in instances:
#         image = client_ec2.create_image(
#             DryRun=False,
#             InstanceId=instance.id,
#             Name=name_ec2,
#             Description=name_ec2,
#             NoReboot=True,
#         )
#     return image

# def instance_state(mim_inst):
#     instances = ec2.instances.filter(
#             Filters=[{'Name': 'tag:Name', 'Values': [name_tag_ec2_asg]}])

#     all_healthy = False
#     print(instances)
#     number_instances = mim_inst*2
#     number_healthy_instances = 0

#     while not all_healthy:

#         for instance in instances:
#             print(number_healthy_instances)
#             instance = ec2.Instance(instance.id)

#             if instance.state['Code'] == 16:
#                 number_healthy_instances += 1

#         if(number_healthy_instances == number_instances):
#             all_healthy = True
#             break

#     return True

def create_launch_configuration(ami_id):
    launch_config = client_autoscaling.create_launch_configuration(
        LaunchConfigurationName=name_lc,
        ImageId=ami_id,
        SecurityGroups=sg_ec2,
        UserData=user_data,
        InstanceType='c5.2xlarge',
        InstanceMonitoring={
            'Enabled': True
        },
        IamInstanceProfile='production_role',
        AssociatePublicIpAddress=True,
        BlockDeviceMappings=[{
            'Ebs':{
                'DeleteOnTermination':
            }
        }]
    )
    return launch_config


# def up_autoscaling(mim_inst, desired):
#     print("UP AUTOSCALING")
#     print(mim_inst)
#     print(desired)
#     autoscaling_config = client_autoscaling.update_auto_scaling_group(
#         AutoScalingGroupName=name_asg,
#         LaunchConfigurationName=name_lc,
#         MinSize=mim_inst,
#         MaxSize=25,
#         DesiredCapacity=desired,
#         TerminationPolicies=[
#             'OldestLaunchConfiguration',
#         ],
#     )
#     return autoscaling_config


# def decrease_autoscaling(mim_inst, desired):
#     autoscaling_decrease = client_autoscaling.update_auto_scaling_group(
#         AutoScalingGroupName=name_asg,
#         MinSize=mim_inst,
#         MaxSize=25,
#         DesiredCapacity=desired,
#         TerminationPolicies=[
#             'OldestLaunchConfiguration',
#         ],
#     )
#     return autoscaling_decrease


# def stop_instance():
#     instances = ec2.instances.filter(
#         Filters=[{'Name': 'tag:Name', 'Values': [name_tag_ec2]}])

#     instances.stop()


# def start_instance():
#     instances = ec2.instances.filter(
#         Filters=[{'Name': 'tag:Name', 'Values': [name_tag_ec2]}])

#     instances.stop()


# def check_elb(group_arn_target):
#     waiter = client_elbv2.get_waiter('target_in_service')

#     waiter.wait(
#         TargetGroupArn=group_arn_target,
#     )

#     return True

# def get_instance_numbers():
#     describe = client_autoscaling.describe_auto_scaling_groups(
#         AutoScalingGroupNames=[
#             name_asg,
#         ],
#         MaxRecords=100
#     )
#     for min in describe['AutoScalingGroups']:
#         asg_instance = min['MinSize']

#     return asg_instance


# def main():
#     print("## Criando AMI ##")
#     image = create_ami()

#     if image:
#         image_new = ec2.Image(image['ImageId'])
#         print("## Verificando o status da AMI ##")
#         while image_new.state != 'available':
#             print(image_new.state)
#             time.sleep(15)
#             image_new = ec2.Image(image['ImageId'])

#         if image_new.state == 'available':
#             print("## Criando Launch Configuration ## ")
#             create_launch_configuration(ami_id=image_new.id)
#             print("## Atualizando as instancias ##")
#             min_inst = get_instance_numbers()
#             asg_numb_inst = min_inst*2
#             up_autoscaling(mim_inst=asg_numb_inst, desired=asg_numb_inst)
#             print("## Aguardando as novas instancias  ##")
#             time.sleep(15)
#             if instance_state(mim_inst=min_inst*2):
#                 #Adicionar o ARN TARGET GROUP do ALB de produção
#                 time.sleep(60)
#                 print("## Verificando as instancias no ALB  ##")
#                 if check_elb(group_arn_target='arn:aws:elasticloadbalancing:us-east-1:092901710718:targetgroup/eiplus-prod-target-group/564395cbb9fcd61b'):
#                     print("## Reduz a quatindade de instancias ##")
#                     decrease_autoscaling(mim_inst=min_inst, desired=min_inst)


if __name__ == '__main__':
    main()
