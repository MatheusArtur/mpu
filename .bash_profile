# /etc/skel/.bash_profile

# This file is sourced by bash for login shells.  The following line
# runs your .bashrc and is recommended by the bash info pages.

export PATH="$(du $HOME/.mpu/packages/usr/bin | cut -f2 | tr '\n' ':')$PATH"

if [[ -z $DISPLAY ]] && [[ $(tty) = /dev/tty1 ]]; then exec ck-launch-session startx -- vt1; fi
if [[ -f ~/.bashrc ]] ; then
	. ~/.bashrc
fi
