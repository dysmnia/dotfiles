#!/bin/bash

xrandr --output DisplayPort-2 --mode 2560x1440 --rate 165 --primary --left-of DisplayPort-0
xrandr --output DisplayPort-2 --set "TearFree" on
xrandr --output DisplayPort-0 --set "TearFree" on
