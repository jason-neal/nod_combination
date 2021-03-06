#!/usr/bin/env python
# -*- coding: utf8 -*-

"""Get File names of files that match regular expression.

Possibly better to use the glob module.
"""
import fnmatch
import os
from typing import List, Optional


def get_filenames(path: str, regexp: str, regexp2: Optional[str] = None) -> List[str]:
    """Regexp must be a regular expression as a string.

    eg '*.ms.*', '*_2.*', '*.ms.norm.fits*'

    resexp2 is if want to match two expressions such as
    '*_1*' and '*.ms.fits*'
    """
    os.chdir(path)
    filelist = []
    for file in os.listdir('.'):
        if regexp2 is not None:  # Match two regular expressions
            if fnmatch.fnmatch(file, regexp) and fnmatch.fnmatch(file, regexp2):
                filelist.append(file)
        else:
            if fnmatch.fnmatch(file, regexp):
                filelist.append(file)
    filelist.sort()
    return filelist

