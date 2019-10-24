from django.db import models



#choices
STATUS_CHOICES = (
    ('ready-for-dispatch', 'Ready for dispatch'),
    ('in-transit', 'In transit'),
    ('delivered', 'Delivered'),
    ('canceled', 'Canceled'),
)
# Create your models here.
class Shipment_details(models.Model):
    shipment_ID = models.IntegerField()
    destination_pincode = models.IntegerField()
    no_of_devices_shipped = models.IntegerField()
    status=models.CharField(max_length=20, choices=STATUS_CHOICES, default='r')
def __str__(self):
        return self.shipment_ID
