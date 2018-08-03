import boto3

instances = [i for i in boto3.resource('ec2', region_name='us-east-1').instances.all()]
keys = ['key1','key2','key3']
# replace elements in keys with your keys
for i in instances:
  if i.tags:
    for key in keys:
      if key not in [t['Key'] for t in i.tags]:
        print i.instance_id+": "+key
  else:
    print("No tags found for: "+i.instance_id)
