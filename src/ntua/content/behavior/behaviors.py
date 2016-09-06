from ntua.content import _
#from plone.autoform import directives
from plone.supermodel import directives
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from zope.component import adapts
from zope.interface import alsoProvides, implements
from zope.interface import provider
from z3c.relationfield.schema import RelationList, RelationChoice
from plone.app.vocabularies.catalog import CatalogSource
from plone.dexterity.interfaces import IDexterityContent


class ITagMembers(model.Schema):
    """Add tag members to content
    """

    directives.fieldset(
            'Members',
            label=_(u'Members'),
            fields=('tags',),
        )

    tags = RelationList(
        title=_(u"Tag Members"),
        value_type=RelationChoice(title=_(u"Related"),
                                  source=CatalogSource(portal_type='Profile'),),
        required=False,
    )


alsoProvides(ITagMembers, IFormFieldProvider)


def context_property(name):
    def getter(self):
        return getattr(self.context, name)
    def setter(self, value):
        setattr(self.context, name, value)
    def deleter(self):
        delattr(self.context, name)
    return property(getter, setter, deleter)


class TagMembers(object):
    implements(ITagMembers)
    adapts(IDexterityContent)

    def __init__(self,context):
        self.context = context

    # -*- Your behavior property setters & getters here ... -*-
    tags = context_property("tags")

