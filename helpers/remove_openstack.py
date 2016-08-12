#!/usr/bin/env python

# Author: Jaime Alvarez <jalvarez@itri.org.tw>

""" 
This script removes the OpenStack Infrastructure endpoint device from the Zenoss
/OpenStack/Infrastructure device class. Additionally, it also removes the discovered
devices found in /Server/SSH/Linux/NovaHost
"""
import Globals
from Products.ZenUtils.ZenScriptBase import ZenScriptBase
from transaction import commit

# Get the DMD object
dmd = ZenScriptBase(connect=True, noopts=True).dmd

# Delete the OpenStack Infrastructure endpoint device(s).
for endpoint in dmd.Devices.getOrganizer('/OpenStack/Infrastructure').getSubDevices():
    endpoint.deleteDevice()

commit()

# Delete the NovaHost devices
for device in dmd.Devices.getOrganizer('/Server/SSH/Linux/NovaHost').getSubDevices():
    device.deleteDevice()

commit()
