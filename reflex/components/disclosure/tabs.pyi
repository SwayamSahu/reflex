"""Stub file for tabs.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `scripts/pyi_generator.py`!
# ------------------------------------------------------

from typing import Union, overload, Optional
from reflex.components.libs.chakra import ChakraComponent
from reflex.components.component import Component
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventChain

class Tabs(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, items, align: Optional[Union[Var[str], str]] = None, default_index: Optional[Union[Var[int], int]] = None, id_: Optional[Union[Var[str], str]] = None, is_fitted: Optional[Union[Var[bool], bool]] = None, is_lazy: Optional[Union[Var[bool], bool]] = None, is_manual: Optional[Union[Var[bool], bool]] = None, orientation: Optional[Union[Var[str], str]] = None, variant: Optional[Union[Var[str], str]] = None, **props) -> "Tabs": ...  # type: ignore

class Tab(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, is_disabled: Optional[Union[Var[bool], bool]] = None, is_selected: Optional[Union[Var[bool], bool]] = None, id_: Optional[Union[Var[str], str]] = None, panel_id: Optional[Union[Var[str], str]] = None, **props) -> "Tab": ...  # type: ignore

class TabList(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, **props) -> "TabList": ...  # type: ignore

class TabPanels(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, **props) -> "TabPanels": ...  # type: ignore

class TabPanel(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, **props) -> "TabPanel": ...  # type: ignore