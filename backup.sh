#!/bin/bash
####################################
#
# Backup to NFS mount script.
#
####################################

# What to backup.
backup_files="/home /var /srv /usr /etc /root /boot /opt /home/frank/”

# Where to backup to.
dest=“/media/BACKUP”

# Create archive filename.
day=$(date +%A)
hostname=$(hostname -s)
archive_file="$hostname-$day.tgz"

# Print start status message.
echo "Backing up $backup_files to $dest/$archive_file"
date

# Backup the files using tar.
tar czf $dest/$archive_file $backup_files

# Print end status message.
echo "Backup finished"


# Long listing of files in $dest to check file sizes.
ls -lh $dest
