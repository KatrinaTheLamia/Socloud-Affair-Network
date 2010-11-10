#!/bin/nologin
"""
	= %(Sokloud_Affair-source)path/sokloud.py
	@Authors: %(KatrinaTheLamia)user
	@Groups: %(NIMHLabs)group, %(SpectrumLabs)group, %(MistofHoenn)group
		%(Sokloud_Affair)group
	@Projects: %(Sokloud_Affair)project, %(RoseBush)project
	@Creation: 3176-5-22

	The "brain" of the Sokloud Affiar node. Decides how to jerk the 
	request into the circle

	== Revisions
	+ 3176-5-22 Created the file

	== TODO
	! Impliment
	! Document
	! Debug
	! Document
"""

import WSGI

import lib "."

import authentication
import loader
import content
import error

class Sokloud(Object):

	def __init__(self):
		self.wsgi = new WSGI()
		self._parse_headers()
		self._quaruntine_content()

	def get_request_type():
		if self._request_type = "auth":
			return authentication.spawn(self._request_auth_type, self._content_local)
		elif self._request_type = "network":
			return loader.network(self._request_network_type, self._content_local)
		elif self._request_type = "content":
			return content.talk(self._request_content_type, self._content_local)
		else
			return error.Unknown_Type()
	def _parse_headers()
		pass

	def _quaruntine_content()
		pass

