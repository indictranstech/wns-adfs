from __future__ import unicode_literals
import frappe
from urlparse import urlparse
from onelogin.saml2.auth import OneLogin_Saml2_Auth
from onelogin.saml2.utils import OneLogin_Saml2_Utils
import os
import webbrowser
import requests
import urllib2


@frappe.whitelist(allow_guest=True)
def init_adfs_request():
    req = prepare_frappe_request()
    auth = init_saml_auth(req)
    errors = []
    sso_built_url = auth.login()
    print "sso_build_url_____________", sso_built_url
    print "request_id _____",auth.get_last_request_id()
    return sso_built_url
    # webbrowser.open(sso_built_url)
    # response = requests.get(sso_built_url)
    # frappe.local.response["type"] = "redirect"
    # frappe.local.response["location"] = sso_built_url
    # return


def init_saml_auth(req):
    path = os.path.join(os.path.dirname(__file__), "..", "config/saml")
    auth = OneLogin_Saml2_Auth(req, custom_base_path=path)
    return auth

@frappe.whitelist(allow_guest=True)
def prepare_frappe_request():
    # If server is behind proxys or balancers use the HTTP_X_FORWARDED fields
    url_data = urlparse(frappe.local.request.host_url)
    request = frappe.local.request
    print dir(frappe.local.request), "local request_________"
    print frappe.local.request.host, "host ____"
    print frappe.local.request.host_url, "host url_________________"
    print frappe.local.request.path, "path ______________"
    print frappe.local.request.query_string, "query string _________________"
    print frappe.local.request.scheme, "https scheme ___________________"
    print frappe.local.request.args, "args data__________"
    print frappe.local.request.form, "form data __________"
    print frappe.local.form_dict, "form dict data___________"
    print frappe.local.request.url, "url __________________________"
    print url_data, "url_Data parsedddddd_______"
    print frappe.local.request.is_secure, "issecure____________"
    data = {
        'https': 'on' if request.scheme == 'https' else 'off',
        'http_host': request.host,
        'script_name':request.path,
        'server_port': 9002,
        'get_data': request.args.copy(),
        'post_data': request.form.copy(),
        'lowercase_urlencoding': True,
        'query_string': request.query_string
    }
    return data

@frappe.whitelist(allow_guest=True)
def init_acs_endpoint():
    print "adfs auth login___________3432424242424324234244"
    return {"assertion consumer service" : "sucess"}

def init_sls():
    print "single log out_____"
    pass

@frappe.whitelist(allow_guest=True)
def init_saml_endpoint():
    print "saml endpoint"
    return  {"saml":"sucessss"}