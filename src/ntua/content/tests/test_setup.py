# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from ntua.content.testing import NTUA_CONTENT_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that ntua.content is properly installed."""

    layer = NTUA_CONTENT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if ntua.content is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'ntua.content'))

    def test_browserlayer(self):
        """Test that INtuaContentLayer is registered."""
        from ntua.content.interfaces import (
            INtuaContentLayer)
        from plone.browserlayer import utils
        self.assertIn(INtuaContentLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = NTUA_CONTENT_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['ntua.content'])

    def test_product_uninstalled(self):
        """Test if ntua.content is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'ntua.content'))

    def test_browserlayer_removed(self):
        """Test that INtuaContentLayer is removed."""
        from ntua.content.interfaces import INtuaContentLayer
        from plone.browserlayer import utils
        self.assertNotIn(INtuaContentLayer, utils.registered_layers())
