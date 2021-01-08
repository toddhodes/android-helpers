#!/usr/bin/env python

import subprocess
import sys
import os

from common_utils import do_input

DEVICES_START = "List of devices attached"


def main():
    args = sys.argv[1:]
    if args:
        runAdbCommand(args)


def runAdbCommand(args):
    if runDevicelessCommands(args):
        return
    devices = getDeviceList()
    if devices is None:
        print("couldn't get list of devices")
    else:
        count = len(devices)
        if count == 0:
            print("no devices attached")
        elif count == 1:
            runOnDevice(devices[0], args)
        else:
            print("More than one device attached...")
            for i in range(0, count):
                print("(%d) %s" % (i + 1, devices[i]))
            print("(%d) Run on all" % (count + 1))
            input = do_input("Choose device: ")
            while not input.isdigit() or not (0 < int(input) <= count + 1):
                input = do_input("No such option, choose again: ")
            input = int(input)
            if input > count:
                runOnAllDevices(devices, args)
            else:
                runOnDevice(devices[input - 1], args)


def getDeviceList():
    out = subprocess.Popen(['adb', 'devices'], stdout=subprocess.PIPE).communicate()[0]
    if DEVICES_START not in out:
        return None
    index = out.index(DEVICES_START) + len(DEVICES_START) + 1
    devices = out[index:]
    devices = devices.split(os.linesep)
    devices = filter(None, devices)
    devices = [d[:d.index("\t")] for d in devices]
    return devices


def runOnAllDevices(devices, args):
    for device in devices:
        runOnDevice(device, args)


def runOnDevice(device, args):
    if args[0] == 'enter':
        inputText(device, args)
        return
    command = ['adb', '-s', device] + args
    print("Running: " + " ".join(command))
    out = subprocess.Popen(command, stdout=subprocess.PIPE).communicate()[0]
    print(out)


def inputText(device, args):
    for text in args[1:]:
        print("text: " + text)
        if text == 'next':
            runOnDevice(device, ['shell', 'input', 'keyevent', '66'])
        else:
            runOnDevice(device, ['shell', 'input', 'text', text])


def runDevicelessCommands(args):
    if not args:
        out = subprocess.Popen(['adb'], stdout=subprocess.PIPE).communicate()[0]
        print(out)
        return True

    command = args[0]
    if command in ["devices", "connect"]:
        out = subprocess.Popen(['adb', command], stdout=subprocess.PIPE).communicate()[0]
        print(out)
        return True

    return False


main()
