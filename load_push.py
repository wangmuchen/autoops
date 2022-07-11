#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import tarfile
import tempfile
import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--dir", help="images file dir",type=str)
args = parser.parse_args()

print(args.dir)
