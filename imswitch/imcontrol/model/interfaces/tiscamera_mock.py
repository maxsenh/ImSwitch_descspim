import numpy as np
from imswitch.imcontrol.model.interfaces.pymbacamera import AVCamera
 

class MockCameraTIS:
    def __init__(self):
        self.properties = {
            'image_height': 1024,
            'image_width': 1280,
            'subarray_vpos': 0,
            'subarray_hpos': 0,
            'exposure_time': 0.1,
            'subarray_vsize': 1024,
            'subarray_hsize': 1280
        }
        self.exposure = 100
        self.gain = 1
        self.brightness = 1
        self.model = 'mock'
                
        #%%
        self.camera = AVCamera()
        self.camera.start()



    def start_live(self):
        pass

    def stop_live(self):
        self.camera.stop()

    def suspend_live(self):
        pass

    def prepare_live(self):
        pass

    def setROI(self, hpos, vpos, hsize, vsize):
        pass

    def getLast(self, **kwargs):
        img = self.camera.last_frame
        return img

    def setPropertyValue(self, property_name, property_value):
        return property_value

    def getPropertyValue(self, property_name):
        return self.properties[property_name]

    def openPropertiesGUI(self):
        pass


# Copyright (C) 2020, 2021 TestaLab
# This file is part of ImSwitch.
#
# ImSwitch is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ImSwitch is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
