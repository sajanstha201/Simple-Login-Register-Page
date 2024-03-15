In this I have made the login and register page using django which will interact with the database for authentication.



I have use simple API for login and register.

Register API will directly insert the data given by the user to the database without using any serializer or any other medium that will help to consider that the given data is valid or not. 

Login API will retrive the data and check whether the data is present in the auth_user table (which is inbuild table in the django).
Now, authentication is done using AuthenticationForm which will directly authenticate the given data to API (username and password) and if it is in the database then it will return with appropriate message.
