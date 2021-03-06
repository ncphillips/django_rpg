from rest_framework import serializers
from rpg_base.models import Location

class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = (
            'pk', 'name', 'description', 'parent_location', 'campaign',
        )

