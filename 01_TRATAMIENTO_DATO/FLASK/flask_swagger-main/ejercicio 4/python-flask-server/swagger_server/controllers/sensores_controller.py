import connexion
import six

from swagger_server.models.meassure import Meassure  # noqa: E501
from swagger_server.models.message import Message  # noqa: E501
from swagger_server import util


def get_historical_meassures_by_sensor_and_type(sensor, start, end):  # noqa: E501
    """Obtener la última medición de un sensor

    Recuperar la última medición de un sensor # noqa: E501

    :param sensor: ID del sensor
    :type sensor: str
    :param start: Fecha de inicio miliseconds
    :type start: str
    :param end: Fecha de fin miliseconds
    :type end: str

    :rtype: Meassure
    """
    return 'do some magic!'


def get_last_meassure_by_sensor(sensor):  # noqa: E501
    """Obtener la última medición de un sensor

    Recuperar la última medición de un sensor # noqa: E501

    :param sensor: ID del sensor
    :type sensor: str

    :rtype: Meassure
    """
    return 'do some magic!'
