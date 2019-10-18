#!/bin/bash
 
installed =yum($yum list installed "httpd")
yum list installed "httpd"
if [ z "$1"]; then
echo "This package is installed"
  exit 0;
  fi
  
  
  
 echo "Look for package? [Y,n]"
read input
if {{$input == "Y" || $input =="y"]]; then
  echo "Look for package"
  installed =yum($yum list installed $input || grep$1)
yum list installed $input
if [ z "$1"]; then
echo "This package is installed"
else
    echo "search terminated"
    exit 0;
 fi

  
  
  
  echo "Do that? [Y,n]"
read input
if [[ $input == "Y" || $input == "y" ]]; then
        echo "do that"
else
        echo "don't do that"
fi





if [-z " $1"]; then
echo "you didn't provide an argument"
  exit 0;
 fi
varname=$(systemctl status $1 | grep Active | awk '{print 2}')
varname2= "inactive"
if [$varname == $varname2]; then 
   echo "noooo"
else
 echo "My status is $status"
   fi
