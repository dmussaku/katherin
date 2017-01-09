# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"

  # config.vm.network "forwarded_port", guest: 8000, host: 8080 # Mapping application port
  # config.vm.network "forwarded_port", guest: 6379, host: 6379 # Mapping redis port
  # config.vm.network "forwarded_port", guest: 3306, host: 3306 # Mapping mysql port
  
  config.vm.synced_folder "./katherin", "/www/katherin"

  config.vm.provision "docker"
  
  # Pull MySQL docker images and create container for storing db data
  config.vm.provision "shell", inline: <<-SHELL
    sudo docker pull mysql:5.7
    sudo docker create --name "mysql-data" -v /var/lib/mysql mysql:5.7
  SHELL
end
