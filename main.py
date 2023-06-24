import os
import tkinter as tk
import subprocess
from tkinter import filedialog
from tkinter import ttk
import shutil

# --- functions ---
def chooseFile():
    print('Please choose .log file:\n')
    fullpath = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("Log file", "*.log*"), ("all files", "*.*")))
    print('file chosen: ', fullpath)
    return fullpath


def extractor():
    logFile = open(str(fullPath))
    g = open('temp.txt', 'a')
    for k in logFile:
        splitK = k.split(',')
        # print(splitK)
        if 'dump <common_logger>: "IPv6"' in k:
            g.write(k)
        elif splitK[0] == '"IPv6"':
            g.write(k)
        elif 'dump <common_logger>: "IPv4"' in k:
            g.write(k)
        elif splitK[0] == '"IPv4"':
            g.write(k)
    logFile.close()
    g.close()


def stringinator(splitK):
    str1 = ""
    for ele in splitK:
        str1 += ele
    return str1


def espWriter():
    g = open('temp.txt')
    j = open('esp_sa', 'a')
    i = 1
    for k in g:
        splitK = k.split(' ')
        while '<common_logger>:' in splitK:
            splitK.pop(0)
        h = stringinator(splitK)
        j.write(h)
        if i == 4:
            j.write('\n')
        i = i + 1
    g.close()
    j.close()


def getUser():
    username = os.getlogin()
    espPath = "C:/Users/" + str(username) + "/AppData/Roaming/Wireshark/esp_sa"
    return espPath


def espOverwriter():
    file = open(wireSharkPath, 'r+')
    for _ in file:
        file.write(' ')
    file.close()
    file = open(wireSharkPath, 'a')
    g = open('esp_sa')
    for line in g:
        file.write(line)
    file.close()
    g.close()

def deleteChecker():
    if os.path.exists('esp_sa'):
        os.remove('esp_sa')
    elif os.path.exists('temp.txt'):
        os.remove('temp.txt')


# --- main ---
wireSharkPath = getUser()
deleteChecker()
print('please choose the required ip-simlib.log file: ')
fullPath = chooseFile()
print(fullPath, ' is the chosen file.')
f = open(str(fullPath), 'r')
extractor()
espWriter()
if os.path.exists('temp.txt'):
    os.remove('temp.txt')
espOverwriter()
print('esp_sa overwritten')

