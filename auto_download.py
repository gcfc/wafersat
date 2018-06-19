#!/usr/bin/python

# run this script from your computer after configuring ssh, see below

# ------------------------------------------------------------------
# Problem
# as length of download file increases, download speed will decrease
# ------------------------------------------------------------------

# script to automatically download file being generated by pi_stats script
# run script from directory you want to save the file in
# or customize path for your computer
# scp automatically overwrites existing files
# will require generating ssh key before hand to automate
# view https://alvinalexander.com/linux-unix/how-use-scp-without-password-backups-copy
# to see how to configure your computer and pi to communicate with eachother
# pi@18.111.18.58 is the current username and ip address of the pi 1/30/18

from subprocess import call
from time import sleep

print('File will be downloaded to current directory')
filename = input('Enter filename to download [do not include full path]: ')

while True:
    sleep(1)
    call(['scp', '-i', '~/.ssh/id_rsa', 'pi@18.111.18.58:/home/pi/WaferSat/' + filename, '.'])