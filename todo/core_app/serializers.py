from rest_framework import serializers


from core_app.models import CheckList, CheckListItem

class CheckListItemSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = CheckListItem
        fields = '__all__'


class CheckListSerializer(serializers.ModelSerializer):
    items = CheckListItemSerializer(source='checklistitem_set',many=True, read_only=True,)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = CheckList
        fields = '__all__'
        # fields = ['title','is_deleted','is_archived','created_on']

# class CheckListSerializer(serializers.Serializer):
#     title = serializers.CharField()
#     is_deleted = serializers.BooleanField()
#     is_archived = serializers.BooleanField()
#     created_on = serializers.DateField()
#     updated_on = serializers.DateField()