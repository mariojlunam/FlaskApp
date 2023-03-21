"""
Helper module with functions that performs part of the 
computation of another function 
"""


def build_feature(values: tuple) -> dict:
    """
    Function to build a valid feature
    Params: 
        values(tuple): Tuple with with geom object, and properties object
    Returns:
        geojson_roads(dict): dict/json like with valid geom/properties
    """
    geom_feature, properties = values

    # Build feature
    feature = {"type": "Feature",
               "geometry": geom_feature,
               "properties": properties
               }

    return feature
