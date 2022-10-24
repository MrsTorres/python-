import boto3

#Code to get the SQS service resource
sqs = boto3.resource('sqs')

#Creating the queue, add a delay time of 3 seconds. Will create and return the queue instnace            
sqs_queue = sqs.create_queue(QueueName='wk15_sqsqueue', Attributes={'DelaySeconds': '3'})

print(sqs_queue.url)
print(sqs_queue.attributes.get('DelaySeconds'))
print(sqs_queue)