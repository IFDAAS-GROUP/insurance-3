from django.contrib.auth.models import User, Group
from polling.models import *
from rest_framework import serializers



#1
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

#2
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
#3
class ContactLoggingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =  ContactLogging
        fields = ('contact','start_datetime','end_datetime','measurement','interval','lastupdate')

#4
class HospitalSubjectDeviceRegistrationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HospitalSubjectDeviceRegistration
        fields = ('hospital_name_id','subject_detail','subject_insurance_policy_detail','medical_history_brief','device_details','lastupdate')
#5
class HospitalSubjectRegistrationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HospitalSubjectRegistration
        fields = ('hospital_detail','api_public_key','api_private_key','api_consumer_key','api_token_key','isactive','isverified','lastupdate','lastupdate')

#6        #InsuraceOfficeRegistration
class InsuraceOfficeRegistrationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InsuraceOfficeRegistration
        fields = ('insurance_office','api_private_key','api_public_key','api_consumer_key','api_token_key','lastupdate')

#7        #InsurancePremiumModelling
class InsurancePremiumModellingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InsurancePremiumModelling
        fields = ('hospital_id','subject_id','insurance_policy_id','projected_premium','lastupdate')


#8
class InsuranceplancategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Insuranceplancategory
        fields = ('insuranceplancategoryname','insuranceplancategorydocumention','lastupdate')
