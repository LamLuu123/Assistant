import os
import subprocess as sp

paths = {
    'word': "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\WINWORD.EXE",
    'discord': "C:\\Users\LUONG VAN LAM\\AppData\\Local\\Discord\\app-1.0.9004\\Discord.exe",
    'calculator': "C:\\Windows\\System32\\calc.exe",
    'excel': "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\EXCEL.EXE",
    'powerpoint':"C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
}


def open_word():
    os.startfile(paths['word'])

def open_excel():
    os.startfile(paths['excel'])

def open_pp():
    os.startfile(paths['powerpoint'])

def open_discord():
    os.startfile(paths['discord'])


def open_cmd():
    os.system('start cmd')


def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)


def open_calculator():
    sp.Popen(paths['calculator'])
