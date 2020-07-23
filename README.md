# Azure-Custom-Image

## Set Up
 # Create a Ubuntu VM
az group create -n Custom-Image-RG -l location
az vm create -g Custom-Image-RG -n CustomVM -l location --Image UbuntuLTS --ssh-key-values .ssh/id_rsa.pub

ssh IP ADDRESS

 # Set Up VM Image
sudo apt update 
sudo apt install python3-pip 
cd Azure-Custom-Image
sudo pip3 -r requirements.txt
vim /tmp/app.service
        [Unit]
        Description=App start up

        [Service]
        ExecStart=/usr/bin/python3 /home/user/Azure-Custom-Image/app.py

        [Install]
        WantedBy=multi-user.target
sudo cp /tmp/app.service /etc/systemd/system/app.service 
sudo systemctl deamon-reload
sudo systemctl start app
sudo systemctl status app
sudo waagent -deprovision+user -force
exit

## Create VM Image
az vm deallocate -g Custom-Image-RG -n CustomVM 
az vm generalize -g Custom-Image-RG -n CustomVM 
az image create -g Custom-Image-RG -n Custom-Image --source CustomVM

## New VM
az vm create -g Custom-Image-RG -n CustomVM2 -l location --image Custom-Image --ssh-key-values .ssh/id_rsa.pub
