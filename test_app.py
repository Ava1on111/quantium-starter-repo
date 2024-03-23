from app import app  # import app.py

def test_header_presence(dash_duo):
    dash_duo.start_server(app) 

    # Verify header exists
    assert dash_duo.find_element("h1"), "The header should be present."

def test_visualisation_presence(dash_duo):
    dash_duo.start_server(app)

    # Verify that the visualization exists
    assert dash_duo.find_element("#sales-chart"), "The visualisation should be present."

def test_region_picker_presence(dash_duo):
    dash_duo.start_server(app)

    # Verify that the region selector exists
    assert dash_duo.find_element("#region-selector"), "The region picker should be present."