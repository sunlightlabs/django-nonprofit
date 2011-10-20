from django.db import models
from email.utils import parseaddr

class Slot(models.Model):
    description = models.CharField(max_length=255)
    forward_to = models.TextField()
    enabled = models.BooleanField(default=True)
    
    class Meta:
        ordering = ('description',)
    
    def __unicode__(self):
        return self.description
    
    def recipients(self):
        for r in self.forward_to.split(','):
            (name, email) = parseaddr(r)
            if email:
                yield email
        
