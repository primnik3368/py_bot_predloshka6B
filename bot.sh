cd py_bot_predloshka6B
pkg update && pkg upgrade
pkg install screen
pkg install termux-api
termux-wake-unlock
git pull
screen python main.py
