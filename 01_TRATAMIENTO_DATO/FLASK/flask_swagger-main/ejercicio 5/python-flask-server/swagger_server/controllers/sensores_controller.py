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
    res=Meassure(sensor,start,'grados centrigados','temperatura','10.2')
    return res


def get_last_meassure_by_sensor(sensor):  # noqa: E501
    """Obtener la última medición de un sensor

    Recuperar la última medición de un sensor # noqa: E501

    :param sensor: ID del sensor
    :type sensor: str

    :rtype: Meassure
    """
    res=Meassure(sensor,'16-12-2022 19:00:00','grados centrigados','temperatura','23.2')
    return res


