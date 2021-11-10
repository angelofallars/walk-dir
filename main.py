"""Traverse through a git repo, calling `makepkg` on each PKGBUILD"""
import os
import sys


def main() -> int:
    start_dir = os.path.abspath(".")
    checking_status = 0

    for pwd, folders, files in os.walk(start_dir):
        os.chdir(os.path.abspath(pwd))
        if "PKGBUILD" in files:
            print(f"Executing 'makepkg --syncdeps' in {pwd} ...")
            exit_status = os.system("makepkg --syncdeps")

            if exit_status != 0:
                checking_status = 1

    return checking_status


if __name__ == "__main__":
    sys.exit(main())
