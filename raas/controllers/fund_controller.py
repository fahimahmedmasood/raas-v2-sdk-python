# -*- coding: utf-8 -*-

"""
    raas.controllers.fund_controller

    This file was automatically generated for Tango Card, Inc. by APIMATIC v2.0 ( https://apimatic.io ).
"""

import logging
from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from ..http.auth.basic_auth import BasicAuth
from ..models.credit_card_model import CreditCardModel
from ..models.unregister_credit_card_response_model import UnregisterCreditCardResponseModel
from ..models.deposit_response_model import DepositResponseModel
from ..models.get_deposit_response_model import GetDepositResponseModel

class FundController(BaseController):

    """A Controller to access Endpoints in the raas API."""

    def __init__(self, client=None, call_back=None):
        super(FundController, self).__init__(client, call_back)
        self.logger = logging.getLogger(__name__)

    def get_credit_cards(self):
        """Does a GET request to /creditCards.

        List all credit cards registered on this platform

        Returns:
            list of CreditCardModel: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_credit_cards called.')
    
            # Prepare query URL
            self.logger.info('Preparing query URL for get_credit_cards.')
            _query_builder = Configuration.get_base_uri()
            _query_builder += '/creditCards'
            _query_url = APIHelper.clean_url(_query_builder)
    
            # Prepare headers
            self.logger.info('Preparing headers for get_credit_cards.')
            _headers = {
                'accept': 'application/json'
            }
    
            # Prepare and execute request
            self.logger.info('Preparing and executing request for get_credit_cards.')
            _request = self.http_client.get(_query_url, headers=_headers)
            BasicAuth.apply(_request)
            _context = self.execute_request(_request, name = 'get_credit_cards')
            self.validate_response(_context)
    
            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, CreditCardModel.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def create_credit_card(self,
                           body):
        """Does a POST request to /creditCards.

        Register a new credit card

        Args:
            body (CreateCreditCardRequestModel): TODO: type description here.
                Example: 

        Returns:
            CreditCardModel: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_credit_card called.')
    
            # Validate required parameters
            self.logger.info('Validating required parameters for create_credit_card.')
            self.validate_parameters(body=body)
    
            # Prepare query URL
            self.logger.info('Preparing query URL for create_credit_card.')
            _query_builder = Configuration.get_base_uri()
            _query_builder += '/creditCards'
            _query_url = APIHelper.clean_url(_query_builder)
    
            # Prepare headers
            self.logger.info('Preparing headers for create_credit_card.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }
    
            # Prepare and execute request
            self.logger.info('Preparing and executing request for create_credit_card.')
            _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
            BasicAuth.apply(_request)
            _context = self.execute_request(_request, name = 'create_credit_card')
            self.validate_response(_context)
    
            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, CreditCardModel.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def create_unregister_credit_card(self,
                                      body):
        """Does a POST request to /creditCardUnregisters.

        Unregister a credit card

        Args:
            body (UnregisterCreditCardRequestModel): TODO: type description
                here. Example: 

        Returns:
            UnregisterCreditCardResponseModel: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_unregister_credit_card called.')
    
            # Validate required parameters
            self.logger.info('Validating required parameters for create_unregister_credit_card.')
            self.validate_parameters(body=body)
    
            # Prepare query URL
            self.logger.info('Preparing query URL for create_unregister_credit_card.')
            _query_builder = Configuration.get_base_uri()
            _query_builder += '/creditCardUnregisters'
            _query_url = APIHelper.clean_url(_query_builder)
    
            # Prepare headers
            self.logger.info('Preparing headers for create_unregister_credit_card.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }
    
            # Prepare and execute request
            self.logger.info('Preparing and executing request for create_unregister_credit_card.')
            _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
            BasicAuth.apply(_request)
            _context = self.execute_request(_request, name = 'create_unregister_credit_card')
            self.validate_response(_context)
    
            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, UnregisterCreditCardResponseModel.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def create_deposit(self,
                       body):
        """Does a POST request to /creditCardDeposits.

        Fund an account

        Args:
            body (DepositRequestModel): TODO: type description here. Example:
                
        Returns:
            DepositResponseModel: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_deposit called.')
    
            # Validate required parameters
            self.logger.info('Validating required parameters for create_deposit.')
            self.validate_parameters(body=body)
    
            # Prepare query URL
            self.logger.info('Preparing query URL for create_deposit.')
            _query_builder = Configuration.get_base_uri()
            _query_builder += '/creditCardDeposits'
            _query_url = APIHelper.clean_url(_query_builder)
    
            # Prepare headers
            self.logger.info('Preparing headers for create_deposit.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }
    
            # Prepare and execute request
            self.logger.info('Preparing and executing request for create_deposit.')
            _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
            BasicAuth.apply(_request)
            _context = self.execute_request(_request, name = 'create_deposit')
            self.validate_response(_context)
    
            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, DepositResponseModel.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def get_deposit(self,
                    deposit_id):
        """Does a GET request to /creditCardDeposits/{depositId}.

        Get details for a specific credit card deposit

        Args:
            deposit_id (string): Deposit ID

        Returns:
            GetDepositResponseModel: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_deposit called.')
    
            # Validate required parameters
            self.logger.info('Validating required parameters for get_deposit.')
            self.validate_parameters(deposit_id=deposit_id)
    
            # Prepare query URL
            self.logger.info('Preparing query URL for get_deposit.')
            _query_builder = Configuration.get_base_uri()
            _query_builder += '/creditCardDeposits/{depositId}'
            _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
                'depositId': deposit_id
            })
            _query_url = APIHelper.clean_url(_query_builder)
    
            # Prepare headers
            self.logger.info('Preparing headers for get_deposit.')
            _headers = {
                'accept': 'application/json'
            }
    
            # Prepare and execute request
            self.logger.info('Preparing and executing request for get_deposit.')
            _request = self.http_client.get(_query_url, headers=_headers)
            BasicAuth.apply(_request)
            _context = self.execute_request(_request, name = 'get_deposit')
            self.validate_response(_context)
    
            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, GetDepositResponseModel.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def get_credit_card(self,
                        token):
        """Does a GET request to /creditCards/{token}.

        Get details for a specific credit card

        Args:
            token (string): Card Token

        Returns:
            CreditCardModel: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_credit_card called.')
    
            # Validate required parameters
            self.logger.info('Validating required parameters for get_credit_card.')
            self.validate_parameters(token=token)
    
            # Prepare query URL
            self.logger.info('Preparing query URL for get_credit_card.')
            _query_builder = Configuration.get_base_uri()
            _query_builder += '/creditCards/{token}'
            _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
                'token': token
            })
            _query_url = APIHelper.clean_url(_query_builder)
    
            # Prepare headers
            self.logger.info('Preparing headers for get_credit_card.')
            _headers = {
                'accept': 'application/json'
            }
    
            # Prepare and execute request
            self.logger.info('Preparing and executing request for get_credit_card.')
            _request = self.http_client.get(_query_url, headers=_headers)
            BasicAuth.apply(_request)
            _context = self.execute_request(_request, name = 'get_credit_card')
            self.validate_response(_context)
    
            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, CreditCardModel.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise
