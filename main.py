#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import typing


def main(argv: typing.List[str] = None):
    if argv is None:
        print("Hello World!")
    else:
        print("Arg: " + argv[0])


if __name__ == "__main__":
    # コマンドライン引数の処理
    if len(sys.argv) > 1:
        main(sys.argv[1:])
    else:
        main()
