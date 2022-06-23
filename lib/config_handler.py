#!/usr/bin/env python3
from lib.text_color import Colors
from subprocess import check_output
import lib.command_handler as shell
import json


def get_path():
    path = input(Colors.FG.LightGreen + Colors.Bold + "Root Magento Path (Example /srv/public_html): " + Colors.Reset)
    if path.endswith('/'):
        path_length = len(path)
        path = path[:path_length - 1]
        return path
    else:
        return path


def load_config(path):
    config = check_output(["php", "-r", "echo json_encode(include '" + path + "/app/etc/env.php');"])
    config = json.loads(config)
    return config


def save_config(config, path):
    action = "Save Config"
    with open('/srv/webscale_toolkit/var/config.json', 'w+') as outfile:
        json.dump(config, outfile)
    shell.run_bash_command(config, path, action, "php -d display_errors=on ./lib/save_config.php " + path, "")
