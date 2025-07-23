#!/usr/bin/env bash

mkdir -p ~/.assets/private-eyes
cp -rf main.py ~/.assets/private-eyes

mkdir -p ~/.config/systemd/user
cp -rf private-eyes.service ~/.config/systemd/user/private-eyes.service
systemctl --user enable --now private-eyes.service