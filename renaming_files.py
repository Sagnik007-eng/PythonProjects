import os
v=1
for i in os.listdir(r'C:\Users\SagnikBhattacharya\Desktop\files\nestedfolder'):
    name=str(v)+i.split('.')[0]
    ext=i.split('.')[1]
    p='.'
    os.rename(f'C:/Users/SagnikBhattacharya/Desktop/files/nestedfolder/{i}',f'C:/Users/SagnikBhattacharya/Desktop/files/nestedfolder/{name}{p}{ext}')
    v=v+1

"""
This program renames a list of files in a folder
"""