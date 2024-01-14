#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 17:04:50 2024

@author: pwecker
"""

import sys
from pip._internal.operations import freeze

# Get Python version
python_version = sys.version

# Get installed packages and versions
installed_packages = freeze.freeze()

# Write to environment.txt
with open('environment.txt', 'w') as file:
    file.write(f"Python {python_version.strip()}\n")
    file.write("{:<25} {:<15}\n".format("Package", "Version"))
    file.write("-" * 40 + "\n")
    
    for package in installed_packages:
        file.write(package + "\n")