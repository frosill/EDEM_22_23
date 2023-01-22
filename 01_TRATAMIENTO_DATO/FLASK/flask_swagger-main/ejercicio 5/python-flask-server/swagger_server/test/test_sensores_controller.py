# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.meassure import Meassure  # noqa: E501
from swagger_server.models.message import Message  # noqa: E501
from swagger_server.test import BaseTestCase


class TestSensoresController(BaseTestCase):
    """SensoresController integration test stubs"""

    def test_get_historical_meassures_by_sensor_and_type(self):
        """Test case for get_historical_meassures_by_sensor_and_type

        Obtener la última medición de un sensor
        """
        response = self.client.open(
            '/v2/getHistoricalMeassuresBySensorAndType/{sensor}//{start}/{end}'.format(sensor='sensor_example', start='start_example', end='end_example'),
            method='GET',
            content_type='application/xml')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_last_meassure_by_sensor(self):
        """Test case for get_last_meassure_by_sensor

        Obtener la última medición de un sensor
        """
        response = self.client.open(
            '/v2/getLastMeassureBySensor/{sensor}'.format(sensor='sensor_example'),
            method='GET',
            content_type='application/xml')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
