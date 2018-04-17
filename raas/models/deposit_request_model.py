# -*- coding: utf-8 -*-

"""
    raas.models.deposit_request_model

    This file was automatically generated for Tango Card, Inc. by APIMATIC v2.0 ( https://apimatic.io )
"""


class DepositRequestModel(object):

    """Implementation of the 'DepositRequest' model.

    Fund Account Request

    Attributes:
        customer_identifier (string): TODO: type description here.
        account_identifier (string): TODO: type description here.
        credit_card_token (string): TODO: type description here.
        amount (float): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "customer_identifier":'customerIdentifier',
        "account_identifier":'accountIdentifier',
        "credit_card_token":'creditCardToken',
        "amount":'amount'
    }

    def __init__(self,
                 customer_identifier=None,
                 account_identifier=None,
                 credit_card_token=None,
                 amount=None):
        """Constructor for the DepositRequestModel class"""

        # Initialize members of the class
        self.customer_identifier = customer_identifier
        self.account_identifier = account_identifier
        self.credit_card_token = credit_card_token
        self.amount = amount


    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        customer_identifier = dictionary.get('customerIdentifier')
        account_identifier = dictionary.get('accountIdentifier')
        credit_card_token = dictionary.get('creditCardToken')
        amount = dictionary.get('amount')

        # Return an object of this model
        return cls(customer_identifier,
                   account_identifier,
                   credit_card_token,
                   amount)


