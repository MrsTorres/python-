import boto3

region='us-east-1'
ec2 = boto3.client ('ec2',region_name='region')



#search for all running instances
instances =ec2.instances.all (Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

#Create a list to store all instances that are running
all_running_instances = []
specific_tag = 'Dev'
for instance in instances:

    #store all running instances
    all_running_instances.append(instance)

    #Tagged instances to ensure certain instances are stopped
    if instance.tags !=None:
        for tags in instance.tags:
            
         #Dev instances tag
            if tags ["Key"] == specific_tag:
        
                #Remove instance with specific tag running
                all_running_instances.remove(instance)
            
#print(all_running_instances)
for specific in all_running_instances:
    print(f'Stopping EC2 instance: {specific.id}')
    specific.wait_until_stopped()
    print(f'EC2 instance "{specific.id}" has been stopped')