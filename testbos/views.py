from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from cerbos_client import cerbos_client
from django.http import HttpResponseForbidden
from .utils import extract_roles_from_jwt
from cerbos.sdk.grpc.client import CerbosClient
from cerbos.engine.v1 import engine_pb2
from google.protobuf.struct_pb2 import Value


@login_required  # Ensure only authenticated users can access this view
def edit_document(request, document_id):
    user_roles = extract_roles_from_jwt(request)
    user = request.user
    
    principal = engine_pb2.Principal(
        id=user.username,
        roles=user_roles,
        attr={},
    )

    resource = engine_pb2.Resource(
        id=document_id,
        kind="document",
        attr={
            "owner": Value(string_value=user.username),
            # Add other relevant resource attributes here
        },
    )
    
    # Instantiate your Cerbos client and perform the authorization check
    with CerbosClient(cerbos_client) as c:
        if not c.is_allowed("edit", principal, resource):
            return HttpResponseForbidden("Not authorized to edit this document.")
    
    # Proceed with your document editing logic
        pass