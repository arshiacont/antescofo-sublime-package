# antescofo-sublime-package
Antescofo Language Package and Plugins for Sublime Text Editor

Using pyOSC package. All methods function by sending OSC messages to instances of Antescofo in Max/Pd or elsewhere. For now, we use <i>localhost</i> using the default send port of 5678.

## Installation

Move the resultant 'Antescofo' folder to ~/Library/Application Support/Sublime Text 2/Packages/

## Usage

- CTRL+p without text selection will evaluate the line in Antescofo (will send OSC message to Antescofo with 'livecode' prepend)
- CTRL+p with text selection will do the above on the entire selected text.
- CTRL+s : to 'start' Antescofo
- CTRL+c : to 'stop' Antescofo

## TODO

Add OSC client configuration
Add OSC receive to move cursor to line # Antescofo is refering to
Add methods for 'startfrom' and similar based on cursor position