#!/usr/bin/env python
# _*_ coding: utf8 _*_

import pyautogui

print ("Script para nmap\n")
ip = raw_input ("rhost: ")

pyautogui.typewrite("nmap -sC -sV ")
pyautogui.typewrite(ip)
pyautogui.typewrite(" -o result.txt")
