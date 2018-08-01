import boto3

instances = [i for i in boto3.resource('ec2', region_name='ap-southeast-2').instances.all()]
key1 = 'sample'
# Print instance_id of instances that do not have a Tag of Key=sample
for i in instances:
  if key1 not in [t['Key'] for t in i.tags]:
    print i.instance_id
