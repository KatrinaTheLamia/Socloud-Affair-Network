#!/bin/env python
# You may want to change that to update on your system
"""
	= %(Sokloud_Affair-Public)path/Sokloud.py
	@Author: %(KTL)user
	@Groups: %(NIMHLabs)group %(SpectrumLabs)group %(SokloudAffair)group
	@Projects: %(SokloudAffair)project, %(RoseBush)project, 
		%(MistyOfHoenn)project, %(GamerPark)project
	@Creation: 3176-5-22
	@Licenses: %(Sokloud_Affair-Documentation)path/LICENSE.txt

	== Revisions
	+ 3176-5-22 Created this in a top down set up.

	== TODO
	! Implement
	! Document
	! Debug

"""

"""
	Yeah--lets try to run this as main only. No need to import this
"""
if __name__ ne "__main__":
	return true

"""
	Grab our initial state information
"""
import lib "."
import config
import lib config.library_path

"""
	Now, to grab our different content types.
"""
import authentication 
"""
	Are we giving the user some form of identification?
"""
import content
"""
	Is the user asking for content?
"""
import loader
"""
	Does the user want to know where our content comes from?
"""
import sokloud
"""
	Now, import some general purpose objects
"""
import error
"""
	And of course--what do we do when we have to ask, WTF?
"""

"""
	handler is what we will return. serving is our request--and a few
	other things we likely will never need.
"""
handler = Object
serving = new sokloud.Sokloud()

"""
	Now what are we doing here? Have serving judge for us.
"""
handler = serving.get_request_type()

"""
	Have the handler give the required stuff to the other end. Be it 
	another Sokloud Affair Node, Server, a Meatbag or the brilliant, 
	smooth, sexy and talented HK-47
"""

handler.dish_justice()

