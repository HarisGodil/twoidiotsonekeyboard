#!/usr/bin/python

from collections import namedtuple
import os

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
   KeyMap('a','Enter'), # a can press Enter, but for some reason Enter is always 'x'?
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

def upper(char):
    # upper for these don't match Shift+key on the keyboard
    if char == '.':
        return '>'
    return char.upper()

def gen_left_keys(key):
    return [
        str(Key(key.left,        key.left,  0)),
        str(Key("C-" + key.left, key.right, 0)),
    ] + [ # And allow for these to work if the other user is pressing their command key
        str(Key(upper(key.left),        key.left,  0)),
        str(Key("C-" + upper(key.left), key.right, 0)),
    ]

def gen_right_keys(key):
    return [
        str(Key(key.right,        key.right, 1)),
        str(Key(upper(key.right), key.left,  1)),
    ] + [ # And allow for these to work if the other user is pressing their command key
        str(Key("C-" + key.right,        key.right, 1)),
        str(Key("C-" + upper(key.right), key.left,  1)),
    ]

# Need to find a non-alphabet char to hold this
tmux_conf = [
    "set -g prefix C-q",
    "unbind C-b",
    "bind C-q send-prefix",
]

for keymap in keys:
    tmux_conf += gen_left_keys(keymap)
    tmux_conf += gen_right_keys(keymap)

# tmux doesn't seem to like using Enter as a command, but whatever
tmux_conf += gen_right_keys(KeyMap("a", "]"))
tmux_conf += [
    str(Key("]", "Enter", 1)),
    str(Key("}", "Enter", 1)),
    str(Key("C-]", "Enter", 1)),
    # C-} Doesn't exist apparently
]

TMUX_CONF_PATH = os.path.expanduser("~") + "/.tmux.conf"
if os.path.exists(TMUX_CONF_PATH):
    # Hrmm, after running this script twice, the original tmux config is gone...
    os.rename(TMUX_CONF_PATH, TMUX_CONF_PATH + ".old")
with open(TMUX_CONF_PATH, 'w') as conf_file:
    conf_file.write("\n".join(tmux_conf))
