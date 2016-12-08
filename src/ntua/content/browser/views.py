# -*- coding: utf-8 -*-
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
#from zope.component import getMultiAdapter
from plone import api
import transaction
from plone.protect.interfaces import IDisableCSRFProtection
from zope.interface import alsoProvides


class TestZZZZZ(BrowserView):

    def __call__(self):
        request = self.request
        portal = api.portal.get()
        news = portal['folder_3']['news']
        alsoProvides(request, IDisableCSRFProtection)
        import pdb; pdb.set_trace()


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


class ProfileView(BrowserView):
    """ Profile View (for profile)
    """
    index = ViewPageTemplateFile('template/profile_view.pt')

    def __call__(self):
        return self.index()


class RawView(BrowserView):
    """ Raw View (for profile)
    """
    index = ViewPageTemplateFile('template/raw_view.pt')

    def __call__(self):
        return self.index()


class NTUAMacro(BrowserView):
    """ NTUA Macro
    """


class SearchResult(BrowserView):
    """ Search Result
    """
    index = ViewPageTemplateFile('template/search_result.pt')

    def __call__(self):
        context = self.context
        request = self.request
        response = request.response
        portal = api.portal.get()
        catalog = context.portal_catalog

        keyword = request.form.get('keyword')
        if not keyword:
            response.redirect(portal.absolute_url())
            return

        self.brain = catalog({
            'Type':['Folder', 'Page', 'File'],
            'SearchableText': keyword,},
            sort_on = 'Type',
            sort_order = 'reverse',
        )

        return self.index()
