from collections import namedtuple
from pathlib import Path

FilesDef = namedtuple("ToxFile", ["ExampleComp"])

ToxFiles = FilesDef(
    ExampleComp = Path( Path( __file__ ).parent, "ExampleComp.tox" )
)