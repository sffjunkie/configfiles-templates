import os
import socket
import subprocess
import sys
from pathlib import Path
from typing import List  # noqa: F401

from libqtile import bar, extension, hook, layout, widget
from libqtile.command import lazy
from libqtile.config import Group, Key, Screen

import yaml

import bar
import group
import kbdmouse
import rule
import secret
import setting

sec = secret.load_secrets()
s = setting.load_settings()
keys = kbdmouse.bind_keys(s)
mouse = kbdmouse.bind_mouse_buttons(s)
groups = group.build_groups(s)
group.bind_group_keys(s, keys)

theme = s["theme"]
layouts = [
    layout.MonadTall(**theme["layout"]),
    layout.Max(**theme["layout"]),
]

top_bar, bottom_bar = bar.build_bars(s, sec)
screens = [Screen(top=top_bar, bottom=bottom_bar)]

auto_fullscreen = True
bring_front_click = "floating_only"
cursor_warp = False
dgroups_app_rules = rule.build_rules()  # type: List
dgroups_key_binder = None
extension_defaults = theme["extension"].copy()
focus_on_window_activation = "smart"
follow_mouse_focus = False
widget_defaults = theme["widget"].copy()
wmname = "QTile"

# @hook.subscribe.client_new
# def client_to_group(client):
#     wm_class = client.window.get_wm_class()[0]
#     group_name = group.find_group_for(wm_class)
#     if group_name:
#         client.togroup(group_name)
# lazy.group[group_name].cmd_toscreen()
