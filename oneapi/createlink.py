import os
fout = 'out'

with open(fout, 'r') as ff:
    for i in ff:
        i = i.strip()
        dirshit, dirsrc = i.split()
        dot,dirdst,ver = dirshit.split('/')
        src = dirsrc
        dst = '2022.1/'+dirdst+'/'+ver
#		print(src+'->'+dst)
#		print(dirsrc+'->'+ver+'->'+dirdst)
        try:
                os.symlink(src, dst)
        except OSError as error:
                print(error)

        directory = dir
        parent_dir = '2022.1'
        mode = 755
        path = os.path.join(parent_dir, directory)
        try:
                os.mkdir(path, mode)
        except OSError as error:
                print(error)
