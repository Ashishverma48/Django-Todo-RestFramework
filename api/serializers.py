from rest_framework import serializers

#import Todo Model Here for create serializer 
from api.models import Todo

class TodoSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Todo   # create serializer for Todo Model
        fields =['title','description','completed']     # for all fields
