# -*- coding: utf-8 -*-

###############################################################################
#
# RemoveFromFavorites
# Removes a photo from a user's favorites list.
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

class RemoveFromFavorites(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RemoveFromFavorites Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(RemoveFromFavorites, self).__init__(temboo_session, '/Library/Flickr/Favorites/RemoveFromFavorites')


    def new_input_set(self):
        return RemoveFromFavoritesInputSet()

    def _make_result_set(self, result, path):
        return RemoveFromFavoritesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RemoveFromFavoritesChoreographyExecution(session, exec_id, path)

class RemoveFromFavoritesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RemoveFromFavorites
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Flickr (AKA the OAuth Consumer Key).)
        """
        super(RemoveFromFavoritesInputSet, self)._set_input('APIKey', value)
    def set_APISecret(self, value):
        """
        Set the value of the APISecret input for this Choreo. ((required, string) The API Secret provided by Flickr (AKA the OAuth Consumer Secret).)
        """
        super(RemoveFromFavoritesInputSet, self)._set_input('APISecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        super(RemoveFromFavoritesInputSet, self)._set_input('AccessToken', value)
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret retrieved during the OAuth process.)
        """
        super(RemoveFromFavoritesInputSet, self)._set_input('AccessTokenSecret', value)
    def set_PhotoID(self, value):
        """
        Set the value of the PhotoID input for this Choreo. ((required, integer) The id of the photo to remove from the user's favorites.)
        """
        super(RemoveFromFavoritesInputSet, self)._set_input('PhotoID', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: xml and json. Defaults to json.)
        """
        super(RemoveFromFavoritesInputSet, self)._set_input('ResponseFormat', value)

class RemoveFromFavoritesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RemoveFromFavorites Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Flickr.)
        """
        return self._output.get('Response', None)

class RemoveFromFavoritesChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return RemoveFromFavoritesResultSet(response, path)
