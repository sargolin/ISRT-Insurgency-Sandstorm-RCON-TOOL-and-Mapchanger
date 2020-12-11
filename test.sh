
#!/bin/bash
for i in $(cat filename | sed 's/^.*: //; s/,.*$//');
do
if  [[ $(( length "$i" )) == 3 ]];
        then
                echo "$i"
 fi
done