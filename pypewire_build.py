import cffi
import pathlib


""" Build the CFFI Python bindings """
ffi = cffi.FFI()
this_dir = pathlib.Path().absolute()
pipewire_root = this_dir / "pipewire"
pipewire_src = pipewire_root / "src"
pipewire_headers = pipewire_src / "pipewire"
pipewire_builddir = pipewire_root / "builddir" / "src"
pipewire_spa_headers = pipewire_root / "spa" / "include"


ffi.cdef("""
void pw_init(int *argc, char **argv[]);
""")

ffi.set_source(
    "_pypewire_cffi",
    """
#include <pipewire/pipewire.h>
    """,
    include_dirs=[pipewire_spa_headers.as_posix(), pipewire_builddir.as_posix(), pipewire_src.as_posix()]
)


ffi.compile()