import boto3

boto3.setup_default_session(profile_name='prod')

ec2 = boto3.resource('ec2', region_name='us-east-1')
client = boto3.client('ec2', region_name='us-east-1')

volumes = ec2.volumes.all()
# volumes = ec2.volumes.filter(Filters=[{'Name': 'status', 'Values':['in-use', 'available']}])
volume_stt = [v.id for v in volumes if v.state == 'available']
for id in volume_stt:
  response = client.delete_volume(
    VolumeId=id,
    DryRun=False
  )
  print(response)


