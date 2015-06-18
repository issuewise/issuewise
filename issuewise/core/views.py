from rest_framework.exceptions import PermissionDenied, NotFound
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from core.permissions import permission_factory

# Create your views here.

class Welcome(APIView):

    def get(self, request, *args, **kwargs):
        data = {"name": "issuewise", "version": 0.1} 
        return Response(data = data)
    

    

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
    
    any detail view class that inherits this mixin must define an attribute self.error_dict
    
    any class that inherits this must define a get_owner() method
    
     
    """
    
    def permit(self, request, view, obj, owner):
        permission_class = self.get_permission_class(view)
        return permission_class.is_permitted(request, obj, owner)
        
    def get_request_type(self, request, view, obj, owner):
        permission_class = self.get_permission_class(view)
        return permission_class.request_type(request, obj, owner)
        
    def get_object(self):
        if not self.obj:
            obj = super(PermissionMixin, self).get_object()
        obj = self.obj
        permit = self.permit(request = self.request, view = self.__class__.__name__, 
            obj = obj, owner = self.owner)
        if not permit:
            error_key = self.get_request_type(request = self.request, view = self.__class__.__name__, 
                obj = obj, owner = self.owner)
            raise PermissionDenied(detail = self.error_dict[error_key])
        return obj 
        
    def get_queryset(self):
        if not self.qs:
            return self.serializer_class.Meta.model.objects.none()
        qs = self.qs
        exclude = []
        for obj in qs:
            permit = self.permit(request = self.request, view = self.__class__.__name__, 
            obj = obj, owner = self.owner)
            if not permit:
                exclude.append(obj.id)
                
        return qs.exclude(id__in = exclude)
                
            
    def get_permission_class(self,view):
        return permission_factory(view)
        
        


class PostWithPermission(object):
    '''
    any class that inherits this must define an attribute self.error_dict
    and a method get_owner() that returns the owner of the resource 
    '''

    def post(self, request, format = None, *args, **kwargs):
        permit = self.permit(request = self.request, view = self.__class__.__name__, 
            obj = None, owner = self.owner)
        if not permit:
            error_key = self.get_request_type(request = self.request, view = self.__class__.__name__, 
            obj = None, owner = self.owner)
            raise PermissionDenied(detail = self.error_dict[error_key])
        return super(PostWithPermission, self).post(request, format = None, *args, **kwargs)
        
        
class PutWithPermission(object):
    '''
    any class that inherits this must define an attribute self.error_dict
    and a method get_owner() that returns the owner of the resource 
    '''

    def put(self, request, format = None, *args, **kwargs):
        permit = self.permit(request = self.request, view = self.__class__.__name__, 
            obj = self.get_object(), owner = self.owner)
        if not permit:
            error_key = self.get_request_type(request = self.request, view = self.__class__.__name__, 
            obj = self.get_object(), owner = self.owner)
            raise PermissionDenied(detail = self.error_dict[error_key])
        return super(PutWithPermission, self).put(request, format = None, *args, **kwargs)
        
        
class DeleteWithPermission(object):
    '''
    any class that inherits this must define an attribute self.error_dict
    and a method get_owner() that returns the owner of the resource 
    '''
    def delete(self, request, format = None, *args, **kwargs):
        permit = self.permit(request = self.request, view = self.__class__.__name__, 
            obj = self.get_object(), owner = self.owner)
        if not permit:
            error_key = self.get_request_type(request = self.request, view = self.__class__.__name__, 
            obj = self.get_object(), owner = self.owner)
            raise PermissionDenied(detail = self.error_dict[error_key])
        return super(DeleteWithPermission, self).delete(request, format = None, *args, **kwargs)        
    
        
        
class WiseListCreateAPIView(PostWithPermission, generics.ListCreateAPIView):

    pass

    
  
        
class WiseRetrieveUpdateDestroyAPIView(PutWithPermission, DeleteWithPermission, generics.RetrieveUpdateDestroyAPIView):

    pass
    

class WiseRetrieveUpdateAPIView(PutWithPermission, generics.RetrieveUpdateAPIView):

    pass
   

    