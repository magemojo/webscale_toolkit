import os

php_version = str(os.popen("php --version | head -n1 | awk '{ print $2 }'").readlines()[0]).replace("\n", "")
php_major = int(php_version.split(".")[0])
php_minor = int(php_version.split(".")[1])

if php_major < 7:
    print("Script Requires PHP 7.1 or higher. Your version: " + php_version)
    exit()
elif php_major == 7 and php_minor < 1:
    print("Script Requires PHP 7.1 or higher. Your version: " + php_version)
    exit()

import shutil

import lib.menu_handler as menu
import lib.config_handler as conf


def main():
    path = conf.get_path()
    if path.lower() == "none":
        menu.dev_copy_menu(False, False)
    else:
        version = str(os.popen("cd " + path + " && n98-magerun2 sys:info | awk 'NR==10 { print $4;exit }'").readlines()[0]).replace("\n", "")
        major = version.split("-")[0].split(".")[0]
        minor = version.split("-")[0].split(".")[1]

        if int(major) != 2:
            print("Script Requires Magento 2.3 or 2.4 Your version: " + version)
            exit()
        elif int(minor) < 3 or int(minor) > 4:
            print("Script Requires Magento 2.3 or 2.4. Your version: " + version)
            exit()

        if os.path.exists(path + "/app/etc/env.php"):
            source = path + "/app/etc/env.php"
            dest = "/srv/webscale_toolkit/var/"
            shutil.copy2(source, dest)

        if os.path.exists(path + "/composer.json"):
            source = path + "/composer.json"
            dest = "/srv/webscale_toolkit/var/"
            shutil.copy2(source, dest)

        menu.main_menu(path)


main()
