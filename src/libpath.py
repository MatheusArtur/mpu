# Update utility for the MPU-package manager, written by Matheus Artur

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

home = str(Path.home())
log_path= str(home+"/.mpu/log/")
log_file= str(log_path+"update.log")
manifest_path = str(home+"/.mpu/manifests/")
#packages_repository = "https://gitlab.com/mpu-pkg-manager/mpu-packages"
dependency_list_path = str(home+"/.mpu/")
pack_path= str(home+"/.mpu/packages/")
src_path= str(home+"/.mpu/src/")
