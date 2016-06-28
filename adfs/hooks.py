# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "adfs"
app_title = "ADFS"
app_publisher = "suyash.p@indictranstech.com"
app_description = "ADFS Integration with SAML"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "suyash.p@indictranstech.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/adfs/css/adfs.css"
# app_include_js = "/assets/adfs/js/adfs.js"

# include js, css files in header of web template
# web_include_css = "/assets/adfs/css/adfs.css"
# web_include_js = "/assets/adfs/js/adfs.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "adfs.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "adfs.install.before_install"
# after_install = "adfs.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "adfs.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"adfs.tasks.all"
# 	],
# 	"daily": [
# 		"adfs.tasks.daily"
# 	],
# 	"hourly": [
# 		"adfs.tasks.hourly"
# 	],
# 	"weekly": [
# 		"adfs.tasks.weekly"
# 	]
# 	"monthly": [
# 		"adfs.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "adfs.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "adfs.event.get_events"
# }

