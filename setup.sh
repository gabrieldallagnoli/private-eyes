#!/usr/bin/env bash

yay -S --noconfirm --needed python-opencv mpv dunst
mkdir -p ~/.config/systemd/user
cp -rf pv-eyes.service ~/.config/systemd/user/pv-eyes.service
systemctl --user enable --now pv-eyes.service