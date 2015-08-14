#!/usr/bin/python

from keystoneclient.v2_0 import client as kclient
from novaclient import client as nclient
import sys
import os
import getopt

def main(argv):
	try:
		opts, args = getopt.getopt(argv, "ha:p:", ["help", "admin_pass=", "project_name="])
	except getopt.GetoptError:                                
	        sys.exit(2)
	
	for opt, arg in opts:       
	        if opt in ("-h", "--help"):        
	                sys.exit()        
	        elif opt in ("-a", "--admin_pass"):
	                admin_pass = arg
	        elif opt in ("-p", "--project_name"):
	                project_name = arg
	
	
	keystone = kclient.Client(username='admin', password=admin_pass , tenant_name='admin', auth_url="http://127.0.0.1:5000/v2.0")
	predef_tenants = ['admin','demo','service','invisible_to_admin','services']
	tenants = []
	tenants_id = []
	tenans_list = keystone.tenants.list()
	for i in range(len(tenans_list)):
		if tenans_list[i].name not in predef_tenants:
			if tenans_list[i].name == project_name:
				tenants.append(str(tenans_list[i].name))
				tenants_id.append(str(tenans_list[i].id))
	
	predef_users = ['admin','demo','nova','heat','glance','cinder','neutron']
	for tenant in tenants_id:
		keystone_user = kclient.Client(username='admin', password=admin_pass , tenant_id=tenant, auth_url="http://127.0.0.1:5000/v2.0")
		#print keystone_user.users.list(tenant)
		users_list = keystone_user.users.list(tenant)
		if users_list:
	                for i in range(len(users_list)):
				if users_list[i].username not in predef_users:
					users_list[i].delete()

if __name__ == "__main__":
    main(sys.argv[1:])
