from libpath import *
import os

manifest_path = home+"/.mpu/manifests/"
world_path = home+"/.mpu/world"

def remove_orphans():
    # Add all installed packages to initial orphan list
    orphans = []
    with open(world_path, "r") as file:
        orphans = file.read().splitlines()

    new_orphans = orphans.copy()
    for file in orphans:
            # read all dependencies in manifest file and remove them from 'orphans' list 
            # to ensure no package will lose functionality after orphan removal
            open_file = open(manifest_path+"/"+file, "r")
            deps = open_file.read().splitlines()

            for dep in deps:
                try:
                    new_orphans.remove(dep)
                except:
                    pass

            # if file has dependencies, it is not an orphan.
            if(deps != []):
                try:
                    new_orphans.remove(file)
                except:
                    pass

        # resulting list contains only the packages that are not dependencies 
        # to other packages and that have no dependencies, which means: only orphan packages.

    print("Orphans: ", new_orphans)
    return new_orphans

remove_orphans()
