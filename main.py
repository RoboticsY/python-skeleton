#! /usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import sys


def main(argv: list[str] | None = None) -> None:
    """Main function.

    Args:
        argv (list[str], optional): コマンドライン引数. Defaults to None.
    """
    if argv is None:
        logging.info("Hello World!")
    else:
        logging.info("Arg: " + argv[0])


if __name__ == "__main__":
    # コマンドライン引数の処理
    if len(sys.argv) > 1:
        main(sys.argv[1:])
    else:
        main()
