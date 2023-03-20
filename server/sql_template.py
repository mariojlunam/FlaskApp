
from sqlalchemy import text

ROADS_QUERY = text(""" SELECT
                        AsGeoJSON(Transform(Roads.geom, :srid)) as geom,
                        -- Build json_object for properties 
                        json_object('id', Roads.id,
                                    'name', Roads.name,
                                    'roadclassification', Roads.roadclassification,
                                    'road_func', Roads.roadfunction,
                                    'length', Roads.length) as props
                        FROM Roads
                        WHERE
                        -- OS Roads dataset is on 27700
                        ST_EnvIntersects(Transform(Roads.geom, :srid),:x1, :y1, :x2, :y2)
                    """)
