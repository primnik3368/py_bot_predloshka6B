#!/bin/bash
echo start install
pkg install python3
pip3 install -r -q requirements.txt
mv bot.sh ..
cd ..
chmod +x bot.sh
echo install is done.
echo exit...