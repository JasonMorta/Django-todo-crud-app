from django.db import models

# Create your models here.
from django.db import models

# models.Model is the base class for all models
# Model automatically creates an id field as the primary key unless explicitly specified.
# The key is an auto-incrementing integer field called id.
class Todo(models.Model):
    title = models.CharField(max_length=50) # create a character field with a max length of 50
    description = models.TextField() # create a text field
    created_at = models.DateTimeField(auto_now_add=True) # add a date and time field to the model
    

    def __str__(self):
        return self.title # instead of 'Todo object (1)', the title will be displayed
