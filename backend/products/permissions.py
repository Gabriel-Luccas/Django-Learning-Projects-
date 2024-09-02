from rest_framework import permissions

class IsStaffEditorPermission(permissions.DjangoModelPermission):
  
  def has_permission(self,request,view):
    user = request.user
    if user.is_staff:
      if user.has_perm("products.add_product"):
        return True
    return False 
  
  def has_obj_permission(self,request,view,obj):
    return obj.owner == request.user
  