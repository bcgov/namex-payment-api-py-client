# coding: utf-8

"""
    SBC Pay API Reference

    BC Registries Pay API reference documentation  # noqa: E501

    The version of the OpenAPI document: 1.0.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.filing_type import FilingType  # noqa: E501
from openapi_client.rest import ApiException

class TestFilingType(unittest.TestCase):
    """FilingType unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test FilingType
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.filing_type.FilingType()  # noqa: E501
        if include_optional :
            return FilingType(
                filing_type_code = '0', 
                priority = True, 
                filing_description = '0'
            )
        else :
            return FilingType(
        )

    def testFilingType(self):
        """Test FilingType"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()