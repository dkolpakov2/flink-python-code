


AWS Console connect to instance:

Failed to connect to your instance
EC2 Instance Connect is unable to connect to your instance. Ensure your instance network settings are configured correctly for EC2 Instance Connect.
 For more information, see Set up EC2 Instance Connect at
 https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-connect-set-up.html.
 
 Win SSH connect:
 
 Download PuTTY.exe to your computer from:
http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html
Start PuTTY.
In the Category list, click Session
In the Host Name field, type hadoop@ec2-3-87-186-208.compute-1.amazonaws.com
In the Category list, expand Connection > SSH > Auth
For Private key file for authentication, click Browse and select the private key file (ec2bastion_keypair.ppk) used to launch the cluster.
In the Category list, expand Connection > SSH, and then click Tunnels.
In the Source port field, type 8157 (a randomly chosen, unused local port).
Select the Dynamic and Auto options.
Leave the Destination field empty and click Add.
Click Open.
Click Yes to dismiss the security alert.

SSH connect Linux:
Open a terminal window. On Mac OS X, choose Applications > Utilities > Terminal. On other Linux distributions, terminal is typically found at Applications > Accessories > Terminal.
To establish an SSH tunnel with the master node using dynamic port forwarding, type the following command. 
Replace ~/ec2bastion_keypair.pem with the location and filename of the private key file (.pem) used to launch the cluster.
ssh -i ~/ec2bastion_keypair.pem -ND 8157 hadoop@ec2-3-87-186-208.compute-1.amazonaws.com
Note: Port 8157 used in the command is a randomly selected, unused local port.
Type yes to dismiss the security warning.

Step 2: Configure a proxy management tool - Learn more
Go to https://chrome.google.com/webstore/category/extensions, search for Proxy SwitchyOmega, and add it to Chrome.
Choose New profile and enter emr-socks-proxy as the profile name.
Choose PAC profile and then Create. Proxy Auto-Configuration (PAC) files help you define an allow list for browser requests that should be forwarded to a web proxy server.
In the PAC Script field, replace the contents with the following script that defines which URLs should be forwarded through your web proxy server. If you specified a different port number when you set up your SSH tunnel, replace 8157 with your port number.
function FindProxyForURL(url, host) {
    if (shExpMatch(url, "*ec2*.amazonaws.com*")) return 'SOCKS5 localhost:8157';
    if (shExpMatch(url, "*ec2*.compute*")) return 'SOCKS5 localhost:8157';
    if (shExpMatch(url, "http://10.*")) return 'SOCKS5 localhost:8157';
    if (shExpMatch(url, "*10*.compute*")) return 'SOCKS5 localhost:8157';
    if (shExpMatch(url, "*10*.amazonaws.com*")) return 'SOCKS5 localhost:8157';
    if (shExpMatch(url, "*.compute.internal*")) return 'SOCKS5 localhost:8157';
    if (shExpMatch(url, "*ec2.internal*")) return 'SOCKS5 localhost:8157';
    return 'DIRECT';
}
Under Actions, choose Apply changes to save your proxy settings.
On the Chrome toolbar, choose SwitchyOmega and select the emr-socks-proxy profile.
To open a web interface, enter the public DNS name of your primary or core node followed by the port number for your chosen interface into your browser address bar.

For a complete list of web interfaces on the primary node, see View Web Interfaces Hosted on Amazon EMR Clusters.

EMR Cluster Connect:
1. Download PuTTY.exe to your computer from: https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html 
2. Start PuTTY.
3. In the Category list, choose Session.
4. In the Host Name field, enter hadoop@ec2-3-236-215-249.compute-1.amazonaws.com
5. In the Category list, expand Connection > SSH, and then choose Auth.
6. For Private key file for authentication, choose Browse and select the private key file (ec2bastion_keypair.ppk) that you used to launch the cluster.
7. Select Open.
8. Select Yes to dismiss the security alert.

# add Restriction to PEM file:
# Fix the issue: 
# >> ec2_user@ec2-44-202-148-27.compute-1.amazonaws.com: Permission denied (publickey,gssapi-keyex,gssapi-with-mic).
# sudo su
chmod 400 ~/.aws/ec2bastion_keypair.pem

Connect to ec2 flink-cluster
## ssh user-fqdn@LinuxBastion-fqdn -L 2222:DESTINATION-EC2-IP:22
## BASTION: ssh -i "ec2bastion_keypair.pem" ec2-user@ec2-44-206-0-10.compute-1.amazonaws.com
## ssh ec2-user@ec2-44-206-0-10.compute-1.amazonaws.com -L 2222:DESTINATION-EC2-IP:22
 ssh -i "ec2bastion_keypair.pem" ec2-user@ec2-44-206-0-10.compute-1.amazonaws.com -L 2222:ec2-44-202-84-33.compute-1.amazonaws.com:22
 # new Bastion:
 IP: ec2-44-212-76-66.comp bastion only for my ip 99.93.13.10
	chmod 400 ec2bastion_keypair.pem
	## ssh -i "ec2bastionpem.pem" ec2-user@ec2-44-202-148-27.compute-1.amazonaws.com -L 2222:ec2-44-202-84-33.compute-1.amazonaws.com:22

Connect via Bastion:
 -Open an SSH client.
	Locate your private key file. The key used to launch this instance is ec2bastionpem.pem
  - Run this command, if necessary, to ensure your key is not publicly viewable!!!
		chmod 400 ec2bastionpem.pem
  -Connect to your instance using its Public DNS:
		ec2-44-212-76-66.compute-1.amazonaws.com
Example:
	ssh -i "ec2bastionpem.pem" ec2-user@ec2-44-212-76-66.compute-1.amazonaws.com	
  -Then connect to Flink cluster: Private IP/Hostname type: ip-172-31-81-152.ec2.internal

Flink Public IP: 44.202.84.33  DNS:  ec2-44-202-84-33.compute-1.amazonaws.com
  
		ssh ec2-user@ec2-44-212-76-66.compute-1.amazonaws.com -L 2222:ec2-44-202-84-33.compute-1.amazonaws.com:22
		
   ## You can Work remotely now ###
   -----------------------------------------------
  -Then upload file  Open separate SSH:
	## establish connection first: -> ssh user-fqdn@LinuxBastion-fqdn -L 2222:DESTINATION-EC2-IP:22
	# Flink IP: 44.202.84.33
	ssh -i "ec2bastionpem.pem" ec2-user@ec2-44-212-76-66.compute-1.amazonaws.com -L 2222:ec2-44-202-84-33.compute-1.amazonaws.com:22
   ## scp -i ~/c/Lana/.aws/ec2bastionpem.pem ~/Desktop/MS115.fa  ubuntu@ec2-54-166-128-20.compute-1.amazonaws.com:~/data/
   ## bad ->scp -i ~/c/Lana/.aws/ec2bastionpem.pem flink-1.16.1-bin-scala_2.12.tar ec2-user@ec2-44-202-84-33.compute-1.amazonaws.com:~/flink
   ## Good to transfer fie -> scp -P 2222 Source-File-Path user-fqdn@localhost:
	scp -P 2222 flink1161binscala.tar ec2-user@localhost:
   ## Good to transfer Folder -> scp -r -P 2222 MY-FILE-SOURCE-PATH MY-FQDN@localhost:
	scp -r -P 2222 flink-1.16.1 ec2-user@localhost:
   ## Download: 
	scp -i ~/Desktop/amazon.pem ubuntu@ec2-54-166-128-20.compute-1.amazonaws.com:/data/ecoli_ref-5m-trim.fastq.gz ~/Download/
	
	## With winCSP
	-bastion: 54.159.218.213 "ec2ppk-key" ec2-54-159-218-213.compute-1.amazonaws.com
	
	
	## Basstion PPK:
	Open Putty, under Host Name, put the public IP address of your Bastion host, and specify Port 22.
	Under SSH->Auth:
	Select the .PPK file as the private key for authentication
	Check the box marked “Allow Agent Forwarding”
	Under SSH->Tunnels
	Source port: Choose a local port which is not being used on your machine, for example 6000.
	Destination port: Input <Internal IP Address of EC2 Machine flink-cluster: 44.202.84.33>:22 and click Add.
	
	ec2-54-159-218-213.compute-1.amazonaws.com 54.159.218.213
	
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Flink flink-ec2cluster ->  i-031cb6aca6e974665  Private: ip-172-31-68-123.ec2.internal  
>> PUBLIC: ec2-3-81-27-218.compute-1.amazonaws.com

chmod 400 ~/.aws/ec2bastion_keypair.pem
ssh -i "ec2bastion_keypair.pem" ec2-user@ec2-3-81-27-218.compute-1.amazonaws.com:22
-i ~/.aws/ec2bastion_keypair.pem private
# BAD -> ssh -i "ec2bastion_keypair.pem" ec2-user@ec2-44-202-148-27.compute-1.amazonaws.com  -L 2222:ip-172-31-68-123.ec2.internal:22
ssh -i "ec2bastion_keypair.pem" ec2-user@ec2-44-202-148-27.compute-1.amazonaws.com  -L 2222:ec2-3-81-27-218.compute-1.amazonaws.com:22
## transfer the file:
	scp -P 2222 Source-File-Path user-fqdn@localhost:
## Transfer folder:
	scp -r -P 2222 flink-1.16.1 ec2-user@ec2-3-81-27-218.compute-1.amazonaws.com:22
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# Small Mem... i-03e98ff23030e8703 (flink-cluster)->   ec2-44-202-84-33.compute-1.amazonaws.com   private: ip-172-31-81-152.ec2.internal
# Flink-ec2 Public IPv4 DNSPublic IPv4 DNS c5alarge =2x4Gb = 0.07  IP name: ip-172-31-64-159.ec2.internal
ssh -i "ec2bastion_keypair.pem" ec2_user@ec2-44-202-148-27.compute-1.amazonaws.com -L 2222 ec2_user@ec2-3-238-205-99.compute-1.amazonaws.com:22  
>>>>>>
# i-08ce88847e4fa58c6 ecbastionpem   ->   ec2-44-212-76-66.compute-1.amazonaws.com            private: ip-172-31-92-156.ec2.internal
# i-0c08dd71651da9ffa (bastionppk)   ->   ec2-54-159-218-213.compute-1.amazonaws.com  private: 172.31.88.8 ip-172-31-88-8.ec2.internal
# i-06fa5d7f2adefa2db (bastion-2ecbkey)-> ec2-44-202-148-27.compute-1.amazonaws.com  private: ip-172-31-91-83.ec2.internal

Connect to Flink SSH ->
 ssh -i "ec2bastionpem.pem" ec2-user@ec2-44-212-76-66.compute-1.amazonaws.com -L 2222:ec2-44-202-84-33.compute-1.amazonaws.com:22
 ssh -i "ec2bastionpem.pem" ec2-user@ec2-44-202-84-33.compute-1.amazonaws.com:22

 ssh -i ec2bastion_keypair.pem ec2-44-202-148-27.compute-1.amazonaws.com  -L 2222:ec2-44-202-84-33.compute-1.amazonaws.com:22
 ==============================================================================================================
 - 1. Add docker to ec2:
 sudo yum update
 sudo yum search docker
 sudo yum info docker
 sudo yum install docker
 >>> outcome message: >>> Created symlink /etc/systemd/system/sockets.target.wants/docker.socket → /usr/lib/systemd/system/docker.socket.
# Add group membership for the default ec2-user so you can run all docker commands without using the sudo command:
	sudo usermod -a -G docker ec2-user
	id ec2-user
# Reload a Linux user's group assignments to docker w/o logout
	newgrp docker 
# Add docker-compose	
	sudo yum install python3-pip
	sudo pip3 install docker-compose # with root access
	# OR # without root access for security reasons
	pip3 install --user docker-compose 
# OR->
	wget https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m) 
	sudo mv docker-compose-$(uname -s)-$(uname -m) /usr/local/bin/docker-compose
	sudo chmod -v +x /usr/local/bin/docker-compose

# Enable docker service at AMI boot time:
	sudo systemctl enable docker.service
# Start the Docker service:
	sudo systemctl start docker.service	
# Verifiction:
	sudo systemctl status docker.service	

# Add docker path to bash startup file ~/.profile or ~/.bash using exprot command:
	echo "$PATH"	
	export PATH=$PATH:/usr/local/bin
	
##### How to control docker service
## Use the systemctl command as follows:

	sudo systemctl start docker.service #<-- start the service
	sudo systemctl stop docker.service #<-- stop the service
	sudo systemctl restart docker.service #<-- restart the service
	sudo systemctl status docker.service #<-- get the service status	
	
## Create test web-site:
	mkdir static-website-1
	cd static-website-1
	# use the echo command to create new index.html for project:
	echo 'Docker Apache static test site' > index.html
	vim Dockerfile
	
	## copy-paste next:
		FROM rockylinux/rockylinux:latest
 
		MAINTAINER DK
		LABEL Remarks="Linux test image for installing static webpage with Apache2"
		 
		# Install apache2 with less
		RUN yum -y update && \
		yum -y install httpd && \
		yum clean all
		 
		# Sample index.html for test 
		COPY index.html /var/www/html/index.html
		 
		# Port and set entry point for container 
		EXPOSE 80
		ENTRYPOINT /usr/sbin/httpd -DFOREGROUND
		
# build docker image:
	sudo docker build -t staticsite01 .		
	sudo docker images
	sudo docker run -d -p 80:80 --name staticsite01  staticsite01   ## --rm <image>  ## Automatically remove the container when it exits ## --rm doesn't work with --restart always
	sudo docker ps -a  #docker ps returns only running containers and needs -a for listing even the stopped ones. 
	sudo docker port staticsite01
	curl 127.0.0.1:80
	# >>>
	docker run staticsite01 # Run a command in a **new** container
	docker start staticsite01 # Start one or more stopped containers
	docker stop staticsite01
	# For each container do:
	 sudo docker stop container_ID
	 sudo docker rm container_ID
	 docker rm <container name>
	# removing all exited containers:
	 docker rm $(docker ps -a -f status=exited -q)	
	
# For specific client examples please see the man page for the specific Docker command using the man command. For instance:
	man docker-build
	man docker-run	
	
### Install and Run Flink docker:
	FLINK_PROPERTIES="jobmanager.rpc.address: jobmanager"	
	docker network create flink-network

	docker run \
    --rm \
    --name=jobmanager \
    --network flink-network \
    --publish 8081:8081 \
    --env FLINK_PROPERTIES="${FLINK_PROPERTIES}" \
    flink:latest jobmanager
	## external address jobmanager:6123, bind address 0.0.0.0:6123.	
	
### Connect to other ssh:
	ssh -i "/C/Users/Lana/.aws/ec2bastion_keypair.pem" ec2-user@ec2-44-202-84-33.compute-1.amazonaws.com
	#
	docker run \
    --rm \
    --name=taskmanager \
    --network flink-network \
    --env FLINK_PROPERTIES="${FLINK_PROPERTIES}" \
    flink:latest taskmanager
	>> [java.net.ConnectException: Connection refused: cdf9ab930654/172.18.0.3:6123]
	

	
## Add clipboard:
	vim --version
	>> If you see "+xterm_clipboard", you are good to go.
	>>>
 system vimrc file: "/etc/vimrc"
     user vimrc file: "$HOME/.vimrc"
 2nd user vimrc file: "~/.vim/vimrc"
      user exrc file: "$HOME/.exrc"
       defaults file: "$VIMRUNTIME/defaults.vim"
 fall-back for $VIM: "/usr/share/vim"
	## rebuild vim
	sudo yum build-dep vim

## Install GIT:	
	https://linux.how2shout.com/how-to-install-git-on-aws-ec2-amazon-linux-2/#3_Install_git_in_Amazon_EC2_instance
	
	git clone https://github.com/dkolpakov2/flink-python-code.git
	sudo yum install git
	mkdir dkgit
	git init
	ls -a .git/
	
## check python:
	sudo python3 --version	
## install pip and EB CLI:
	curl -O https://bootstrap.pypa.io/get-pip.py
	python3 get-pip.py --user
	echo $SHELL
	export PATH=LOCAL_PATH:$PATH
	## Load the profile script 
	source ~/PROFILE_SCRIPT
	pip --version
	## install EB CLI:
	pip install awsebcli --upgrade --user
	eb --version
	
	more -l README.md 

## Install Java 8
	sudo yum install -y git
	wget --no-cookies --no-check-certificate --header "Cookie: gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-cookie" "http://download.oracle.com/otn-pub/java/jdk/8u131-b11/d54c1d3a095b4ff2b6607d096fa80163/jdk-8u131-linux-x64.tar.gz"
	tar -xzvf jdk-8u131-linux-x64.tar.gz
	rm -rf jdk-8u131-linux-x64.tar.gz
	# Configure Java_home
	sudo vim ~/.bashrc
	alias cls='clear'
	sudo export JAVA_HOME=~/jdk1.8.0_131
	echo "export "JAVA_HOME"="~/jdk1.8.0_131>>~/.bashrc
	echo "export "JAVA_HOME"="~/jdk1.8.0_131>>~/.profile
	export JRE_HOME=~/jdk1.8.0_131/jre
	echo "export "JRE_HOME"="~/jdk1.8.0_131/jre>>~/.bashrc
	echo "export "JRE_HOME"="~/jdk1.8.0_131/jre>>~/.profile
	export PATH=$PATH:~/jdk1.8.0_131/bin:/~/jdk1.8.0_131/jre/bin
	export PATH=$PATH:~/jdk1.8.0_131/bin:/~/jdk1.8.0_131/jre/bin
	
	source ~/.bashrc 
	source ~/.profile
	java -version

## Install Apache Flink:
 pip install apache-flink==1.17.0	
 pip install widgetsnbextension --upgrade
 pip install jupiter
 pip install nltk
 LANGUAGE="" LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8 jupiter notebook
 
 ## ERROR:
 ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. 
	This behaviour is the source of the following dependency conflicts.
	awscli 2.9.19 requires prompt-toolkit<=3.0.29,>=3.0.24, but you have prompt-toolkit 3.0.38 which is incompatible.
	
	[esc]:set prompt
	
## Create cert (will need mkcert):
mkcert \
>  -cert-file flink.local.crt \
>  -key-file flink.local.key \
>  flink.local

## 	Fix ec2 deployment config issue:
rest.port: 8081
rest.addres: localhost
rest.bind-address: 0.0.0.0


