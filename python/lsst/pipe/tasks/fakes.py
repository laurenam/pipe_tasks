#
# LSST Data Management System
# Copyright 2008-2014 LSST Corporation.
#
# This product includes software developed by the
# LSST Project (http://www.lsst.org/).
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the LSST License Statement and
# the GNU General Public License along with this program.  If not,
# see <http://www.lsstcorp.org/LegalNotices/>.
#

import lsst.pex.config
import lsst.pipe.base

class FakeSourcesConfig(lsst.pex.config.Config):
    pass

class FakeSourcesTask(lsst.pipe.base.Task):
    ConfigClass = FakeSourcesConfig

    def __init__(self, **kwargs):
        lsst.pipe.base.Task.__init__(self, **kwargs)
        lsst.afw.image.MaskU.addMaskPlane("FAKE")
        self.bitmask = lsst.afw.image.MaskU.getPlaneBitMask("FAKE")

    def run(self, exposure, sources, background):
        pass

