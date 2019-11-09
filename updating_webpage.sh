#!/bin/bash

time=$(date)                                                                                                        # Set variable time equal to date
echo "<html><body><h1>Hi there, it is $time, how are you?</h1></body></html>" > /var/www/html/pages.dir/page2.html  # Update page2 of website with new date&time
