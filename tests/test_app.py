from dash.testing.application_runners import import_app

def test_header_presence(dash_duo):
    app = import_app("app.app")
    dash_duo.start_server(app) 

    # The header is present.
    assert dash_duo.find_element("h1"), "The header should be present."

def test_visualisation_presence(dash_duo):
    app = import_app("app.app")
    dash_duo.start_server(app)

    # The visualisation is present.
    assert dash_duo.find_element("#sales-chart"), "The visualisation should be present."

def test_region_picker_presence(dash_duo):
    app = import_app("app.app")
    dash_duo.start_server(app)

    # The region picker is present.
    assert dash_duo.find_element("#region-selector"), "The region picker should be present."
