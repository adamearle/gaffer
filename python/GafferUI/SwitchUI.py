##########################################################################
#
#  Copyright (c) 2015, Image Engine Design Inc. All rights reserved.
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are
#  met:
#
#      * Redistributions of source code must retain the above
#        copyright notice, this list of conditions and the following
#        disclaimer.
#
#      * Redistributions in binary form must reproduce the above
#        copyright notice, this list of conditions and the following
#        disclaimer in the documentation and/or other materials provided with
#        the distribution.
#
#      * Neither the name of John Haddon nor the names of
#        any other contributors to this software may be used to endorse or
#        promote products derived from this software without specific prior
#        written permission.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
#  IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
#  THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
#  PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
#  CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
#  EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
#  PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
#  PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
#  LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
#  NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#  SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
##########################################################################

import Gaffer

for nodeType in ( Gaffer.SwitchDependencyNode, Gaffer.SwitchComputeNode ) :

	Gaffer.Metadata.registerNode(

		nodeType,

		"description",
		"""
		Chooses between multiple input connections, passing through the
		chosen input to the output.
		""",

		# Add + buttons for creating new plugs in the NodeGraph
		"noduleLayout:customGadget:addButtonTop:gadgetType", "GafferUI.SwitchUI.PlugAdder",
		"noduleLayout:customGadget:addButtonTop:section", "top",
		"noduleLayout:customGadget:addButtonBottom:gadgetType", "GafferUI.SwitchUI.PlugAdder",
		"noduleLayout:customGadget:addButtonBottom:section", "bottom",
		"noduleLayout:customGadget:addButtonLeft:gadgetType", "GafferUI.SwitchUI.PlugAdder",
		"noduleLayout:customGadget:addButtonLeft:section", "left",
		"noduleLayout:customGadget:addButtonRight:gadgetType", "GafferUI.SwitchUI.PlugAdder",
		"noduleLayout:customGadget:addButtonRight:section", "right",

		plugs = {

			"index" : [

				"description",
				"""
				The index of the input which is passed through. A value
				of 0 chooses the first input, 1 the second and so on. Values
				larger than the number of available inputs wrap back around to
				the beginning.
				""",

				"nodule:type", "",

			],

			"in" : [

				"description",
				"""
				The array of inputs to choose from. One of these is chosen
				by the index plug to be passed through to the output.
				""",

				"nodule:type", "GafferUI::CompoundNodule",
				"plugValueWidget:type", "",

			],

			"out" : [

				"description",
				"""
				Outputs the input specified by the index.
				""",

				"plugValueWidget:type", "",

			],

		}

	)
