#!/usr/bin/python
import boto3
import csv
with open('reserve_instance.csv','w') as f:
	writer = csv.writer(f)
	writer.writerow(['ReservedInstancesId','OfferingType','AvailabilityZone','InstanceType','InstanceCount','State','InstanceTenancy'])
	client = boto3.client('ec2',region_name='us-east-1')
	ec2_regions = [region['RegionName'] for region in client.describe_regions()['Regions']]
	for region in ec2_regions:
		client = boto3.client('ec2',region_name= region)
		response = client.describe_reserved_instances()
		for data in response['ReservedInstances']:
			output = (data['ReservedInstancesId'],data['OfferingType'],data['AvailabilityZone'],data['InstanceType'],data['InstanceCount'],data['State'],data['InstanceTenancy'])
			writer.writerow(output)

	f.close()
