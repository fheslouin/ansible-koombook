# Ansible-koombook
Ansible directory for KoomBook package and configuration file

From your computer, first install ansible 
 - ```sudo apt-get install ansible```
then 
 - Clone the repository 
 - modify those 2 files: 
  - hosts (with ip adress of your server) 
  - groups_vars/all complete the variables to suit your need
 - Deploy the script with: ```ansible-playbook -i hosts -l pull_mode_hosts  -u root ansible_pull.yml```

What does it do: 
Ansible-playbook copy a playbook and all the server to install, then each server use ansible-pull to automaticly pull the git hub repository and use the playbook to install all the package and configuration files
