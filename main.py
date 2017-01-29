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

class Index(webapp2.RequestHandler):
    """ Handles requests coming in to '/' (the root of our site)
    """

    def get(self):

        edit_header = "<h3>Signup</h3>"

        # a form for adding new movies
        add_form = """
        <form method="post" action="/signup">
            <label>
                Username
                <input type="text" name="username"/>
            </label><br><br>
            <label>
                Password
                <input type="text" name="password"/>
            </label><br><br>
            <label>
                Verify Password
                <input type="text" name="verify"/>
            </label><br><br>
            <label>
                Email (optional)
                <input type="text" name="email"/>
            </label><br><br>
            <input type="submit" value="Submit"/>
        </form>
        """

        # if we have an error, make a <p> to display it
        error = self.request.get("error")
        error_element = "<p class='error'>" + error + "</p>" if error else ""

        # combine all the pieces to build the content of our response
        main_content = edit_header + add_form + error_element
       # content = page_header + main_content + page_footer
        self.response.write(main_content)

class Signup(webapp2.RequestHandler):
    """ Handles requests coming in to '/signup' 
    """
    
    def post(self):
    #pull submitted information for username -- need to do error handling
    	username = self.request.get("username")
    #pull submitted information for password and verify pwd--need to do error handling
    	password = self.request.get("password")
    #pull submitted information for email -- need to do error handling (email is optional)
    	email = self.request.get("email")
    
    #build signup page	
    	main_content = "<p>Congrats!</p>"
    	
    	self.response.write(main_content)
        

app = webapp2.WSGIApplication([
    ('/', Index),
    ('/signup', Signup)
], debug=True)
