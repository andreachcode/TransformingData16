# -*- coding: utf-8 -*-

###############################################################################
#
# FilterPlacesByMultipleCities
# Restrict a query to a specified city.
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

class FilterPlacesByMultipleCities(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the FilterPlacesByMultipleCities Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(FilterPlacesByMultipleCities, self).__init__(temboo_session, '/Library/Factual/FilterPlacesByMultipleCities')


    def new_input_set(self):
        return FilterPlacesByMultipleCitiesInputSet()

    def _make_result_set(self, result, path):
        return FilterPlacesByMultipleCitiesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return FilterPlacesByMultipleCitiesChoreographyExecution(session, exec_id, path)

class FilterPlacesByMultipleCitiesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the FilterPlacesByMultipleCities
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((optional, string) The API Key provided by Factual (AKA the OAuth Consumer Key).)
        """
        super(FilterPlacesByMultipleCitiesInputSet, self)._set_input('APIKey', value)
    def set_APISecret(self, value):
        """
        Set the value of the APISecret input for this Choreo. ((optional, string) The API Secret provided by Factual (AKA the OAuth Consumer Secret).)
        """
        super(FilterPlacesByMultipleCitiesInputSet, self)._set_input('APISecret', value)
    def set_Cities(self, value):
        """
        Set the value of the Cities input for this Choreo. ((required, json) A A JSON-encoded array of cities to filter results by.)
        """
        super(FilterPlacesByMultipleCitiesInputSet, self)._set_input('Cities', value)
    def set_Query(self, value):
        """
        Set the value of the Query input for this Choreo. ((optional, string) A search string (i.e. Starbucks).)
        """
        super(FilterPlacesByMultipleCitiesInputSet, self)._set_input('Query', value)

class FilterPlacesByMultipleCitiesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the FilterPlacesByMultipleCities Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Factual.)
        """
        return self._output.get('Response', None)

class FilterPlacesByMultipleCitiesChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return FilterPlacesByMultipleCitiesResultSet(response, path)
