#!/usr/bin/env python3
"""Duck typing - first element of a sequence."""

from typing import Sequence, Any, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """Return first element if exists, otherwise None."""
    if lst:
        return lst[0]
    return None
