from django.db import models

from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel

from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.contrib.settings.models import BaseGenericSetting, register_setting
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.images.models import Image as WagtailImage
from wagtail.snippets.models import register_snippet


class HomePageItem(models.Model):
    heading = models.CharField(max_length=255, blank=True)
    content = RichTextField(blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    link = models.ForeignKey('wagtailcore.Page', on_delete=models.CASCADE)
    button_text = models.CharField(max_length=255, blank=True)
    page = ParentalKey('HomePage', related_name='homepageitems')


class HomePage(Page):
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    hero_heading = models.CharField(max_length=255, blank=True)
    hero_subheading = models.CharField(max_length=255, blank=True)

    home_heading = models.CharField(max_length=255, blank=True)
    home_content = RichTextField(blank=True)

    hero_button_link = models.ForeignKey(
        'wagtailcore.Page',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="homepage_hero_button_link",
    )
    hero_button_text = models.CharField(max_length=255, blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel('hero_image'),
                FieldPanel('hero_heading'),
                FieldPanel('hero_subheading'),
                FieldPanel('hero_button_link'),
                FieldPanel('hero_button_text'),
            ],
            heading="Hero Image and Content",
        ),

        MultiFieldPanel(
            [
                FieldPanel('home_heading'),
                FieldPanel('home_content'),
            ],
            heading="Homepage Content",
        ),

        InlinePanel('homepageitems', label='Home Page Items'),
    ]


class GenericPage(Page):
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    hero_heading = models.CharField(max_length=255, blank=True)
    hero_subheading = models.CharField(max_length=255, blank=True)

    content = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel('hero_image'),
                FieldPanel('hero_heading'),
                FieldPanel('hero_subheading'),
            ],
            heading="Hero Image and Content",
        ),

        MultiFieldPanel(
            [
                FieldPanel('content'),
            ],
            heading="Page Content",
        ),
    ]


@register_setting
class SocialMediaSettings(BaseGenericSetting):
    copyright = models.CharField(help_text='Copyright Blurb at bottom of page', max_length=255, blank=True)
    facebook = models.URLField(help_text='Your Facebook page URL')
    email = models.EmailField(help_text='Your Contact Email Address')

    class Meta:
        verbose_name = 'social media accounts'
