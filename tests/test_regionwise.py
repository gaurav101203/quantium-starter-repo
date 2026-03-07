import pytest
from regionwise import dash_app

def test_header_is_present(dash_duo):
    dash_duo.start_server(dash_app)

    header = dash_duo.find_element("#header")

    assert header is not None
    assert header.text == "Pink Morsel Visualizer"

def test_visualization_is_present(dash_duo):
    dash_duo.start_server(dash_app)

    graph = dash_duo.find_element("#visualization")

    assert graph is not None

def test_region_picker_is_present(dash_duo):
    dash_duo.start_server(dash_app)

    region_picker = dash_duo.find_element("#region-picker")

    assert region_picker is not None