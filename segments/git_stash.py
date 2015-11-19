# https://github.com/milkbikis/powerline-shell/pull/201

import subprocess


def add_git_stash_segment():
    stash_count = subprocess.check_output('git stash list | wc -l', shell=True).strip()

    if stash_count == '0':
        return

    bg = 55  # purple
    fg = 254 # white

    # ↯
    # DOWNWARDS ZIGZAG ARROW
    # Unicode: U+21AF, UTF-8: E2 86 AF
    # stash_symbol = u'\u21AF'

    # ⎗
    # PREVIOUS PAGE
    # Unicode: U+2397, UTF-8: E2 8E 97
    stash_symbol = u'\u2397'

    # stash_symbol = u'\u2398' #⎘
    # stash_symbol = u'\u2295' #⊕
    # stash_symbol = u'\u24c8' #Ⓢ

    count = stash_count if stash_count > 1 else u''
    string = u' {}{} '.format(count, stash_symbol)
    powerline.append(string, fg, bg)

try:
    add_git_stash_segment()
except OSError:
    pass
except subprocess.CalledProcessError:
    pass
