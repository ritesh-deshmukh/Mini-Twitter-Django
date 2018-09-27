from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView
from .models import Tweet
# Create Retrieve Update Delete => CRUD
# List/Search
# class based views(whole class)/ function based views(writing a function)


# function views
# Retrieve View

# class based views
class TweetDetailView(DetailView):
    # template_name = "tweets/detail_view.html"
    queryset = Tweet.objects.all()

    # def get_object(self):
    #     print(self.kwargs)
    #     pk = self.kwargs.get("pk")
    #     # print(pk)
    #     return Tweet.objects.get(id=pk)


class TweetListView(ListView):
    # template_name = "tweets/list_view.html"
    queryset = Tweet.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(TweetListView, self).get_context_data(*args, **kwargs)
        return context

# def tweet_detail_view(request, id=1):
#     obj = Tweet.objects.get(id=id) # Get data from Db
#     print(obj)
#     context = {
#         "object": obj
#     }
#     return render(request, "tweets/detail_view.html", context)


# def tweet_list_view(request):
#     queryset = Tweet.objects.all()
#     for obj in queryset:
#         print(obj.content)
#     # print(queryset)
#     context = {
#         "object_list": queryset
#     }
#     return render(request, "tweets/list_view.html", context)
