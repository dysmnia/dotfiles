# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

from qtile_extras import widget
from qtile_extras.widget.decorations import BorderDecoration

mod = "mod4"
term = "alacritty"
fm = "pcmanfm"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html

    # window manager
    Key([mod, "shift"], "r", lazy.reload_config()),
    Key([mod, "shift"], "q", lazy.shutdown()),
    Key([mod], "period",     lazy.to_screen(1)),
    Key([mod], "comma",      lazy.to_screen(0)),
    Key([mod], "f",          lazy.next_layout()),
    Key([mod], "c",          lazy.window.kill()),
    Key([mod], "s",          lazy.window.toggle_floating()),

    Key([mod], "j",          lazy.layout.down()),
    Key([mod], "k",          lazy.layout.up()),
    Key([mod, "shift"], "h", lazy.layout.shrink_main()),
    Key([mod, "shift"], "l", lazy.layout.grow_main()),

    # custom applications
    Key([mod], "Return",     lazy.spawn(term)),
    Key([mod], "v",          lazy.spawn(fm)),
    Key([mod], "p",          lazy.spawn("rofi -show drun")),
    Key([mod], "l",          lazy.spawn("xlock -mode blank")),
    Key([], "XF86Launch7",   lazy.spawn("pamixer --default-source -t")),
    Key([], "Print",         lazy.spawn("flameshot gui")),
    Key([mod], "space",      lazy.widget["keyboardlayout"].next_keyboard()),
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),

            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=False),
                desc="Switch to & move focused window to group {}".format(
                    i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

# doom-one
# colors = {
#     "bg": "282c34",
#     "fg": "bbc2cf",
#     "black": "1b2229",
#     "gray": "3f444a",
#     "red": "ff6c6b",
#     "orange": "da8548",
#     "green": "98be65",
#     "teal": "4db5bd",
#     "yellow": "ecbe7b",
#     "blue": "51afef",
#     "magenta": "c678dd",
#     "violet": "a9a1e1",
#     "cyan": "46d9ff",
#     "white": "dfdfdf"
# }

# catppuccin
colors = {
    "bg": "1e1e2e",
    "fg": "cdd6f4",
    "black": "313244",
    "gray": "6c7086",
    "red": "f38ba8",
    "orange": "fab387",
    "green": "a6e3a1",
    "teal": "94e2d5",
    "yellow": "f9e2af",
    "blue": "89b4fa",
    "magenta": "f5c2e7",
    "violet": "cba6f7",
    "cyan": "89dceb",
    "white": "b4befe"
}

layouts = [
    layout.MonadTall(
        border_focus=colors["magenta"],
        border_normal=colors["bg"],
        border_width=2,
        margin=12
    ),
    layout.Max(),
]

widget_defaults = dict(
    font="Ubuntu Bold",
    background=colors["bg"],
    foreground=colors["fg"],
    fontsize=14,
    padding=2
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    highlight_color=colors["bg"],
                    highlight_method="line",
                    this_current_screen_border=colors["magenta"],
                    this_screen_border=colors["bg"],
                    other_current_screen_border=colors["magenta"],
                    other_screen_border=colors["bg"],
                    active=colors["cyan"],
                    inactive=colors["fg"]
                ),
                widget.Sep(
                    linewidth=2,
                    padding=12,
                    size_percent=50,
                    foreground=colors["gray"]
                ),
                widget.CurrentLayoutIcon(
                    scale=0.65
                ),
                widget.CurrentLayout(),
                widget.Sep(
                    linewidth=2,
                    padding=12,
                    size_percent=50,
                    foreground=colors["gray"]
                ),
                widget.WindowName(
                    foreground=colors["green"],
                    max_chars=50
                ),
                widget.OpenWeather(
                    location="Budapest",
                    foreground=colors["cyan"],
                    format=" {weather}, {temp: .1f}°C ",
                    decorations=[
                        BorderDecoration(
                            colour=colors["cyan"],
                            border_width=[0, 0, 2, 0],
                            padding_x=5,
                            padding_y=None,)
                    ]
                ),
                widget.KeyboardLayout(
                    configured_keyboards=["us", "hu"],
                    display_map={"us": "us", "hu": "hu"},
                    foreground=colors["red"],
                    fmt=" kbd: {} ",
                    decorations=[
                        BorderDecoration(
                            colour=colors["red"],
                            border_width=[0, 0, 2, 0],
                            padding_x=5,
                            padding_y=None,)
                    ]
                ),
                widget.DF(
                    format="{uf}{m}",
                    visible_on_warn=False,
                    foreground=colors["orange"],
                    fmt=" disk: {} free ",
                    decorations=[
                        BorderDecoration(
                            colour=colors["orange"],
                            border_width=[0, 0, 2, 0],
                            padding_x=5,
                            padding_y=None,)
                    ]
                ),
                widget.ThermalSensor(
                    format=" temp: {temp: .0f}{unit} ",
                    tag_sensor="CPU",
                    foreground=colors["yellow"],
                    decorations=[
                        BorderDecoration(
                            colour=colors["yellow"],
                            border_width=[0, 0, 2, 0],
                            padding_x=5,
                            padding_y=None,)
                    ]
                ),
                widget.Memory(
                    format=" mem: {MemUsed: .1f}G used ",
                    measure_mem="G",
                    foreground=colors["green"],
                    decorations=[
                        BorderDecoration(
                            colour=colors["green"],
                            border_width=[0, 0, 2, 0],
                            padding_x=5,
                            padding_y=None,)
                    ]
                ),
                widget.Net(
                    format=" net: {down:.0f}{down_suffix}   {up:.0f}{up_suffix}  ",
                    foreground=colors["cyan"],
                    decorations=[
                        BorderDecoration(
                            colour=colors["cyan"],
                            border_width=[0, 0, 2, 0],
                            padding_x=5,
                            padding_y=None,)
                    ]
                ),
                widget.CPU(
                    format=" cpu: {load_percent: .0f}% ",
                    foreground=colors["blue"],
                    decorations=[
                        BorderDecoration(
                            colour=colors["blue"],
                            border_width=[0, 0, 2, 0],
                            padding_x=5,
                            padding_y=None,)
                    ]
                ),
                widget.Clock(
                    format=" %a, %b %d %H:%M ",
                    foreground=colors["magenta"],
                    decorations=[
                        BorderDecoration(
                            colour=colors["magenta"],
                            border_width=[0, 0, 2, 0],
                            padding_x=5,
                            padding_y=None,)
                    ]
                ),
                widget.Systray(),
                widget.TextBox(
                    text=" "
                ),
            ],
            28,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ],
    border_focus=colors["magenta"],
    border_normal=colors["bg"],
    border_width=2
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
