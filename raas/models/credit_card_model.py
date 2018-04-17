# -*- coding: utf-8 -*-

"""
    raas.models.credit_card_model

    This file was automatically generated for Tango Card, Inc. by APIMATIC v2.0 ( https://apimatic.io )
"""
from raas.api_helper import APIHelper

class CreditCardModel(object):

    """Implementation of the 'CreditCard' model.

    Credit Card

    Attributes:
        customer_identifier (string): TODO: type description here.
        account_identifier (string): TODO: type description here.
        token (string): TODO: type description here.
        label (string): TODO: type description here.
        last_four_digits (string): TODO: type description here.
        expiration_date (string): TODO: type description here.
        status (string): TODO: type description here.
        created_date (datetime): TODO: type description here.
        activation_date (datetime): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "customer_identifier":'customerIdentifier',
        "account_identifier":'accountIdentifier',
        "token":'token',
        "label":'label',
        "last_four_digits":'lastFourDigits',
        "expiration_date":'expirationDate',
        "status":'status',
        "created_date":'createdDate',
        "activation_date":'activationDate'
    }

    def __init__(self,
                 customer_identifier=None,
                 account_identifier=None,
                 token=None,
                 label=None,
                 last_four_digits=None,
                 expiration_date=None,
                 status=None,
                 created_date=None,
                 activation_date=None):
        """Constructor for the CreditCardModel class"""

        # Initialize members of the class
        self.customer_identifier = customer_identifier
        self.account_identifier = account_identifier
        self.token = token
        self.label = label
        self.last_four_digits = last_four_digits
        self.expiration_date = expiration_date
        self.status = status
        self.created_date = APIHelper.RFC3339DateTime(created_date) if created_date else None
        self.activation_date = APIHelper.RFC3339DateTime(activation_date) if activation_date else None


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
        token = dictionary.get('token')
        label = dictionary.get('label')
        last_four_digits = dictionary.get('lastFourDigits')
        expiration_date = dictionary.get('expirationDate')
        status = dictionary.get('status')
        created_date = APIHelper.RFC3339DateTime.from_value(dictionary.get("createdDate")).datetime if dictionary.get("createdDate") else None
        activation_date = APIHelper.RFC3339DateTime.from_value(dictionary.get("activationDate")).datetime if dictionary.get("activationDate") else None

        # Return an object of this model
        return cls(customer_identifier,
                   account_identifier,
                   token,
                   label,
                   last_four_digits,
                   expiration_date,
                   status,
                   created_date,
                   activation_date)


