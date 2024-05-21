import os

os.system('ls /dev/i2c-*')
os.system('i2cdetect -r -y 3')
os.system('echo ds3231 0x68 | sudo tee  /sys/class/i2c-adapter/i2c-3/new_device')
os.system('ls /dev/rtc*')
os.system('hwclock -r -f /dev/rtc1')
os.system('apt-get install ntp -y')
os.system('sudo service ntp start')
os.system('hwclock -r -f /dev/rtc1')
os.system('timedatectl')
os.system('touch /etc/rc.local')
os.system('chmod 777 /etc/rc.local')