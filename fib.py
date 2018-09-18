#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sequences

def main(argv):
    n = int(argv[1])
    print(sequences.fibonacci(n)[-1])

if __name__ == "__main__":
    import sys
    main(sys.argv)