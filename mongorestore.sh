#!/bin/bash
input=$1
backup_path="/home/nagaraju/Downloads/2019-01-25-110001/postedit-db-0-4/"
while IFS= read -r col_name
do
  echo $col_name
#  echo "mongorestore --db postedit-db-0-4 --collection $col_name $backup_path/$col_name.bson"
  mongorestore --db postedit-db-0-4 --collection "$col_name" "$backup_path/$col_name.bson"
done < "$input"
