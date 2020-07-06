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
from openapi_client.models.transactions import Transactions  # noqa: E501
from openapi_client.rest import ApiException

class TestTransactions(unittest.TestCase):
    """Transactions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Transactions
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.transactions.Transactions()  # noqa: E501
        if include_optional :
            return Transactions(
                items = [
                    openapi_client.models.transaction.Transaction(
                        _links = [
                            openapi_client.models.links.Links(
                                self = '0', 
                                collection = '0', )
                            ], 
                        id = '0', 
                        client_system_url = '0', 
                        start_time = '0', 
                        end_time = '0', 
                        pay_system_url = '0', 
                        payment_id = 56, 
                        status_code = 'DRAFT', )
                    ]
            )
        else :
            return Transactions(
        )

    def testTransactions(self):
        """Test Transactions"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()