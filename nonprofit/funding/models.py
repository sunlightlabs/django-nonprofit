from django.db import models
import datetime

def this_year():
    return datetime.datetime.utcnow().year

class Contribution(models.Model):
    year = models.IntegerField(default=this_year)
    contributor = models.CharField(max_length=128)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    note = models.TextField(blank=True)
    is_inkind = models.BooleanField(default=False)
    
    class Meta:
        ordering = ('-year','-amount','contributor')
    
    def __unicode__(self):
        return u"%s %s $%s" % (self.year, self.contributor, self.amount)

class Grant(models.Model):
    year = models.IntegerField(default=this_year)
    recipient = models.CharField(max_length=128)
    recipient_url = models.URLField(verify_exists=False, blank=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    purpose = models.TextField(blank=True)
    is_minigrant = models.BooleanField(default=False)
    
    class Meta:
        ordering = ('-year','-amount','recipient')
        
    def __unicode__(self):
        return u"%s %s $%s" % (self.year, self.recipient, self.amount)