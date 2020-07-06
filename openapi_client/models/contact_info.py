# coding: utf-8

"""
    SBC Pay API Reference

    BC Registries Pay API reference documentation  # noqa: E501

    The version of the OpenAPI document: 1.0.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class ContactInfo(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'address_line1': 'str',
        'city': 'str',
        'province': 'str',
        'postal_code': 'str',
        'country': 'str'
    }

    attribute_map = {
        'address_line1': 'addressLine1',
        'city': 'city',
        'province': 'province',
        'postal_code': 'postalCode',
        'country': 'country'
    }

    def __init__(self, address_line1=None, city=None, province=None, postal_code=None, country=None, local_vars_configuration=None):  # noqa: E501
        """ContactInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._address_line1 = None
        self._city = None
        self._province = None
        self._postal_code = None
        self._country = None
        self.discriminator = None

        if address_line1 is not None:
            self.address_line1 = address_line1
        if city is not None:
            self.city = city
        if province is not None:
            self.province = province
        if postal_code is not None:
            self.postal_code = postal_code
        if country is not None:
            self.country = country

    @property
    def address_line1(self):
        """Gets the address_line1 of this ContactInfo.  # noqa: E501

        Address line 1  # noqa: E501

        :return: The address_line1 of this ContactInfo.  # noqa: E501
        :rtype: str
        """
        return self._address_line1

    @address_line1.setter
    def address_line1(self, address_line1):
        """Sets the address_line1 of this ContactInfo.

        Address line 1  # noqa: E501

        :param address_line1: The address_line1 of this ContactInfo.  # noqa: E501
        :type address_line1: str
        """

        self._address_line1 = address_line1

    @property
    def city(self):
        """Gets the city of this ContactInfo.  # noqa: E501

        City  # noqa: E501

        :return: The city of this ContactInfo.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this ContactInfo.

        City  # noqa: E501

        :param city: The city of this ContactInfo.  # noqa: E501
        :type city: str
        """

        self._city = city

    @property
    def province(self):
        """Gets the province of this ContactInfo.  # noqa: E501

        Province  # noqa: E501

        :return: The province of this ContactInfo.  # noqa: E501
        :rtype: str
        """
        return self._province

    @province.setter
    def province(self, province):
        """Sets the province of this ContactInfo.

        Province  # noqa: E501

        :param province: The province of this ContactInfo.  # noqa: E501
        :type province: str
        """

        self._province = province

    @property
    def postal_code(self):
        """Gets the postal_code of this ContactInfo.  # noqa: E501

        Postal Code  # noqa: E501

        :return: The postal_code of this ContactInfo.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this ContactInfo.

        Postal Code  # noqa: E501

        :param postal_code: The postal_code of this ContactInfo.  # noqa: E501
        :type postal_code: str
        """

        self._postal_code = postal_code

    @property
    def country(self):
        """Gets the country of this ContactInfo.  # noqa: E501

        Country  # noqa: E501

        :return: The country of this ContactInfo.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this ContactInfo.

        Country  # noqa: E501

        :param country: The country of this ContactInfo.  # noqa: E501
        :type country: str
        """

        self._country = country

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ContactInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ContactInfo):
            return True

        return self.to_dict() != other.to_dict()