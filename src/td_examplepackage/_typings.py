from typing import Union
from .ExampleComp.extExampleExtension import extExampleExtension
from td import COMP # We need to explicitly import td as it will not be loaded in time during startup


ExampleComp = Union[COMP, extExampleExtension ]