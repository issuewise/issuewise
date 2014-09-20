from django.db.models import get_model

def get_model_from_settings(model_string):
    try:
       app_label, model_name = model_string.split('.')
    except ValueError:
       raise ImproperlyConfigured("function argument must be of the " 
           "form 'app_label.model_name', got '%s'" % model_string)
    model = get_model(app_label, model_name)
    if model is None:
        raise ImproperlyConfigured("function argument refers to model "
            "'%s' that has not been installed" % model_string)
    return model


    
