# make dir
mkdir ~/.mpu
# copy all files
cp * ~/.mpu -r
# aliases
#cat .bashrc >> ~/.bashrc
#cat .bash_profile >> ~/.bash_profile
echo "alias mpu=\"python3 ~/.mpu/src/main.py\"">> ~/.bashrc
# reload bash
. ~/.bashrc
# important directories and files
mkdir ~/.mpu/packages
mkdir ~/.mpu/log
touch ~/.mpu/world
