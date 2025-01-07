#!/bin/bash
echo start install
pkg install python3
pip install -r -q requirements.txt
mv bot.sh ..
cd ..
echo install is done.
echo exit...