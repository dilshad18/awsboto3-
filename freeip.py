#!/bin/python
import boto3
import csv

with open('eip.csv', 'a') as f:
	writer = csv.writer(f)
	writer.writerow (['EIP','AllocationID','Type'])
	client = boto3.client('ec2',region_name='ap-south-1')
	ec2_regions = [region['RegionName'] for region in client.describe_regions()['Regions']]
	for region in ec2_regions:
		client = boto3.client('ec2',region_name= region)
		addresses_dict = client.describe_addresses()
		for eip_dict in addresses_dict['Addresses']:
			if "NetworkInterfaceId" not in eip_dict:
				#print("Eip %s Addrr %s Type %s") %(eip_dict['PublicIp'],eip_dict.get('AllocationId', 'NA'),eip_dict('Domain'))
				data = (eip_dict['PublicIp'],eip_dict.get('AllocationId', 'NA'), eip_dict['Domain'])
				writer.writerow(data)
				#print "{}, {}, {}".format(eip_dict['PublicIp'],eip_dict.get('AllocationId', 'NA'), eip_dict['Domain'])
				
f.close()

