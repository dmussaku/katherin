'''
New structure for api
Now we have a django app, called api_v1 which is the first
version of the api. It has its own directories (python modules)
which in turn have their own structure:
api_v1/:
--auth/
----api.py # contains views and viewsets
----router.py # register url patterns
----serializers.py # contains serializator objects
----tests.py # contains tests
--blog/
--core/
'''
