#!/bin/bash

#expr $quelBail : ".*order\=\(.*\) HTT.*" |sed "s/%3D/=/g" |base64 --decode

input=""
while IFS= read -r line
do
  echo -e "`expr "$line" : ".*order\=\(.*\) HTT.*" |sed "s/%3D/=/g" |base64 --decode`\n\n"
done < "$input"