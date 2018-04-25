# -*- coding: utf-8 -*-

"""
    tests.controllers.test_exchange_rates_controller

    This file was automatically generated for Tango Card, Inc. by APIMATIC v2.0 ( https://apimatic.io ).
"""

import jsonpickle
import dateutil.parser
from .controller_test_base import ControllerTestBase
from ..test_helper import TestHelper
from raas.api_helper import APIHelper


class ExchangeRatesControllerTests(ControllerTestBase):

    @classmethod
    def setUpClass(cls):
        super(ExchangeRatesControllerTests, cls).setUpClass()
        cls.controller = cls.api_client.exchange_rates

