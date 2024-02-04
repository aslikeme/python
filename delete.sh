#! /bin/bash

trash=~/trash
fileName="$1"
archName="$fileName".gz
inode=$(stat -c '%i' $fileName)
tmpFile="/tmp/deletesh.tmpFile"

if [ $# -ne 1 ]
then
    echo " Enter file name "
    exit 1
fi

mkdir -p $trash
find $trash -type f -mtime +2 -delete

if [ ! -f $fileName ]
then
    echo " File $fileName does not exist "
    exit 1
fi

if [ -f $trash/$archName ]
then
    echo "File $archName already exist "
    exit 1
fi

if [ -L $fileName ]
then
        realPath=$(readlink $fileName)
        unlink $fileName
        echo "$fileName was a sim link to a $realPath"
        exit 0
fi

find / -inum $inode 2> /dev/null > $tmpFile

if [ $(cat $tmpFile | wc -l) -ge 2 ]
then
        rm $fileName
        echo "The deleted file was a hardlink. There is a one more file with same inode:"
        echo $(grep -v $fileName $tmpFile
        )
        rm $tmpFile

        exit 0
fi
gzip -c $fileName > $trash/$archName && rm $fileName  || echo "Something went wrong"