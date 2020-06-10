#!/usr/bin/python

import subprocess, time, sys
from i3ipc import *

i3 = Connection()

def update():
	tree = i3.get_tree()
	scratchpad = tree.scratchpad()
	focused = tree.find_focused()
	workspace = focused.workspace()
	return scratchpad, workspace

def activate():
	scratchpad, workspace = update()
	for container in scratchpad:
		container.command('scratchpad show')
		container.command('floating toggle')
	i3.command('restart')

def deactivate():
	scratchpad, workspace = update()
	for container in workspace.floating_nodes:
		container.command('move scratchpad')

if sys.argv[1] == "activate":
	activate()
elif sys.argv[1] == "deactivate":
	deactivate()
