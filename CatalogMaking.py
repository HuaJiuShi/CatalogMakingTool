#!/usr/bin/python
#-*- coding:utf-8 -*-

'''
Software Instruction:
使用python对文件目录进行索引，自动创建文件索引，并在Catalog文件夹中保存为*.txt文件
Index file directories with Python
'''

import os
import argparse

tabs = ''
tab1 = ''
dirLayerNum = 0

#递归调用，实现子文件夹的完全检索，并写入目录文件
def checkDeeperDir(presDir,writeFile):
    if(os.path.exists(presDir)):
        global tabs,tab1,dirLayerNum
        dirLayerNum += 1
        paths = os.listdir(presDir)
        if paths:
            chechDirFiles(presDir,writeFile)
            for path in paths:
                if os.path.isdir(os.path.join(presDir,path)):
                    for i in range(dirLayerNum-1):
                        tabs = tabs + tab1
                    print(tabs + path)
                    writeFile.write(tabs + path + '\n')
                    tabs = ''
                    checkDeeperDir(os.path.join(presDir,path),writeFile)
            dirLayerNum -= 1
            return 1
        else:
            dirLayerNum -= 1
            return 0
    else:
        print('Error:No Directory!!!')
        
#检索当前文件夹下所有文件，并写入目录文件
def chechDirFiles(presDir,writeFile):
    if(os.path.exists(presDir)):
        global tabs,tab1,dirLayerNum
        files = os.listdir(presDir)
        if files:
            for i in range(dirLayerNum-1):
                tabs = tabs + tab1
            for file in files:
                if os.path.isfile(os.path.join(presDir,file)):
                    print(tabs + file)
                    writeFile.write(tabs + file + '\n')
            tabs = ''
            
def get_commandline_options():
    parser = argparse.ArgumentParser()

    parser.add_argument('-d', '--directory',
                        help='Making catalog of the directory(selected/default)',
                        action='store',
                        type=int,
                        dest='directory',
                        default=0)    #默认当前目录

    parser.add_argument('-m', '--mark',
                        help='set the mark to fill the tab',
                        action='store',
                        type=str,
                        dest='mark',
                        default=' ')    #默认空格填充
    
    parser.add_argument('-s', '--save',
                        help='set the file to save the catalog',
                        action='store',
                        type=str,
                        dest='save',
                        default='catalog.txt')

    opts = parser.parse_args()
    return opts
    
    
def main():
    opts = get_commandline_options()
    if opts.directory == 0:     #default
        readroot = os.getcwd()
    elif opts.directory == 1:   #selected
        readroot = input('Please Input the Dir: ')
    global tab1
    for i in range(4):
        tab1 = tab1 + opts.mark
    print('Catalog Dir: %s' %(readroot))
    print('Save File  : %s' %(os.path.join(readroot,opts.save)))
    print("Mark: '%s'" %(opts.mark))
    
    try:
        catalogTxt = open(os.path.join(readroot,opts.save),'w')
        checkDeeperDir(readroot,catalogTxt)
    finally:
        catalogTxt.close()  #确保文件被关闭
    
if __name__ == '__main__':
    main()
    
