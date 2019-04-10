# make dir
mkdir ~/.mpu
# copy all files
cp .bash_profile ~/
cp * ~/.mpu -r
# aliases
echo "alias mpu=\"python3 ~/.mpu/src/main.py\"">> ~/.bashrc
# reload bash
bash -r
# important directories and files
mkdir ~/.mpu/packages
mkdir ~/.mpu/log
touch ~/.mpu/world
