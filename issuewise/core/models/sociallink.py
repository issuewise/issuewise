from django.db import models
from django.utils.translation import ugettext_lazy as _


class SocialLinkMixin(models.Model):

    LINK_TYPE_CHOICES = (
        ('SOC', 'social profile'),
        ('BLO', 'blog'),
        ('PER', 'personal website'),
        ('ORG', 'organization website'),
        )

    WEBSITE_CHOICES = (
        ('PER', 'Personal'),
        ('ORG', 'Organization'),
        ('FAC', 'Facebook'),
        ('TWI', 'Twitter'),
        ('GOO', 'Google'),
        ('YOU', 'Youtube'),
        ('SIN', 'Sina Weibo'),
        ('QZO', 'Qzone'),
        ('VIN', 'Vine'),
        ('INS', 'Instagram'),
        ('VK', 'VK'),
        ('LIN', 'Linkedin'),
        ('REN', 'Renren'),
        ('PIN', 'Pinterest'),
        ('TUM', 'Tumblr'),
        ('FRI', 'Friendster'),
        ('FOU', 'Foursquare'),
        ('PAT', 'Path'),
        ('MYS', 'Myspace'),
        ('TUE', 'Tuenti'),
        ('WOR', 'Wordpress'),
        ('BLO', 'Blogger'),
        ('SQU', 'Squarepage'),
        ('MED', 'Medium'),
        ('HUB', 'Hubpages'),
        ('JUM', 'Jumla'),
        ('LIV', 'Live Journal'),
        ('QUO', 'Quora'),
        ('TYP', 'Typepad'),
        ('WEE', 'Weebly'),
        ('DRU', 'Drupal'),
        ('SQU', 'Squidoo'),
        ('POS', 'Postachio'),
        ('FBN', 'Facebook Notes'),
        ('SVT', 'Svtle'),
        ('SET', 'Sett'),
        ('GHO', 'Ghost'),
        ('PHA', 'Posthaven'),
        ('PRS', 'Posterous'),
        ('BLG', 'Blog'),
        ('ZOO', 'Zoomshare'),
        ('XAN', 'Xanga'),
)
    
    url = models.URLField(_('social link'), max_length = 300)
    website = models.CharField(_('link to website'), 
        choices = WEBSITE_CHOICES)
    link_type = models.CharField(_('this link goes to a'), max_length =3,
        choices = LINK_TYPE_CHOICES)


    class Meta:
        abstract = True
