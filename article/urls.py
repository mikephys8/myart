from django.conf.urls import patterns, include, url

# from django.contrib import admin
# from article.views import HelloTemplate

# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'article.views.home', name='home'),
    # url(r'^hello/', 'article.views.hello', name='hello'),
    # url(r'^hello_template/', 'article.views.hello_template', name='hello_template'),
    # url(r'^hello_template_simple/', 'article.views.hello_template_simple', name='hello_template_simple'),
    # url(r'^hello_class_view/', HelloTemplate.as_view()),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    url(r'^all/', 'article.views.articles', name='all'),
    # ?P = parameter
    url(r'^get/(?P<article_id>\d+)/', 'article.views.article', name='article'),
    )
