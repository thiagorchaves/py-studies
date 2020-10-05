import boto3
import datetime


client = boto3.client('ec2',
                      region_name=os.getenv('AWS_REGION'),
                      aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                      aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))
    snapshots = client.describe_snapshots(OwnerIds=[''])
    for snapshot in snapshots['Snapshots']:
      a= snapshot['StartTime']
      b=a.date()
      c=datetime.datetime.now().date()
      d=c-b
      try:
        if d.days>10:
          id = snapshot['SnapshotId']
          client.delete_snapshot(SnapshotId=id)
      except Exception,e:
        if 'InvalidSnapshot.InUse' in e.message:
          print "skipping this snapshot"
          continue