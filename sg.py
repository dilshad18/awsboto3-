#!/bin/python
import boto3
import csv

with open ('sg.csv', 'w') as f:
	writer = csv.writer(f)
	writer.writerow(['All SG','SGS attached to instances', 'Free SGS'])
	client = boto3.client('ec2',region_name='ap-south-1')
	ec2_regions = [region['RegionName'] for region in client.describe_regions()['Regions']]
	for region in ec2_regions:
		ec2 = boto3.resource('ec2', region_name=region) #You have to change this line based on how you pass AWS credentials and AWS config
		sgs = list(ec2.security_groups.all())
		insts = list(ec2.instances.all())
		all_sgs = set([sg.group_name for sg in sgs])
		all_inst_sgs = set([sg['GroupName'] for inst in insts for sg in inst.security_groups])
		unused_sgs = all_sgs - all_inst_sgs
		data =(all_sgs,all_inst_sgs,unused_sgs)
		writer.writerow(data)
	f.close()
#print 'Total SGs:', len(all_sgs)
#print 'All SGS', all_sgs
#print 'SGS attached to instances:', len(all_inst_sgs)
#print 'Orphaned SGs:', len(unused_sgs)
#print 'Unattached SG names:', unused_sgs
