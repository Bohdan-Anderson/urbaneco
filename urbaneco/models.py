# MODELS -- EVENTS -- SPEAKERS
from django.db import models
from django.template.defaultfilters import slugify

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    # affiliation = models.CharField(max_length=30)
    slug = models.SlugField(blank=True)
    
    def __unicode__(self):
        return self.first_name + " " + self.last_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.first_name + " " + self.last_name)
        super(Person, self).save(*args, **kwargs)

class Theme(models.Model):
    theme_name = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    slug = models.SlugField(blank=True)

    def __unicode__(self):
        return self.theme_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.theme_name)
        super(Theme, self).save(*args, **kwargs)

class Event(models.Model):
    event_name = models.CharField(max_length=30)
    time = models.DateTimeField(blank=True)
    location = models.CharField(max_length=30, blank=True)
    description = models.TextField(max_length=400, blank=True)
    slug = models.SlugField(blank=True)
    
    # RELATIONSHIPS
    speakers = models.ManyToManyField(Person, through='Membership', blank=True)
    themes = models.ManyToManyField(Theme)

    
    def __unicode__(self):
        return self.event_name
        
    def save(self, *args, **kwargs):
        self.slug = slugify(self.event_name)
        super(Event, self).save(*args, **kwargs)

class Membership(models.Model):
    person = models.ForeignKey(Person)
    event = models.ForeignKey(Event)
    role = models.CharField(max_length=50)
    
    def __unicode__(self):
        return "name: " + self.person.first_name + "// event: " + self.event.event_name + "// role: " + self.role