# usense
intelligent news recommendation for business decision makers

# About the application

Usense web application presents fresh weekly news to managers about workforce mobility so they can have better decision on this topic without making heavy search process themselves.
The news are presented in 3 different groups (in sub sections) 3 news in each sections. In each section they can see a small fraction of the news. If they get interested, it is possible to read a longer header and finally they can also click and open the whole news in a new browser window.
A free text search also support the quick assessment of the content. This function is available separately for each sub section.
For more advanced users additional services are available after registration with their Google account. Additional services are statistics about top-words, distribution of active users by professional area, feed-back about the service that will be used for later customization.
The news information is collected by a separate service and the result is loaded as a ready-made content to this part of the service. No automation, no interface is developed for feed-in the news.

This code is uploaded and maintained in GitHub and available only for invited contributors.

Overview of the applied technology framework: <br/>
- Enviroment: Google Application Engine <br/>
- Web application: Webapp2 / Paython2 <br/>
- DB: Google Datastore <br/>
- Template handling: Jinja2 <br/>
- Font-end: Bootstrap3, CSS and Javasript <br/>

The structure of the code is briefly described below.

./sd_vote.py server site applcation script written in Python <br/>
./template/ html code of the site, this is a one page design <br/>
./js/ this is the folder of .js code <br/>
./img/ this is the folder of image resources (is it applies) <br/>

User input is sent to server storage with ajax function with help of http post transaction.

Sample application is available here: http://www.usense.biz/


Development server

- First check the python version on your local machine
- After checking the python version if version is not found then install python2.7 on your local machine and check python version
- Next download the google-cloud-sdk zip file from https://cloud.google.com/appengine/docs/standard/python/tools/using-local-server
- Extract the google-cloud-sdk zip file and save in any directory
- open the terminal and enter the directory where you save google-cloud-sdk folder and run the following command ./google-cloud-sdk/install.sh
- when this command execute run the following command ./google-cloud-sdk/bin/gcloud init
- Run pip install -t lib -r requirements.txt
- After go to your project folder and open the terminal and Running the local development server using following command: dev_appserver.py app.yaml  
- When you run this command after enter the http://localhost:8080/ in your browser. Note (if you are use already a terminal then first stop this terminal) 

Code Development
- To create a new page, first create a new view class by inerting from webapphandler class, secondly create a jinja template in templates directory and then assign that template in newly create view class by setting variable template_name by the name of jinja tempalte. 
- To make a page login required set the view class variable login_required to True. By default it's False.
- To append an extra data in context (send new data to template) override the function get_template_values in view class.
- To make style (CSS) changes write css rules in style.css
- Execute a code at the time of google engine app launch, write code in appengine_config.py

