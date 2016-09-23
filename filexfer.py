import shutil
import os
import datetime
import time
import sqlite3


def checkMTime(directory, dstdir,conn):
    #establish database connection
    c = conn.cursor()
    timesta = time.time()
    datestamp = str(datetime.datetime.fromtimestamp(int(time.time())).strftime('%Y-%m-%d %H:%M:%S'))
    c.execute("INSERT INTO cTimes (date, checktime) VALUES(?,?)",(datestamp, timesta))
    conn.commit()
    #walk through folder and compare last edit against 24 hours
    for root, dirs, fils in os.walk(directory):
        for fil in fils:
            filpath = os.path.join(root, fil)
            mt = os.path.getmtime(filpath)
            if mt > (timesta - 86400):
                shutil.move(filpath, dstdir)
            else:
                print fil + " is older than 24 hours."
        

def get_filepaths(directory):
    #add full file paths to file path array
    file_paths = []
    for root, directories, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)
    return file_paths
 
full_file_paths = get_filepaths("C:\\Users\\User\\Desktop\\home office")
    
def xferFile():
    for file_ in full_file_paths:
        print file_
        shutil.move(file_, "C:\\Users\\User\\Desktop\\satellite")


