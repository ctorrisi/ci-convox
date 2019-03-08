#!/usr/bin/python

import sys,subprocess

args = sys.argv

if len(args) < 3:
    print('Usage: update-env-vars org rack [vars]')
    exit(1)

org = args[1]
rack = args[2]

def runCommand(cmd):
    full =  cmd + ' --rack {}/{}'.format(org, rack) 
    p = subprocess.Popen(full, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    p.wait()
    return p.stdout.readlines()

currentVars = {}
for line in runCommand('convox env'):
    kv = line.strip().split('=')
    currentVars[kv[0]] = kv[1]

newVars = {}
for i in range(3, len(args)):
    kv = args[i].strip().split('=')
    newVars[kv[0]] = kv[1]

addList = []
for key in newVars:
    if key not in currentVars or currentVars[key] != newVars[key]:
        addList.append(key + '=' + newVars[key])

if addList:
    envs = ' '.join(addList)
    runCommand('convox env set {}'.format(envs))
    print('Set environment variables: {}'.format(envs))

removeList = []
for key in currentVars:
    if key not in newVars:
        removeList.append(key)

if removeList:
    envs = ' '.join(removeList)
    runCommand('convox env unset {}'.format(envs))
    print('Unset environment variables: {}'.format(envs))

if not (addList or removeList):
    print('No changes to environment variables required')

sys.exit(0)
