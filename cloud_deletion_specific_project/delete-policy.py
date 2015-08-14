#!/usr/bin/python

from keystoneclient.v2_0 import client as kclient
from novaclient import client as nclient
from neutronclient.neutron import client as neclient
import os
import csv
import getopt
import sys

def main(argv):
	try:
	        opts, args = getopt.getopt(argv, "ha:", ["help", "admin_pass=", "project_name="])
	except getopt.GetoptError:                                
	        sys.exit(2)
	
	for opt, arg in opts:       
	        if opt in ("-h", "--help"):        
	                sys.exit()        
	        elif opt in ("-a", "--admin_pass"):
	                admin_pass = arg
	        elif opt in ("-p", "--project_name"):
	                project_name = arg


	keystone = kclient.Client(username='admin', password=admin_pass, tenant_name='admin', auth_url="http://127.0.0.1:5000/v2.0")
	predef_tenants = ['admin','demo','service','invisible_to_admin','services']
	tenants = []
	tenants_id = []
	tenans_list = keystone.tenants.list()
	for i in range(len(tenans_list)):
		if tenans_list[i].name not in predef_tenants:
			if tenans_list[i].name == project_name:
				tenants.append(str(tenans_list[i].name))
				tenants_id.append(str(tenans_list[i].id))
	
	
	for tenant in tenants:
		res= os.system("/root/cloud_deletion_specific_project/cloud_deletion_specific_project/code/config --username admin --password " + admin_pass + " --tenant " + tenant +  " --api-server 127.0.0.1 show policy" + " > " + "/root/cloud_deletion_specific_project/cloud_deletion_specific_project/test.csv")
	
		with open('/root/cloud_deletion_specific_project/cloud_deletion_specific_project/test.csv', 'rb') as csvfile:
			rules = csv.reader(csvfile)
			for row in rules:
				a = str(row[0])
				b = a.split('    ',1)[1]
				c = a.split('    ',1)[0]
				comand = "/root/cloud_deletion_specific_project/cloud_deletion_specific_project/code/config --username admin --password " + admin_pass + " --tenant " + tenant +  " --api-server 127.0.0.1 delete policy " + "'" + b + "'"
				#print comand	
				os.system(comand)


if __name__ == "__main__":
    main(sys.argv[1:])
