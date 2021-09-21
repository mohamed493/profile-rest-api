from rest_framework import permissions 


class UpdateOwnProfile(permissions.BasePermission):
    """" Allow user to edit their own profile """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS :
            print(object.id ,"idddddddddddddddddddddd")
            print(request.user.id ,"idddddddddddddddd222222222222")
            return True 
        print(object.id ,"idddddddddddddddddddddd")
        print(request.user.id,"idddddddddddddddd222222222222")
        return object.id==request.user.id 
