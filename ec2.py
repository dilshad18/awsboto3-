#!/bin/python
import boto3
import csv
with open ('ec2.csv', 'w') as f:
	writer = csv.writer(f)
	writer.writerow (['instance id','instance_type','region','instance.public_ip','instance.private_ip','instance_status'])
	client = boto3.client('ec2', region_name='us-east-1')
	ec2_regions = [region['RegionName'] for region in client.describe_regions()['Regions']]
	for region in ec2_regions:
		conn = boto3.resource('ec2',region_name=region)
		instances = conn.instances.filter()
		for instance in instances:
			if instance.state["Name"] == "running" or instance.state["Name"] == "stopped":
				data = (instance.id,instance.instance_type,region,instance.public_ip_address,instance.private_ip_address,instance.state['Name'])
				writer.writerow(data)
	f.close()
