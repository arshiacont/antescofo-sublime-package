# antescofo-sublime-package
Antescofo Language Package and Plugins for Sublime Text Editor 2 and 3.

Using [pyOSC](https://trac.v2.nl/wiki/pyOSC) package for Sublime Text 2 and [Python-OSC](https://github.com/attwad/python-osc) for Sublime Text 3 (automatically) for communications to *Antescofo* objects in Max/Pd.

Change *Antescofo.sublime-settings* to use non-default network parameters (we use 'localhost' on port 5678 by default).

## Installation

- Download the ZIP archive from the link above
- Move the resultant 'Antescofo' folder to '~/Library/Application Support/Sublime Text 2/Packages/' (same with Sublime Text 3)

## Usage

### Open Antescofo Communication

Open *Antescofo* in either Max or Pd and initiate OSC communication from the object by sending 'ascograph open' to the object (or double-clicking on *Antescofo* object in case of Max).

### Syntax Coloring

By openning an Antescofo file with '.asco' or '.asco.txt' extension, the *Antescofo* syntax is automatically detected. You should see this at the bottom-right corner of the Sublime Text Editor. If not, just click there and choose *Antescofo*.
Additionally, you should choose your favourite color scheme from 'Preferences -> Color Schemes -> Antescofo' (Courtesy of [Julia Blondeau](http://www.juliablondeau.fr/)!) 

### Hot-Keys

The following short cuts are currently available on all platforms. You can easily change them by modifying the 'Default (OSX).sublime-keymap' file in the plugin folder (and other platforms accordingly). They are also available in the 'Tools' menu.

- alt+p without text selection will evaluate the line in Antescofo (will send OSC message to Antescofo with 'livecode' prepend)
- alt+p with text selection will do the above on the entire selected text.
- alt+s : to 'start' Antescofo
- alt+c : to 'stop' Antescofo

## Problems or Suggestions?

Create an [Issue](https://github.com/arshiacont/antescofo-sublime-package/issues) and we will get back to you swiftly!