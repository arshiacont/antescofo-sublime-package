# antescofo-sublime-package
[Antescofo Language](http://repmus.ircam.fr/antescofo) Package and Plugins for [Sublime Text Editor](http://www.sublimetext.com) v2 and v3.

Using [pyOSC](https://trac.v2.nl/wiki/pyOSC) package for Sublime Text 2 and [Python-OSC](https://github.com/attwad/python-osc) for Sublime Text 3 (automatically) for communications to *Antescofo* objects in Max/Pd.

Change *Antescofo.sublime-settings* to use non-default network parameters (we use 'localhost' on port 5678 for Antescofo object and port 6789 for Ascograph by default).

## Installation

### Using Package Control

- Make sure you have [Package Control](https://packagecontrol.io/installation) installed in your Sublime Text
- This package is part of [Package Control Packages](https://packagecontrol.io/packages/Antescofo). See [Instructions](https://packagecontrol.io/docs/usage) for installation within ST. 

### Manual Installation

- Download the ZIP archive from the link above
- Move the resultant 'Antescofo' folder to '~/Library/Application Support/Sublime Text 2/Packages/' (same with Sublime Text 3)

## Usage

#### Plugin Settings and key Maps

You can modify the plugin setting stored in *antescofo.sublime-settings* file by creating a new one and putting it in the *Packages/User/* folder. This setting contains Antescofo IP and port (default: 'localhost', 5678) and AscoGraph IP and port (default: 'localhost', 6789). Similarly, you can modify the key maps.

Setting and Key-map files in the *Packages/User/* folder have priority over the main package. This allows you to create your own setting while safely updating your packages in future releases.

#### Open Antescofo Communication

Open *Antescofo* in either Max or Pd and initiate OSC communication from the object by sending 'ascograph open' to the object (or double-clicking on *Antescofo* object in case of Max).

#### Syntax Coloring

By openning an Antescofo file with '.asco' or '.asco.txt' extension, the *Antescofo* syntax is automatically detected. You should see this at the bottom-right corner of the Sublime Text Editor. If not, just click there and choose *Antescofo*.
Additionally, you should choose your favourite color scheme from 'Preferences -> Color Schemes -> Antescofo' (Courtesy of [Julia Blondeau](http://www.juliablondeau.fr/)!) 

#### Hot-Keys

The following short cuts are currently available on all platforms. You can easily change them by modifying the 'Default (OSX).sublime-keymap' file in the plugin folder (and other platforms accordingly). They are also available in the 'Tools' menu.

- <kbd>alt+p</kbd> without text selection will evaluate the line in Antescofo (will send OSC message to Antescofo with 'playstring' prepend)
- <kbd>alt+p</kbd> with text selection will do the above on the entire selected text.
- <kbd>alt+s</kbd> : to remotely 'start' Antescofo score
- <kbd>alt+shift+s</kbd> : 'startfromlabel' if cursor is on an event with a given label
- <kbd>alt+c</kbd> : to remotely 'stop' Antescofo
- <kbd>alt+l</kbd> : Loads the current file remotely in Antescofo object (Max/Pd) and Ascograph

#### Event navigation
To jump directly to an event in your score :
- <kbd>cmd+r</kbd> opens a menu with all the events in the score. 

## Problems or Suggestions?

Create an [Issue](https://github.com/arshiacont/antescofo-sublime-package/issues) and we will get back to you swiftly!