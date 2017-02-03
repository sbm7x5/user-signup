#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import re

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASSWORD_RE = re.compile(r"^.{3,20}$")
EMAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")

def valid_username(username):
    return USER_RE.match(username)

def valid_password(password):
    return PASSWORD_RE.match(password)

def valid_email(email):
    return EMAIL_RE.match(email)


edit_header = "<h3>Signup</h3>"

add_form = """
<form method="post" action="/welcome">
    <label>
        Username
        <input type="text" name="username" value="%(username)s"/>
        <span>%(username_error)s</span>
        %(uvalid_error)s
    </label><br><br>
    <label>
        Password
        <input type="text" name="password"/>
        %(password_error)s
    </label><br><br>
    <label>
        Verify Password
        <input type="text" name="verify"/>
        %(pvalid_error)s
    </label><br><br>
    <label>
        Email (optional)
        <input type="text" name="email" value="%(email)s"/>
        %(email_error)s
    </label><br><br>
    <input type="submit" value="Submit"/>
</form>"""


class Index(webapp2.RequestHandler):
    """ Handles requests coming in to '/' (the root of our site)
    """
    def write_form(self, username="", email="", username_error="", password_error="", pvalid_error="", email_error="", uvalid_error=""):
        self.response.write(edit_header + add_form % {
            'username': username,
            'email':email,
            'username_error': username_error,
            'password_error':password_error,
            'email_error':email_error,
            'pvalid_error':pvalid_error,
            'uvalid_error':uvalid_error})

    def get(self):
        # if we have an error, make a <p> to display it
        # error = self.request.get("error")
        # error_element = '<p style="color:red;">' + error + '</p>' if error else ""
        # combine all the pieces to build the content of our response
        # main_content = edit_header + add_form + error_element
        # self.response.write(main_content)
        self.write_form()

    def post(self):
        #pull submitted information for username -- need to do error handling
        error = False
        username = self.request.get("username")
        password = self.request.get("password")
        verify = self.request.get("verify")
        email = self.request.get("email")
        username_error = ""
        uvalid_error = ""
        password_error = ""
        pvalid_error = ""
        email_error = ""

    #The user does not enter a username
        if not username:
            error = True
            username_error = "You must enter a username"
    #The user's username is not valid -- for example, contains a space character.
        if valid_username(username) == None:
            error = True
            uvalid_error = "Your username is not valid"
    # The user's password and password-confirmation do not match
        if valid_password(password) == None:
            error = True
            password_error = "Your password is not valid"
        if password != verify:
            error = True
            pvalid_error = "Your passwords do not match"
    #The user provides an email, but it's not a valid email.
        if email != '' and valid_email(email) == None:
            error = True
            email_error = "Your email is not valid"

        if error == True:
            self.write_form(username, email, username_error,
            password_error, pvalid_error, email_error, uvalid_error)

        else:
            self.redirect("/welcome?username=%s"%username)


class Welcome(Index):
    """ Handles requests coming in to '/Welcome'
    """

    def get(self):
        username = self.request.get("username")
        self.response.write("<h1> Welcome, %s!</h1>"%(username))

app = webapp2.WSGIApplication([
    ('/', Index),
    ('/welcome', Welcome)
], debug=True)
