import json

from django.conf import settings
from wagtail.admin.panels import FieldPanel

from .widgets import MapInput


class MapFieldPanel(FieldPanel):
    def __init__(self, field_name, *args, **kwargs):
        self.default_centre = kwargs.pop('centre', getattr(settings, 'WAGTAIL_ADDRESS_MAP_CENTER', None))
        self.zoom = kwargs.pop('zoom', getattr(settings, 'WAGTAIL_ADDRESS_MAP_ZOOM', 8))
        self.latlng = kwargs.pop('latlng', False)

        super().__init__(field_name, *args, **kwargs)

    def clone(self):
        instance = super().clone()

        instance.default_centre = self.default_centre
        instance.zoom = self.zoom
        instance.latlng = self.latlng

        return instance

    def classes(self):
        classes = super().classes()
        classes.append('wagtailgmap')
        return classes

    def get_form_options(self):
        form_options = super().get_form_options()
        form_options["widgets"] = {self.field_name: MapInput(
            default_centre=self.default_centre,
            zoom=12,
            latlng=self.latlng
        )}
        return form_options
