#!/usr/bin/python

from collections import namedtuple
import os

"""
Proof of concept tmux config

bind -n q select-pane -t 1 \; send-keys b
bind -n w select-pane -t 2 \; send-keys c
"""

KeyMap = namedtuple('keymap', ['left', 'right'])
class Key(namedtuple('key', ['cmd', 'char', 'pane'])):
    __slots__ = ()
    def __repr__(self):
        return self.__str__()
    def __str__(self):
        return "bind -n {} select-pane -t {} \\; send-keys {}".format(self.cmd, self.pane, self.char)

keys = [
   # Do I care about numbers?
   # First Row
   KeyMap('q','p'),
   KeyMap('w','o'),
   KeyMap('e','i'),
   KeyMap('r','u'),
   KeyMap('t','y'),
   # Second Row
   KeyMap('a','Enter'), # How does "enter" look like for command versus send-keys
   KeyMap('s','l'),
   KeyMap('d','k'),
   KeyMap('f','j'),
   KeyMap('g','h'),
   # Third Row
   KeyMap('z','.'), # How does "." look like for command versus send-keys
   KeyMap('x','m'),
   KeyMap('c','n'),
   KeyMap('v','b'),
]

def gen_left_keys(key):
    return [
        str(Key(key.left,        key.left,  0)),
        str(Key("C-" + key.left, key.right, 0)),
    ] + [ # And allow for these to work if the other user is pressing their command key
        str(Key(key.left.upper(),        key.left,  0)),
        str(Key("C-" + key.left.upper(), key.right, 0)),
    ]

def gen_right_keys(key):
    return [
        str(Key(key.right,         key.right, 1)),
        str(Key(key.right.upper(), key.left,  1)),
    ] + [ # And allow for these to work if the other user is pressing their command key
        str(Key("C-" + key.right,         key.right, 1)),
        str(Key("C-" + key.right.upper(), key.left,  1)),
    ]

tmux_conf = [
    "set -g prefix C-q",
    "unbind C-b",
    "bind C-q send-prefix",
]

for keymap in keys:
    tmux_conf += gen_left_keys(keymap)
    tmux_conf += gen_right_keys(keymap)

TMUX_CONF_PATH = os.path.expanduser("~") + "/.tmux.conf"
if os.path.exists(TMUX_CONF_PATH):
    # Hrmm, after running this script twice, the original tmux config is gone...
    os.rename(TMUX_CONF_PATH, TMUX_CONF_PATH + ".old")
with open(TMUX_CONF_PATH, 'w') as conf_file:
    conf_file.write("\n".join(tmux_conf))
