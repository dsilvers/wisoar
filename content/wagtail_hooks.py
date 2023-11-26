from django.core.exceptions import ObjectDoesNotExist
from django.utils.html import escape

from wagtail import hooks
from wagtail.documents.rich_text import DocumentLinkHandler

# magical things happening here

# https://docs.wagtail.io/en/stable/advanced_topics/customisation/rich_text_internals.html

# https://github.com/wagtail/wagtail/blob/ba6f94def17b8bbc66002cbc7af60ed422658ff1/wagtail/documents/rich_text/__init__.py

# https://github.com/wagtail/wagtail/blob/ba6f94def17b8bbc66002cbc7af60ed422658ff1/wagtail/documents/wagtail_hooks.py


class FancyDocumentLinkHandler(DocumentLinkHandler):
    @classmethod
    def expand_db_attributes(cls, attrs):
        try:
            doc = cls.get_instance(attrs)
            return '<a tacos="yes" href="%s">' % escape(doc.url)
        except (ObjectDoesNotExist, KeyError):
            return "<a>"


@hooks.register('register_rich_text_features')
def register_document_feature(features):
    features.register_link_type(FancyDocumentLinkHandler)
