# -*- coding: UTF-8 -*-

"""Inicializador padrão python."""

import minimal


def initialize(context):
    """Initialize the minimal product."""
    context.registerClass(
        minimal.minimal,
        constructors=(
            minimal.manage_add_minimal_action,
        )
    )
