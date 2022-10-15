# import AWS boto3 library 
import boto3 
region='us-east-1
ec2 = boto3.client('ec2,region_name='region')
a= ec2.describe_instances()

#search for all running instances
instances =ec2.instances.all (Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

#Create a list to store all instances that are running
all_running_instances = []
specific_tag = 'Dev'
for instance in instances:

    #store all running instances
    all_running_instances.apppend(instance)

    #Tagged instances to ensure certain instances are stopped
    if instance.tags !=None:
        for tags in instance.tags:
        
        #
        