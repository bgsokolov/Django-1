from django.db import models
from django.urls import reverse     #Used to generate URLs by reversing the URL patterns

# Create your models here.
class Mode(models.Model):
    """
    Model representing a running mode: Full, Network, Real, Virtual.
    """
    mode_name = models.CharField(max_length=20, help_text="Running Mode Name")
    mode_desc = models.CharField(max_length=100, help_text="Running Mode Description")

    def get_absolute_url(self):
        """
        Returns the url to access a particular mode instance.
        """
        return reverse('mode-detail', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.mode_name



#mode_list = [
#    {
#    'name': 'FULL',
#    'description': ('Full config generation mode.'),
#    },
#    {
#    'name': 'NET',
#    'description': ('Network configuration (ip, vlan, mgmt).'),
#    },
#    {
#    'name': 'REAL',
#    'description': ('Real Servers and Health Checks configuration.'),
#    },
#    {
#    'name': 'VIRT',
#    'description': ('Virtual Servers (FARM) configuration.'),
#    },
#]
