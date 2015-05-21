from rest_framework.exceptions import PermissionDenied, NotFound
from rest_framework import generics

from core.permissions import permission_factory

# Create your views here.



class PermissionMixin(object):
    """
    this mixin is to be inherited by all the view classes in issuewise.
    this mixin exposes the method authorize(*args) that takes the following 
    arguments:
    
    1. request : a Request object representing the incoming http request. 
    the http method used in the request and the user making the request can 
    be figured out from this. 
    
    2. model
    
    3. view : the view class
    
    4. url_capture : the captured data from the uri
    
    the authorize method calls the correct permission class for the 
    given node using a permission_class(view) method which retuns a
    permission class
    
    methods in the permission class is then called to determine 
    with the same arguments as the authorize function to return 
    
     
    """
    
    
    def permit(self, request, view, model, obj, url_capture):
        permission_class = self.get_permission_class(view)
        return permission_class.is_permitted(request, model, obj, url_capture)
        
    def get_object(self):
        if not self.obj:
            obj = super(PermissionMixin, self).get_object()
        obj = self.obj
        permit = self.permit(self.request, self.__class__.__name__, self.serializer_class.Meta.model, obj, self.kwargs)
        if not permit:
            raise PermissionDenied
        return obj 
        
    def get_queryset(self):
        if not self.qs:
            return self.serializer_class.Meta.model.objects.none()
        qs = self.qs
        exclude = []
        for obj in qs:
            permit = self.permit(self.request, self.__class__.__name__, self.serializer_class.Meta.model, obj, self.kwargs)
            if not permit:
                exclude.append(obj.id)
                
        return qs.exclude(id__in = exclude)
                
            
    def get_permission_class(self,view):
        return permission_factory(view)
        
        


class PostWithPermission(object):

    def post(self, request, format = None, *args, **kwargs):
        permit = self.permit(self.request, self.__class__.__name__,
            self.serializer_class.Meta.model, None, self.kwargs)
        if not permit:
            raise PermissionDenied
        return super(PostWithPermission, self).post(request, format = None, *args, **kwargs)
        
        
class PutWithPermission(object):

    def put(self, request, format = None, *args, **kwargs):
        permit = self.permit(self.request, self.__class__.__name__,
            self.serializer_class.Meta.model, self.get_object(), self.kwargs)
        if not permit:
            raise PermissionDenied
        return super(PutWithPermission, self).put(request, format = None, *args, **kwargs)
        
        
class DeleteWithPermission(object):

    def delete(self, request, format = None, *args, **kwargs):
        permit = self.permit(self.request, self.__class__.__name__,
            self.serializer_class.Meta.model, self.get_object(), self.kwargs)
        if not permit:
            raise PermissionDenied
        return super(DeleteWithPermission, self).delete(request, format = None, *args, **kwargs)        
    
        
        
class WiseListCreateAPIView(PostWithPermission, generics.ListCreateAPIView):

    pass

    
  
        
class WiseRetrieveUpdateDestroyAPIView(PutWithPermission, DeleteWithPermission, generics.RetrieveUpdateDestroyAPIView):

    pass
    

class WiseRetrieveUpdateAPIView(PutWithPermission, generics.RetrieveUpdateAPIView):

    pass
   

    