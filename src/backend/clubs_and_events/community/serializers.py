from django.utils.translation import gettext as _
from rest_framework import serializers

from community.models import Club, Event, CommunityEvent, Lab, Community
from membership.models import Membership


class OfficialClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = '__all__'
        read_only_fields = ('is_official', 'created_by', 'updated_by')


class UnofficialClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        exclude = ('url_id', 'is_publicly_visible', 'room')
        read_only_fields = ('is_official', 'created_by', 'updated_by')


class ApprovedEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
        read_only_fields = ('is_approved', 'created_by', 'updated_by')


class UnapprovedEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        exclude = ('url_id', 'is_publicly_visible')
        read_only_fields = ('is_approved', 'created_by', 'updated_by')


class ExistingCommunityEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunityEvent
        fields = '__all__'
        read_only_fields = ('is_approved', 'created_under', 'created_by', 'updated_by')


class NotExistingCommunityEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunityEvent
        fields = '__all__'
        read_only_fields = ('is_approved', 'created_by', 'updated_by')

    def validate(self, data):
        base_community = Community.objects.get(pk=data['created_under'].id)
        base_membership = Membership.objects.filter(
            user_id=self.context['request'].user.id, position__in=[1, 2, 3], community_id=base_community.id, status='A'
        )

        if len(base_membership) != 1:
            raise serializers.ValidationError(
                _('Community events are not able to be created under communities you are not a staff.'),
                code='permission_denied'
            )

        try:
            if not Club.objects.get(pk=data['created_under']).is_official:
                raise serializers.ValidationError(
                    _('Community events are not able to be created under unofficial clubs.'),
                    code='unofficial_club_limitations'
                )
        except Club.DoesNotExist:
            pass

        try:
            Event.objects.get(pk=data['created_under'])
            raise serializers.ValidationError(
                _('Community events are not able to be created under events.'),
                code='hierarchy_error'
            )
        except Event.DoesNotExist:
            pass

        return data


class LabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lab
        fields = '__all__'
        read_only_fields = ('created_by', 'updated_by')

    def create(self, validated_data):
        if 'url_id' in validated_data.keys() and validated_data['url_id'].strip() == '':
            validated_data['url_id'] = None
        if 'room' in validated_data.keys() and validated_data['room'].strip() == '':
            validated_data['room'] = None

        return self.Meta.model.objects.create(**validated_data)

    def update(self, instance, validated_data):
        if 'url_id' in validated_data.keys() and validated_data['url_id'].strip() == '':
            validated_data['url_id'] = None
        if 'room' in validated_data.keys() and validated_data['room'].strip() == '':
            validated_data['room'] = None

        instance.__dict__.update(**validated_data)
        instance.save()

        return instance