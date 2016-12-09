# drf-ignore-slash-middleware
Django middleware that makes urls ending with and without slashes equivalent


When using [DRF](https://www.django-rest-framework.org) routers you have a choice to either have urls end with trailing slash (default) or not. 
i.e `DefaultRouter(trailing_slash=False)`. You can't however have it both ways, as in ignore them.

This package defines a very simple middleware class that removes trailing slashes from urls if they have one.
So in order to ignore trailing slashes and have `/api/some_url` be equivalent to `/api/some_url/` simply install the package and add the middleware class as the first entry in the MIDDLEWARE list. Please note that middleware [changed in django 1.10](https://docs.djangoproject.com/en/1.10/topics/http/middleware/) and this this pacakge requires django version >= 1.10.

```python
MIDDLEWARE = [
	# Should be first entry
	'drf_ignore_slash_middleware.SlashIgnoreMiddleware',
	# Rest of your middleware
]
```
