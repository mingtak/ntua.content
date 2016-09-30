# -*- coding: utf-8 -*-
from plone.indexer.decorator import indexer
from zope.interface import Interface


@indexer(Interface)
def outside_notice_indexer(obj):
    return obj.outside_notice
