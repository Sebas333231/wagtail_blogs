from django.db import models
from django import forms
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.snippets.models import register_snippet
# Create your models here.


class BlogPage(Page):
    intro = RichTextField(blank=True)
    authors = ParentalManyToManyField('blog.Author', blank=True)


    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('authors', widget= forms.CheckboxSelectMultiple)
    ]

    subpage_types = [
        "PostPage"
    ]


class PostPage(Page):
    date = models.DateField('Post Date')
    summary = models.CharField(max_length=250)
    body = RichTextField()

    authors = ParentalManyToManyField('blog.Author', blank=True)

    content_panels = Page.content_panels +[
        FieldPanel('date'),
        FieldPanel('authors', widget= forms.CheckboxSelectMultiple),
        FieldPanel('summary'),
        FieldPanel('body'),
        InlinePanel('gallery_images', label="Gallery images")
    ]

    parent_page_type = [
        "BlogPage"
    ]


class BlogPageGalleryImage(Orderable):
    page = ParentalKey(PostPage, on_delete=models.CASCADE, related_name="gallery_images")
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name="+"
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        FieldPanel('image'),
        FieldPanel('caption')
    ]

@register_snippet
class Author(models.Model):
    name = models.CharField(max_length=255)
    author_image = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)
    correo = models.CharField(blank=True, max_length=250)

    pannels = [
        FieldPanel('name'),
        InlinePanel('author_image', label="Gallery Images"),
        FieldPanel('caption'),
        FieldPanel('correo')
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Authors'