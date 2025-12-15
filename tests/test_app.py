import sys
import os

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import app
from dash import html


def find_component_by_id(component, component_id):
    """Recursively search Dash layout for component by id"""

    if hasattr(component, "id") and component.id == component_id:
        return component

    if hasattr(component, "children") and component.children is not None:
        children = component.children

        # Dash children can be list, tuple, or single component
        if isinstance(children, (list, tuple)):
            for child in children:
                result = find_component_by_id(child, component_id)
                if result is not None:
                    return result
        else:
            return find_component_by_id(children, component_id)

    return None


def test_header_present():
    header_found = False

    def find_h1(component):
        nonlocal header_found
        if isinstance(component, html.H1):
            header_found = True
        if hasattr(component, "children") and component.children is not None:
            children = component.children
            if isinstance(children, (list, tuple)):
                for child in children:
                    find_h1(child)
            else:
                find_h1(children)

    find_h1(app.app.layout)
    assert header_found is True


def test_graph_present():
    graph = find_component_by_id(app.app.layout, "graph")
    assert graph is not None


def test_region_picker_present():
    radio = find_component_by_id(app.app.layout, "region")
    assert radio is not None
