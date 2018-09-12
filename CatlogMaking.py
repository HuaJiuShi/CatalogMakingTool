#!/usr/bin/python
#-*- coding:utf-8 -*-

'''
Software Instruction:
使用python对文件目录进行索引，自动创建文件索引，并在Catalog文件夹中保存为*.xls以及*.txt文件
Index file directories with Python
'''

import os

tabs = ''
tab1 = '----'
dirLayerNum = 0

#递归调用，实现子文件夹的完全检索
def checkDeeperDir(presDir,writeFile):
    if(os.path.exists(presDir)):
        global tabs,tab1,dirLayerNum
        dirLayerNum += 1
        paths = os.listdir(presDir)
        if paths:
            for path in paths:
                if os.path.isdir(os.path.join(presDir,path)):
                    for i in range(dirLayerNum-1):
                        tabs = tabs + tab1
                    print(tabs + path)
                    writeFile.write(tabs + path + '\n')
                    tabs = ''
                    chechDirFiles(os.path.join(presDir,path),writeFile)
                    checkDeeperDir(os.path.join(presDir,path),writeFile)
            dirLayerNum -= 1
            return 1
        else:
            dirLayerNum -= 1
            return 0
    else:
        print('Error:No Directory!!!')
        
def chechDirFiles(presDir,writeFile):
    if(os.path.exists(presDir)):
        global tabs,tab1,dirLayerNum
        files = os.listdir(presDir)
        if files:
            for i in range(dirLayerNum):
                tabs = tabs + tab1
            for file in files:
                if os.path.isfile(os.path.join(presDir,file)):
                    print(tabs + file)
                    writeFile.write(tabs + file + '\n')
            tabs = ''
                    
def main():
    readroot = os.getcwd()
    try:
        catalogTxt = open('catalog.txt','w')
        checkDeeperDir(readroot,catalogTxt)
    finally:
        catalogTxt.close()  #确保文件被关闭
    
if __name__ == '__main__':
    main()
    
    

