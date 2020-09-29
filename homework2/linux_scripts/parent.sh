#! /bin/bash

cd ..
mkdir 'hello parent'
cd 'hello parent'
touch parent.txt
echo 'hello parent!' > parent.txt
cat parent.txt
ls -lh ../'hello parent'
