from __future__ import unicode_literals
from frappe import _

def get_data():
    return [
      {
        "label":_("Library Management"),
        "icon": "octicon octicon-briefcase",
        "items": [
            {
              "type": "doctype",
              "name": "Articles",
              "onboard":1,
              "description": _("Articles which members issue and return."),
            },
			{
				"type": "doctype",
				"name": "Library Member",
				"onboard": 1,
				"description": _("Library members."),
			},
			{
				"type": "doctype",
				"name": "Library Membership",
				"onboard": 1,
				"description": _("Library memberships."),
			},
			{
				"type": "doctype",
				"name": "Library Transaction",
				"onboard": 1,
				"description": _("Library transactions."),
			},
			{
				"type": "doctype",
				"name": "Library Settings",
				"onboard": 1,
				"description": _("Library Settings."),
			},
          ]
      }
  ]
