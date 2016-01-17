import sublime, sublime_plugin
import sys
import os

pyosc = 1
# pyosc is the folder in our plugin
if sys.version_info < (3, 3):
    sys.path.append(os.path.join(os.path.dirname(__file__), "pyosc"))
    import OSC
else:
    # pythonosc
    sys.path.append(os.path.join(os.path.dirname(__file__), "python-osc-1.4.2"))
    from pythonosc import osc_message_builder
    from pythonosc import udp_client
    pyosc = 0

# Extends CMD+SHIFT+p to use OSC to send to Antescofo  
class OscsendCommand(sublime_plugin.TextCommand):  
    def run(self, edit):
        self.settings = sublime.load_settings('Antescofo.sublime-settings')
        address = self.settings.get('antescofoip', 'localhost')    
        port = self.settings.get('antescofoport', 5678)    
        # Walk through each region in the selection  
        for region in self.view.sel():
            # If no region, then just send the line!
            if region.empty():  
                # Expand the region to the full line it resides on, excluding the newline  
                line = self.view.line(region) 
                # Extract the string for the line, and add a newline  
                Contents = self.view.substr(line) + '\n'
            else :
                # if region, then send the region
                # Get the selected text  
                Contents = self.view.substr(region) + '\n'

            # Send OSC message
            if pyosc:
                ## Send using pyosc
                client = OSC.OSCClient()
                client.connect((address, port))
                oscmsg = OSC.OSCMessage('/antescofo/cmd')
                oscmsg.append('playstring')
                oscmsg.append(Contents)
                client.send(oscmsg)
            else :
                client = udp_client.UDPClient(address, port)
                oscmsg = osc_message_builder.OscMessageBuilder(address = "/antescofo/cmd")
                oscmsg.add_arg("playstring")
                oscmsg.add_arg(Contents)
                oscmsg = oscmsg.build()
                client.send(oscmsg)



# ctrl+s to START Antescofo via OSC 
class StartantescofoCommand(sublime_plugin.WindowCommand):  
    def run(self):
        print('Starting Antescofo...')
        self.settings = sublime.load_settings('Antescofo.sublime-settings')
        address = self.settings.get('antescofoip', 'localhost')    
        port = self.settings.get('antescofoport', 5678)    
        if pyosc:
            ## Use pyosc
            client = OSC.OSCClient()
            client.connect((address, port))
            oscmsg = OSC.OSCMessage("/antescofo/cmd")
            oscmsg.append('start')
            client.send(oscmsg)
        else:
            ## use pythonosc
            client = udp_client.UDPClient(address, port)
            oscmsg = osc_message_builder.OscMessageBuilder(address = "/antescofo/cmd")
            oscmsg.add_arg("start")
            oscmsg = oscmsg.build()
            client.send(oscmsg)

# ctrl+s to START Antescofo via OSC 
class StopantescofoCommand(sublime_plugin.WindowCommand):  
    def run(self):
        print('Stop Antescofo...')
        self.settings = sublime.load_settings('Antescofo.sublime-settings')
        address = self.settings.get('antescofoip', 'localhost')    
        port = self.settings.get('antescofoport', 5678) 
        if pyosc:
            ## Use pyosc
            client = OSC.OSCClient()
            client.connect((address, port))
            oscmsg = OSC.OSCMessage("/antescofo/cmd")
            oscmsg.append('stop')
            client.send(oscmsg)
        else:
            ## use pythonosc
            client = udp_client.UDPClient(address, port)
            oscmsg = osc_message_builder.OscMessageBuilder(address = "/antescofo/cmd")
            oscmsg.add_arg("stop")
            oscmsg = oscmsg.build()
            client.send(oscmsg)

# ctrl+l to load current file in Antescofo
class Loadantescofo(sublime_plugin.WindowCommand):
    def run(self):
        if sublime.version()==u'2221':
            print('Can not load file in ST2')
        else:
            self.settings = sublime.load_settings('Antescofo.sublime-settings')
            address = self.settings.get('antescofoip', 'localhost')    
            port = self.settings.get('antescofoport', 5678) 

            ascographip = self.settings.get('ascographip', 'localhost') 
            ascographport = self.settings.get('ascographport', 6789) 

            filename = self.window.extract_variables()['file']
            print('Antescofo Loading ', filename)
            ## use pythonosc
            # Send to Antescofo object in Max/Pd
            client = udp_client.UDPClient(address, port)
            oscmsg = osc_message_builder.OscMessageBuilder(address = "/antescofo/cmd")
            oscmsg.add_arg("score")
            oscmsg.add_arg(filename)
            oscmsg = oscmsg.build()
            client.send(oscmsg)
            # Send to AscoGraph if any
            ascoclient = udp_client.UDPClient(ascographip, ascographport)
            oscmsg2 = osc_message_builder.OscMessageBuilder(address = "/antescofo/loadscore")
            oscmsg2.add_arg(filename)
            oscmsg2 = oscmsg.build()
            ascoclient.send(oscmsg2)
                
