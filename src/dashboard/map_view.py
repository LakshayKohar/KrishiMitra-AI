import folium
import streamlit as st
from streamlit_folium import st_folium


def add_ndvi_legend(map_object):
    legend_html = """
    <div style="
        position: fixed;
        bottom: 50px;
        left: 50px;
        width: 220px;
        height: 145px;
        background-color: white;
        border:2px solid grey;
        z-index:9999;
        font-size:14px;
        padding: 10px;
        border-radius: 8px;
    ">
    <b>NDVI Legend</b><br>
    <span style="color:red;">■</span> Low Vegetation / Stress<br>
    <span style="color:orange;">■</span> Sparse Vegetation<br>
    <span style="color:yellow;">■</span> Moderate Vegetation<br>
    <span style="color:lightgreen;">■</span> Healthy Vegetation<br>
    <span style="color:green;">■</span> Dense Vegetation
    </div>
    """
    map_object.get_root().html.add_child(folium.Element(legend_html))


def render_map(ndvi_image, satellite_image, report):
    st.header("🗺️ Interactive Field Map")

    latitude = report["latitude"]
    longitude = report["longitude"]

    m = folium.Map(
        location=[latitude, longitude],
        zoom_start=13,
        tiles="OpenStreetMap",
    )

    rgb_vis = {
        "min": 0,
        "max": 3000,
        "bands": ["B4", "B3", "B2"],
    }

    ndvi_vis = {
        "min": -1,
        "max": 1,
        "palette": [
            "red",
            "orange",
            "yellow",
            "lightgreen",
            "green",
        ],
    }

    rgb_map_id = satellite_image.getMapId(rgb_vis)
    ndvi_map_id = ndvi_image.getMapId(ndvi_vis)

    folium.TileLayer(
        tiles=rgb_map_id["tile_fetcher"].url_format,
        attr="Google Earth Engine",
        name="Sentinel-2 RGB",
        overlay=True,
        control=True,
    ).add_to(m)

    folium.TileLayer(
        tiles=ndvi_map_id["tile_fetcher"].url_format,
        attr="Google Earth Engine",
        name="NDVI Layer",
        overlay=True,
        control=True,
    ).add_to(m)

    folium.Marker(
        location=[latitude, longitude],
        popup=f"""
        <b>{report['location']}</b><br>
        Avg NDVI: {report['ndvi']['average']:.3f}<br>
        Health: {report['crop_health']}<br>
        Cloud Cover: {report['cloud_cover']:.2f}%
        """,
        tooltip="Selected Location",
    ).add_to(m)

    folium.LayerControl().add_to(m)

    add_ndvi_legend(m)

    st_folium(
        m,
        width=1100,
        height=600,
        returned_objects=[],
    )