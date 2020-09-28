#! /bin/bash

mkdir tmp
cd tmp
mkdir 'hello world'
cd 'hello world'
touch absolute.txt
echo "hello world!" > absolute.txt
cat -A absolute.txt
cd ..
cd ..
ls -lh ./tmp/'hello world'
