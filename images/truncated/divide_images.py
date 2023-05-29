import glob as glob
import sys
import shutil

pwd = '{}/'.format(sys.path[0])

images = [name.replace(pwd, '') for name in glob.glob(pwd+'*.png')]
print(len(images))

members = ['Mark', 'Christian', 'Jon', 'Chris', 'Quentin']
divvy = len(images)/ len(members)
print(divvy)

print(len(images))


#for member in members:
#    dir = pwd + '{}/'.format(member)
#    print("moving truncated images to {}'s directory".format(member))
#    for i in range(int(divvy)):
#        shutil.copy(pwd+images[i], dir)