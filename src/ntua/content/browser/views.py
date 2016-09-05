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
