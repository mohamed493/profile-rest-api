from rest_framework import permissions 


class UpdateOwnProfile(permissions.BasePermission):
    """" Allow user to edit their own profile """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS :
        #    print(obj.id ,"idddddddddddddddddddddd////////")
       #     print(request.user.id ,"idddddddddddddddd222222222222////////")
            return True 
     #   print(obj ,"opjjjjjjjjjjjjj")
    #    print(request.user.id,"idddddddddddddddd222222222222")
        return obj.id==request.user.id 


class UpdateOwnStatus(permissions.BasePermission):
    """" Allow user to update their own status """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS :
            return True 
        print(obj ,"opjjjjjjjjjjjjj")
        print(request.user.id,"idddddddddddddddd222222222222")
        return obj.user_profile.id==request.user.id 
