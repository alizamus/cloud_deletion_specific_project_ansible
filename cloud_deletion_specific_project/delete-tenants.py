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
	predef_tenants = ['admin','demo','service','invisible_to_admin']
	tenants = []
	tenants_id = []
	tenants_list = keystone.tenants.list()
	if tenants_list:
		for i in range(len(tenants_list)):
			if tenants_list[i].name not in predef_tenants:
				if tenants_list[i].name == project_name:
					tenants_list[i].delete()


if __name__ == "__main__":
    main(sys.argv[1:])		
