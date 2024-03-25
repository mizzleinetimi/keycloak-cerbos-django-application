from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from cerbos_client import cerbos_client

@login_required  # Ensure only authenticated users can access this view
def edit_document(request, document_id):
    # Retrieve user information from the request object (populated by django-allauth)
    user = request.user

    # Extract roles from user attributes (assuming roles are mapped to attributes in the JWT)
    # This is just an example, adjust it according to how your user's roles are stored.
    user_roles = user.attributes.get('roles', [])  # Replace 'roles' with the actual attribute name

    # Print the user's username and roles for testing purposes
    print(f"User: {user.username}, Roles: {user_roles}")

    # Check permission using Cerbos client
    if not cerbos_client.is_allowed("edit", "document", user.username, {"id": document_id, "roles": user_roles}):
        return HttpResponseForbidden("Not authorized to edit this document.")

    # If authorized, proceed with editing logic
    # ... (your document editing logic)
    
    # ... (return appropriate response after editing)