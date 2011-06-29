""" AT Field
"""
from zope.interface import implements
from zope.publisher.interfaces import NotFound
from Products.Five.browser import BrowserView
from valentine.imagescales.browser.interfaces import IImageView


class ATFieldImageView(BrowserView):
    """ Image View
    """
    implements(IImageView)
    field = None

    def __init__(self, context, request):
        super(ATFieldImageView, self).__init__(context, request)
        self.field = context.getField('image')

    def display(self, scalename='thumb'):
        """ Display
        """
        return bool(self.field)

    def __call__(self, scalename='thumb'):
        if not self.display(scalename):
            raise NotFound(self.request, scalename)

        scale = self.field.getScale(self.context, scale=scalename)
        if scale:
            return scale

        return self.field.get(self.context).__of__(self.context)
