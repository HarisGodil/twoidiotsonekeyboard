# Two Idiots One Keyboard

Each half of the keyboard is sent to a different pane. The left user can
press the Control key to get their missing half of the keyboard, and the 
right user can press shift to get their half of the keyboard.

The keys are match by reflecting over the center axis. For example, the
letters 'q' and 'p' are a partners, responsible for creating the other.

## How to install

If you already have tmux installed, all you need to is run
`generate_tmux_conf.py`


## Caveats and Quirks

Unfortunately the Enter key doesn't play nicely with tmux, so that key
is on the pair 'a' & ']'.

I have also create a pairing between 'z' & '.', which skips over ',', but
I think '.' is a more useful key to have


## Warnings

This will probably destory your existing tmux conf, so please stash that
somewhere before you run `generate_tmux_conf.py`

