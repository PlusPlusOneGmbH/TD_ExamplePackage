from collections import namedtuple
from pathlib import Path
from typing import Union
FilesDef = namedtuple("ToxFile", ["ExampleComp"])

from .ExampleComp.extExampleExtension import extExampleExtension

ToxFiles = FilesDef(
    ExampleComp = Path( Path( __file__ ).parent, "ExampleComp.tox" )
)

Typings = FilesDef(
    ExampleComp = Union[ COMP, extExampleExtension ] 
)