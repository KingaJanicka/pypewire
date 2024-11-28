# -*- coding: utf-8 -*-

import ctypes
import pathlib

if __name__ == "__main__":
    # TODO: make cross-platform
    libname = "/usr/lib/aarch64-linux-gnu/libpipewire-0.3.so.0"
    c_lib = ctypes.CDLL(libname)
    print(c_lib)
