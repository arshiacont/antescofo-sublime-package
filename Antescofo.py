import sublime, sublime_plugin
import sys
import os

# pyosc is the folder in our plugin
sys.path.append(os.path.join(os.path.dirname(__file__), "pyosc"))
import OSC

# Extends CMD+SHIFT+p to use OSC to send to Antescofo  
class OscsendCommand(sublime_plugin.TextCommand):  
    def run(self, edit):          
        # Walk through each region in the selection  
        for region in self.view.sel():
            # If no region, then just send the line!
            if region.empty():  
                print 'Region is empty'
                # Expand the region to the full line it resides on, excluding the newline  
                line = self.view.line(region) 
                # Extract the string for the line, and add a newline  
                lineContents = self.view.substr(line) + '\n'
                ## Send using pyosc
                client = OSC.OSCClient()
                client.connect(('localhost', 5678))
                oscmsg = OSC.OSCMessage('/antescofo/cmd')
                oscmsg.append('livecode')
                oscmsg.append(lineContents)
                client.send(oscmsg)
                print oscmsg
            else :
                print 'Region is not empty'
                # if region, then send the region
                # Get the selected text  
                RegionContents = self.view.substr(region) + '\n'
                ## Send using pyosc
                client = OSC.OSCClient()
                client.connect(('localhost', 5678))
                oscmsg = OSC.OSCMessage('/antescofo/cmd')
                oscmsg.append('livecode')
                oscmsg.append(RegionContents)
                client.send(oscmsg)
                print oscmsg



# ctrl+s to START Antescofo via OSC 
class StartantescofoCommand(sublime_plugin.WindowCommand):  
    def run(self):
        print 'Starting Antescofo...'
        client = OSC.OSCClient()
        client.connect(('localhost', 5678))
        oscmsg = OSC.OSCMessage("/antescofo/cmd")
        oscmsg.append('start')
        client.send(oscmsg)
        print oscmsg

# ctrl+s to START Antescofo via OSC 
class StopantescofoCommand(sublime_plugin.WindowCommand):  
    def run(self):
        print 'Starting Antescofo...'
        client = OSC.OSCClient()
        client.connect(('localhost', 5678))
        oscmsg = OSC.OSCMessage("/antescofo/cmd")
        oscmsg.append('stop')
        client.send(oscmsg)
        print oscmsg
                
