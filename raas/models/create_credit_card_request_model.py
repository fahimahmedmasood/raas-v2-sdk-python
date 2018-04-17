# -*- coding: utf-8 -*-

"""
    raas.models.create_credit_card_request_model

    This file was automatically generated for Tango Card, Inc. by APIMATIC v2.0 ( https://apimatic.io )
"""
import raas.models.new_credit_card_model
import raas.models.billing_address_model

class CreateCreditCardRequestModel(object):

    """Implementation of the 'CreateCreditCardRequest' model.

    Register Credit Card Request

    Attributes:
        customer_identifier (string): TODO: type description here.
        account_identifier (string): TODO: type description here.
        label (string): TODO: type description here.
        ip_address (string): TODO: type description here.
        credit_card (NewCreditCardModel): TODO: type description here.
        billing_address (BillingAddressModel): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "customer_identifier":'customerIdentifier',
        "account_identifier":'accountIdentifier',
        "label":'label',
        "ip_address":'ipAddress',
        "credit_card":'creditCard',
        "billing_address":'billingAddress'
    }

    def __init__(self,
                 customer_identifier=None,
                 account_identifier=None,
                 label=None,
                 ip_address=None,
                 credit_card=None,
                 billing_address=None):
        """Constructor for the CreateCreditCardRequestModel class"""

        # Initialize members of the class
        self.customer_identifier = customer_identifier
        self.account_identifier = account_identifier
        self.label = label
        self.ip_address = ip_address
        self.credit_card = credit_card
        self.billing_address = billing_address


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
        label = dictionary.get('label')
        ip_address = dictionary.get('ipAddress')
        credit_card = raas.models.new_credit_card_model.NewCreditCardModel.from_dictionary(dictionary.get('creditCard')) if dictionary.get('creditCard') else None
        billing_address = raas.models.billing_address_model.BillingAddressModel.from_dictionary(dictionary.get('billingAddress')) if dictionary.get('billingAddress') else None

        # Return an object of this model
        return cls(customer_identifier,
                   account_identifier,
                   label,
                   ip_address,
                   credit_card,
                   billing_address)


