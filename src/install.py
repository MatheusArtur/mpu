# Installation utility for the MPU-package manager, written by LC

# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation; either version 3, or (at your option) any later
# version.

# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General
# Public License for more details.

# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.


from pathlib import Path
import os, errno, sys, glob


home = str(Path.home())
manifest_path = str(str(home)+"/.mpu/manifests/")
packages_repository = "https://gitlab.com/mpu-pkg-manager/mpu-packages"
dependency_list_path = str(str(home)+"/.mpu/")
dependency_list = []

# class PackagesInstallation:

def install_packages(user_input):

	if os.path.exists(str(manifest_path)) == False:
		sys.exit("You should first update MPU - use 'main.py update'")

	if not (user_input):
		sys.exit("You should enter at least one package name - use 'main.py install YourPackageName'")

	for package in user_input:

		dependency_list_file = open(dependency_list_path+"dependency_list-"+str(package)+".txt", "w")
		dependency_list_file.write("")

		similarity = [os.path.basename(x) for x in glob.glob(manifest_path+package+'-[0-9]*')]

		for match in similarity:
			dependency_checks(match, package)




def dependency_checks(package, user_input):

	if not package in dependency_list:
		dependency_list.append(package)
		with open(dependency_list_path+"dependency_list-"+str(user_input)+".txt", "a") as file:
			file.write(str(package)+"\n")

		print()
		print("Checking dependencies of > "+ str(package))

		if os.path.isfile(manifest_path+package) == True:
			# sys.exit("The manifest "+package+" doesn't exist.")

			with open(manifest_path+package) as file:
				line = file.readline()

				while line:
					dependency = line.strip()
					print("- {}".format(dependency))
					dependency_checks(str(dependency+'.mpu'), user_input)
					line = file.readline()

				file.close()