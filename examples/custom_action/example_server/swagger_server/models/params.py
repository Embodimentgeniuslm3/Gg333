# coding: utf-8

from __future__ import absolute_import

from typing import List

from .base_model_ import Model
from .. import util


class Params(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(
        self,
        target_dialogue_state: str = None,
        dynamic_resource: object = None,
        allowed_intents: List[str] = None,
        time_zone: str = None,
        language: str = None,
        locale: str = None,
        timestamp: int = None,
    ):
        """Params - a model defined in Swagger

        :param target_dialogue_state: The target_dialogue_state of this Params.
        :type target_dialogue_state: str
        :param dynamic_resource: The dynamic_resource of this Params.
        :type dynamic_resource: object
        :param allowed_intents: The allowed_intents of this Params.
        :type allowed_intents: List[str]
        :param time_zone: The time_zone of this Params.
        :type time_zone: str
        :param language: The language of this Params.
        :type language: str
        :param locale: The locale of this Params.
        :type locale: str
        :param timestamp: The timestamp of this Params.
        :type timestamp: int
        """
        self.swagger_types = {
            "target_dialogue_state": str,
            "dynamic_resource": object,
            "allowed_intents": List[str],
            "time_zone": str,
            "language": str,
            "locale": str,
            "timestamp": int,
        }

        self.attribute_map = {
            "target_dialogue_state": "target_dialogue_state",
            "dynamic_resource": "dynamic_resource",
            "allowed_intents": "allowed_intents",
            "time_zone": "time_zone",
            "language": "language",
            "locale": "locale",
            "timestamp": "timestamp",
        }
        self._target_dialogue_state = target_dialogue_state
        self._dynamic_resource = dynamic_resource
        self._allowed_intents = allowed_intents
        self._time_zone = time_zone
        self._language = language
        self._locale = locale
        self._timestamp = timestamp

    @classmethod
    def from_dict(cls, dikt) -> "Params":
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Params of this Params.
        :rtype: Params
        """
        return util.deserialize_model(dikt, cls)

    @property
    def target_dialogue_state(self) -> str:
        """Gets the target_dialogue_state of this Params.

        The name of next turn's dialogue state (if set)

        :return: The target_dialogue_state of this Params.
        :rtype: str
        """
        return self._target_dialogue_state

    @target_dialogue_state.setter
    def target_dialogue_state(self, target_dialogue_state: str):
        """Sets the target_dialogue_state of this Params.

        The name of next turn's dialogue state (if set)

        :param target_dialogue_state: The target_dialogue_state of this Params.
        :type target_dialogue_state: str
        """

        self._target_dialogue_state = target_dialogue_state

    @property
    def dynamic_resource(self) -> object:
        """Gets the dynamic_resource of this Params.

        The additional values for gazetteer

        :return: The dynamic_resource of this Params.
        :rtype: object
        """
        return self._dynamic_resource

    @dynamic_resource.setter
    def dynamic_resource(self, dynamic_resource: object):
        """Sets the dynamic_resource of this Params.

        The additional values for gazetteer

        :param dynamic_resource: The dynamic_resource of this Params.
        :type dynamic_resource: object
        """

        self._dynamic_resource = dynamic_resource

    @property
    def allowed_intents(self) -> List[str]:
        """Gets the allowed_intents of this Params.

        The list of allowed intents for next turn (if set)

        :return: The allowed_intents of this Params.
        :rtype: List[str]
        """
        return self._allowed_intents

    @allowed_intents.setter
    def allowed_intents(self, allowed_intents: List[str]):
        """Sets the allowed_intents of this Params.

        The list of allowed intents for next turn (if set)

        :param allowed_intents: The allowed_intents of this Params.
        :type allowed_intents: List[str]
        """

        self._allowed_intents = allowed_intents

    @property
    def time_zone(self) -> str:
        """Gets the time_zone of this Params.

        The time zone of the request

        :return: The time_zone of this Params.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone: str):
        """Sets the time_zone of this Params.

        The time zone of the request

        :param time_zone: The time_zone of this Params.
        :type time_zone: str
        """

        self._time_zone = time_zone

    @property
    def language(self) -> str:
        """Gets the language of this Params.

        The language of the request

        :return: The language of this Params.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language: str):
        """Sets the language of this Params.

        The language of the request

        :param language: The language of this Params.
        :type language: str
        """

        self._language = language

    @property
    def locale(self) -> str:
        """Gets the locale of this Params.

        The locale of the request

        :return: The locale of this Params.
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale: str):
        """Sets the locale of this Params.

        The locale of the request

        :param locale: The locale of this Params.
        :type locale: str
        """

        self._locale = locale

    @property
    def timestamp(self) -> int:
        """Gets the timestamp of this Params.

        The timestamp of the request

        :return: The timestamp of this Params.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp: int):
        """Sets the timestamp of this Params.

        The timestamp of the request

        :param timestamp: The timestamp of this Params.
        :type timestamp: int
        """

        self._timestamp = timestamp
