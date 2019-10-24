from tastypie.resources import ModelResource
from api.models import Shipment_details
from tastypie.authorization import Authorization
from tastypie.constants import ALL

class shipment_op(ModelResource):
    class Meta:
        queryset = Shipment_details.objects.all()
        resource_name = 'ship'
        authorization = Authorization()
        filtering={"shipment_ID": ALL}
        fields = ['shipment_ID', 'destination_pincode', 'no_of_devices_shipped', 'status']