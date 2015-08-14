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

	keystone = kclient.Client(username='admin', password=admin_pass, tenant_name='admin', auth_url="http://127.0.0.1:5000/v2.0")
	predef_tenants = ['admin','demo','service','invisible_to_admin','services']
	tenants = []
	tenans_list = keystone.tenants.list()
	for i in range(len(tenans_list)):
		if tenans_list[i].name not in predef_tenants:
			if tenans_list[i].name == project_name:
				tenants.append(str(tenans_list[i].name))
	#print tenants
	for tenant in tenants:	
		nova = nclient.Client(2,'admin', admin_pass, tenant, "http://127.0.0.1:5000/v2.0",service_type="compute")
		try:
			for i in range(len(nova.servers.list())):
				compute_list = nova.servers.list(i)
				#print compute_list
				#print compute_list[0].id
				nova.servers.delete(compute_list[i].id)
				#print compute_list
		except:
			command = 'keystone --os-username=admin --os-password=' + admin_pass + ' --os-tenant-name=admin --os-auth-url=http://127.0.0.1:5000/v2.0 ' + 'user-role-add --user=admin --tenant=' + tenant + ' --role=admin'
			os.system(command)
                        for i in range(len(nova.servers.list())):
                                compute_list = nova.servers.list(i)
                                #print compute_list
                                #print compute_list[0].id
                                nova.servers.delete(compute_list[i].id)
                                #print compute_list
	
if __name__ == "__main__":
    main(sys.argv[1:])
