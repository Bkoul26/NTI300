#!/bin/bash
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
