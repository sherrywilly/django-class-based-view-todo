from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView,UpdateView,DeleteView,View
from .models import Todo
from .forms import TodoForm
from django.urls import reverse_lazy


# Create your views here.

# we can also write all actions of a model in one  class using View
# what is view
# The master class-based base view. All other class-based views inherit from this base class.


# class TodoViews(View):
#     model = Todo
#     def get(self,request,*args,**kwargs):
#         pass
#     def post(self,request,*args,**kwargs):
#         pass
#     def put(self,request,*args,**kwargs):
#         pass
#     def delete(self,request,*args,**kwargs):
#         pass


# defined the list view 
# A page representing a list of objects.
class Home(ListView):
    model = Todo
    template_name = "index.html"
    context_object_name = 'todos'
    form = TodoForm

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form
        return context

    def post(self,request,*args,**kwargs):
        item = request.POST.get('item')
        form = Todo()
        form.item = item
        form.save()
        return redirect('home')



# While this view is executing, self.object will contain the object that the view is operating upon.
# detailed view of an object
class Tododetail(DetailView):
    model = Todo
    template_name = "details.html"
    context_object_name = 'todo'

# A view that displays a form for editing an existing object,
#  redisplaying the form with validation errors (if there are any) and saving changes to the object. 
# This uses a form automatically generated from the object’s model class (unless a form class is manually 
# specified).
class Todoupdate(UpdateView):
    model=Todo
    template_name = "update.html"
    form_class = TodoForm
    success_url = reverse_lazy('home')


# A view that displays a confirmation page and deletes an existing object. 
# The given object will only be deleted if the request method is POST. If this view is fetched via GET,
#  it will display a confirmation page that should contain a form that POSTs to the same URL.

class Tododelete(DeleteView):
    model = Todo
    template_name = 'confirm.html'
    context_object_name = 'data'
    success_url =  reverse_lazy('home')