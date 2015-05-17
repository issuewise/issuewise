"""
Django expects to find an app's concrete models inside the 
models.py file under the app.

This app's models are in multiple files inside a models
package instead of a single models.py file. This requires
some special treatment. 

Whenever you add new concrete models to this app, you need to

1. Import it here

2. Add your model class to __all__  

If you miss this step, Django might not recognize your models and
may issue inadequate sql statements leading to unexpected errors. 
"""

from accounts.models.wiseusers import (WiseUser, WiseFriendship, WiseActivation)

__all__ = ['WiseUser',  
           'WiseFriendship',
           'WiseActivation',] 