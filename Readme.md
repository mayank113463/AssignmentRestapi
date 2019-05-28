-----------------ProJect Setup--------------------

1-->I make this project on Django framework so for install django i have created a virtual Environment and install required library  using command pip install Django==2.2.1

2--> I created app name as employees using pip install startapp employees which is having Model name is Employee which has field -->

First Name
Last Name
Company Name
Age
City
State
Zip
Email
Web


3-->add this employees app in settings.py and in installed app

4-->run command makemigrations and migrate for create table into database which is sqlite3 i am using here.


5-->after that i installed 3rd party app rest_framework using pip commmand
and craete a file name with  serializers.py and create a modelserilzer for

-----CRUD operation----------

pip install djangorestframework
pip install markdown       # Markdown support for the browsable API.
pip install django-filter  # Filtering support


6-->in settings.py -->installed app. add rest_framework.[settings.py]

7--> in settings.py REST_FRAMEWORK -->add default pagination class ,per page data,and search param..etc added


8-->now time to views.py serialize data .there i inherited viewsets.ModelViewSet and serialize using serializer_class



9-->now come to urls.py i did routing using routers.DefaultRouter() and register router with views with EmployeeViewSet ..and give url for api-->


localhost:8000/api/users/


10-->for pagination i have created pagination.py in employees app and inherit class PageNumberPagination and give it page_size adn page_query_param for limit
per page data and import this class into views.py as pagination_class and add in class EmployeeViewSet


11-->I test it using browsable api and postman both.



Thanks! i did my best but if you give any suggestion or modification and question than  please revert me back .
