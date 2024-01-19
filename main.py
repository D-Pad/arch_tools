from pyperclip import copy
from requests import get
from sys import argv as args
from logos import get_arch_logo, dye
from json import load

del args[0]


def main(mode="mirrors"):

    get_arch_logo()

    # Define command behaviors
    def build_mirror_list():

        def build_request_string():
            # https://archlinux.org/mirrorlist/?country=US&protocol=http&protocol=https&ip_version=4

            url = "https://archlinux.org/mirrorlist/?"
            with open("config/config.json") as file:
                settings = load(file)['mirrors']

            for k, v in settings.items():
                for i in v:
                    url += f"{k}={i}&"

            return url[:-1]

        print(dye("Downloading mirror list", "yellow"))
        mirror_list = get(build_request_string())
        mirrors = mirror_list.text

        new_mirrors = ""
        for line in mirrors.split("\n"):
            if line[:1] == "#" and line[:2] != "##":
                new_mirrors += line[1:] + "\n"
            else:
                new_mirrors += line + "\n"

        with open("mirrors.txt", "w") as file:
            file.write(new_mirrors)

        copy(new_mirrors)
        print(dye("Mirror list updated and copied to clipboard", "cyan"))

    # If no command was passed, use the default mode
    if len(args) == 0:
        args.append(mode)

    # Run the appropriate function from the command provided
    cmd = args[0]
    if cmd == "mirrors" or cmd == "mirror":
        build_mirror_list()


if __name__ == "__main__":
    main()
