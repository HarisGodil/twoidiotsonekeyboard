# Two Idiots One Keyboard

Each half of the keyboard is sent to a different pane. The left user can
press the Control key to get their missing half of the keyboard, and the 
right user can press shift to get their half of the keyboard.

The keys are match by reflecting over the center axis. For example, the
letters 'q' and 'p' are a partners, responsible for creating the other.

## How to Install / Run

To install, ensure tmux is installed, and then run
`generate_tmux_conf.py` to generate the tmux config.

To set this up, start tmux, and create an extra pane (`C-Space %`)


## Caveats and Quirks

Unfortunately the Enter and Space keys don't play too nicely with tmux,
so those keys are now pair like:

Left    Right
a       ] (In place of Enter)
Space   ,


I have also create a pairing between 'z' & '.', which skips over ',', but
I think '.' is a more useful key to have


I'm not super happy about any of the above quirks, so if you have any
suggestions, let me know.

## Warnings

This will probably destory your existing tmux conf, so please stash that
somewhere before you run `generate_tmux_conf.py`

