# Copyright (C) 2016 Canonical
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
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import os
import tempfile
import testflinger


class TestConfig:
    def test_default_config(self):
        app = testflinger.create_flask_app()
        assert app.config.get('REDIS_HOST') == 'localhost'
        assert app.config.get('REDIS_PORT') == '6379'

    def test_load_config(self):
        with tempfile.NamedTemporaryFile() as testconfig:
            testconfig.write('TEST_FOO="YES"'.encode())
            testconfig.flush()
            os.environ['TESTFLINGER_CONFIG'] = testconfig.name
            app = testflinger.create_flask_app()
            assert app.config.get('TEST_FOO') == 'YES'
