"""
KrishiMitra AI
---------------

Google Earth Engine Connection Module

Author:
Team KrishiMitra AI

Purpose:
Connects the application to Google Earth Engine.
"""

import ee


class EarthEngineConnector:
    """
    Handles Google Earth Engine authentication
    and initialization.
    """

    def __init__(self):
        self.initialized = False

    def initialize(self):
        """
        Authenticate and initialize Earth Engine.
        """

        try:
            ee.Initialize()
            self.initialized = True
            print("✅ Google Earth Engine Initialized Successfully!")

        except Exception:
            print("🔐 Authentication Required...")
            ee.Authenticate()
            ee.Initialize()

            self.initialized = True

            print("✅ Authentication Successful!")