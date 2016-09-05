# -*- coding: utf-8 -*-
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
#from zope.component import getMultiAdapter
from plone import api


class CoverView(BrowserView):
    """ Cover View
    """
    index = ViewPageTemplateFile('template/cover_view.pt')

    def __call__(self):
        return self.index()


class NtuaAlbum(BrowserView):
    """ NTUA Album
    """
    index = ViewPageTemplateFile('template/ntua_album.pt')

    def __call__(self):
        return self.index()

