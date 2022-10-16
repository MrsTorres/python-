import boto3

ec2 = boto3.resource('ec2', region_name='us-east-1')

def stopped_environment_instances(ec2):
   running_environment_instances = ec2.instances.filter(Filters=[{'Name':'instance-state-name', 'Values': ['running']},{'Name': 'tag:Environment','Values':['Dev']}])
   for instance in running_environment_instances:
        id=instance.id
        ec2.instances.filter(InstanceIds=[id]).start()
        if("i-0bcff0540f6c6f743" !=id):
            ec2.instance.filter(InstanceIds=[id]).stop()
print("All Environment:Dev Instances are now stopped.")
print("All other department instances are still running.")

if __name__ == "_main_":
    stopped_environment_instances(ec2)