#!/bin/bash
cd ~ 
rm bot.sh
echo start install
pkg update
pkg install expat
pkg install python3
pip install -r requirements.txt
mv bot.sh ..
cd ..
echo install is done.
echo exit...
