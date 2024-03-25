
from django.urls import path
from .views import edit_document

urlpatterns = [
    # ... other url patterns
    path('document/edit/<int:document_id>/', edit_document, name='edit_document'),
]