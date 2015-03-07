import win32gui as gui # set window
import win32api as api # send keys

from win32con import WM_CHAR # write message

import pyHook # for key logging

dota = gui.FindWindow(None, "Dota 2")

api.PostMessage(dota, WM_CHAR, ord('T'), 0) # send a message T to window Dota 2

import pythoncom # pump messages

def OnKeyboardEvent(event):
	if event.WindowName.lower() == 'dota 2':
		print 'MessageName:',event.MessageName
		print 'Message:',event.Message
		print 'Time:',event.Time
		print 'Window:',event.Window
		print 'WindowName:',event.WindowName
		print 'Ascii:', event.Ascii, chr(event.Ascii)
		print 'Key:', event.Key
		print 'KeyID:', event.KeyID
		print 'ScanCode:', event.ScanCode
		print 'Extended:', event.Extended
		print 'Injected:', event.Injected
		print 'Alt', event.Alt
		print 'Transition', event.Transition
		print '---'

	# return True to pass the event to other handlers
	return True # false to block

# create a hook manager
hm = pyHook.HookManager()
# watch for all mouse events
hm.KeyDown = OnKeyboardEvent
# set the hook
hm.HookKeyboard()
# wait forever
pythoncom.PumpMessages()