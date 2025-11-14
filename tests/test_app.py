import sys
import os

# Add project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app import app

def test_header_exists():
    header = app.layout.children[0]
    assert header.children == "Pink Morsel Sales Visualiser"

def test_visualisation_exists():
    graph = app.layout.children[2].children[0]
    assert graph.id == "sales-graph"

def test_region_picker_exists():
    region_picker = app.layout.children[1].children[1]
    assert region_picker.id == "region-filter"
