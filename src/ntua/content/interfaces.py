# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from ntua.content import _
from zope import schema
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from plone.namedfile.field import NamedBlobImage


class INtuaContentLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class ICover(Interface):

    title = schema.TextLine(
        title=_(u"Title"),
        required=True,
    )

    description = schema.Text(
        title=_(u"Description"),
        required=False,
    )

    heroURL = schema.List(
        title=_(u"Hero URL"),
        value_type=schema.TextLine(title=_(u"Hero URL")),
        required=False,
    )

    footerVideo = schema.Text(
        title=_(u"Footer Video"),
        description=_(u"Youtube Video in Footer"),
        required=True,
    )


class IProfile(Interface):

    title = schema.TextLine(
        title=_(u"Title"),
        required=True,
    )

    jobTitle = schema.TextLine(
        title=_(u"Job Title"),
        required=True,
    )

    image = NamedBlobImage(
        title=_(u"Profile Image"),
        required=False,
    )
