# cloud_deletion_specific_project_ansible
This repository is to run Ansible code which delete specific project and its corresponding openstack and contrail changes.
1- You should run this python code in playbook directory to generate the necessary codes to delete the specific project.
python config.py
2- Then you shoud run command below to actually start deletion process.
ansible-playbook specific_project_deletion.yml
