from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from article.models import Article
# from django.template.loader import get_template
# from django.template import Context
from django.views.generic.base import TemplateView
# import templates
# Create your views here.


def home(request):
    # return HttpResponse("Hello World")
    articles = Article.objects.all()
    print(articles)
    return render(request, "article/home.html", {'articles': articles})


def hello(request):
    name = "Mike"
    html = "<html><body><h3>Hi %s, this seems to have worked!</h3></body></html>" % name
    return HttpResponse(html)

def hello_template(request):
    name = "Mike"
    # t = get_template('article/hello.html')
    # html = t.render(Context({'name': name}))
    # return HttpResponse(html)
    return render(request, "article/hello.html", {'name': name})


def hello_template_simple(request):
    name = 'Mike'
    return render_to_response('article/hello.html', {'name': name})


class HelloTemplate(TemplateView):

    template_name = 'article/hello_class.html'

    def get_context_data(self, **kwargs):
        context = super(HelloTemplate, self).get_context_data(**kwargs)
        context['name'] = 'Mike'
        return context


def articles(request):
    return render_to_response('article/articles.html', {'articles': Article.objects.all()})


def article(request, article_id=1):
    return render_to_response('article/article.html', {'article': Article.objects.get(id=article_id)})


