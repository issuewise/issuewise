"""
This app's models are in multiple files inside a models
package instead of a single models.py file. This requires
some special treatment. 

Whenever you add new concrete models to this app, you need to

1. Import it here

2. Add your model class to __all__  

Please do this, otherwise Django will be confused when loading models,
might make errors in the schema declarations and even throw
unexpected errors! 
"""

from wiselocations import WiseLocation

__all__ = ['WiseLocation']
