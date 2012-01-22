#!/usr/bin/env python

import sys
import os

from wiki import main

if __name__ == "__main__":
    parent_dir, dir = os.path.split(sys.path[0])
    sys.path.insert(0, parent_dir)
    main()
