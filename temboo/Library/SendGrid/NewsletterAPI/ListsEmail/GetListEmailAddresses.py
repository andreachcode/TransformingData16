# -*- coding: utf-8 -*-

###############################################################################
#
# GetListEmailAddresses
# Retrieve email addresses associated with a specified Recipient List.
#
# Python versions 2.6, 2.7, 3.x
#
# Copyright 2014, Temboo Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
#
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetListEmailAddresses(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetListEmailAddresses Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetListEmailAddresses, self).__init__(temboo_session, '/Library/SendGrid/NewsletterAPI/ListsEmail/GetListEmailAddresses')


    def new_input_set(self):
        return GetListEmailAddressesInputSet()

    def _make_result_set(self, result, path):
        return GetListEmailAddressesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetListEmailAddressesChoreographyExecution(session, exec_id, path)

class GetListEmailAddressesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetListEmailAddresses
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key obtained from SendGrid.)
        """
        super(GetListEmailAddressesInputSet, self)._set_input('APIKey', value)
    def set_APIUser(self, value):
        """
        Set the value of the APIUser input for this Choreo. ((required, string) The username registered with SendGrid.)
        """
        super(GetListEmailAddressesInputSet, self)._set_input('APIUser', value)
    def set_Email(self, value):
        """
        Set the value of the Email input for this Choreo. ((optional, string) The email address to search for in a recipient list.)
        """
        super(GetListEmailAddressesInputSet, self)._set_input('Email', value)
    def set_List(self, value):
        """
        Set the value of the List input for this Choreo. ((required, string) The recipient list from which email addresses will be retrieved.  Must be an existing recipient list.)
        """
        super(GetListEmailAddressesInputSet, self)._set_input('List', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format of the response from SendGrid, in either json, or xml.  Default is set to json.)
        """
        super(GetListEmailAddressesInputSet, self)._set_input('ResponseFormat', value)


class GetListEmailAddressesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetListEmailAddresses Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from SendGrid. The format corresponds to the ResponseFormat input. Default is json.)
        """
        return self._output.get('Response', None)

class GetListEmailAddressesChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetListEmailAddressesResultSet(response, path)
