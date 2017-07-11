from rest_framework import BasePermission

class IsUserOrReadOnly(BasePermission):
	def has_object_permission(self, request, view, obj):
		return obj.user == self.request.user