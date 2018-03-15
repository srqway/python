from django.contrib.auth.models import User, Group
from rest_framework import serializers

from my_app_0.models import Basic


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Group
        fields = ('url', 'name')


class BasicSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    big_integer_field = serializers.IntegerField()
    boolean_field = serializers.BooleanField()
    char_field = serializers.CharField()
    choice_field = serializers.ChoiceField(choices=Basic.MY_CHOICE)
    date_field = serializers.DateField()
    date_time_field = serializers.DateTimeField()
    decimal_field = serializers.DecimalField(max_digits=5, decimal_places=2)
    duration_field = serializers.DurationField()
    email_field = serializers.EmailField()
    file_field = serializers.FileField()
    file_path_field = serializers.FilePathField(path="/tmp/file_path_field")
    float_field = serializers.FloatField()
    image_field = serializers.ImageField()
    integer_field = serializers.IntegerField()
    generic_ip_address_field = serializers.IPAddressField()
    null_boolean_field = serializers.NullBooleanField()
    positive_integer_field = serializers.IntegerField()
    positive_small_integer_field = serializers.IntegerField()
    slug_field = serializers.SlugField()
    small_integer_field = serializers.IntegerField()
    text_field = serializers.CharField()
    time_field = serializers.TimeField()
    url_field = serializers.URLField()
    uuid_field = serializers.UUIDField()

    def create(self, validated_data):
        return Basic.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.big_integer_field = validated_data.get('big_integer_field', instance.big_integer_field)
        instance.boolean_field = validated_data.get('boolean_field', instance.boolean_field)
        instance.char_field = validated_data.get('char_field', instance.char_field)
        instance.choice_field = validated_data.get('choice_field', instance.choice_field)
        instance.date_field = validated_data.get('date_field', instance.date_field)
        instance.date_time_field = validated_data.get('date_time_field', instance.date_time_field)
        instance.decimal_field = validated_data.get('decimal_field', instance.decimal_field)
        instance.duration_field = validated_data.get('duration_field', instance.duration_field)
        instance.email_field = validated_data.get('email_field', instance.email_field)
        instance.file_field = validated_data.get('file_field', instance.file_field)
        instance.file_path_field = validated_data.get('file_path_field', instance.file_path_field)
        instance.float_field = validated_data.get('float_field', instance.float_field)
        instance.image_field = validated_data.get('image_field', instance.image_field)
        instance.integer_field = validated_data.get('integer_field', instance.integer_field)
        instance.generic_ip_address_field = validated_data.get('generic_ip_address_field', instance.generic_ip_address_field)
        instance.null_boolean_field = validated_data.get('null_boolean_field', instance.null_boolean_field)
        instance.positive_integer_field = validated_data.get('positive_integer_field', instance.positive_integer_field)
        instance.positive_small_integer_field = validated_data.get('positive_small_integer_field', instance.positive_small_integer_field)
        instance.slug_field = validated_data.get('slug_field', instance.slug_field)
        instance.small_integer_field = validated_data.get('small_integer_field', instance.small_integer_field)
        instance.text_field = validated_data.get('text_field', instance.text_field)
        instance.time_field = validated_data.get('time_field', instance.time_field)
        instance.url_field = validated_data.get('url_field', instance.url_field)
        instance.uuid_field = validated_data.get('uuid_field', instance.uuid_field)
        instance.save()
        return instance
    
