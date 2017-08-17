from rest_framework import serializers
from unologbase.models import Patient
from string import capwords
import datetime



class PatientSerializer(serializers.ModelSerializer):
	"""
	Serializer of patient model
	"""
	class Meta:

		model = Patient
		fields =('pk','name', 'firstname', 'birthdate', 'street')

	def validate_birthdate(self, value):
		"""
		check birthdate not in future
		"""
		if value > datetime.date.today():
			raise serializers.ValidationError("patient can't be born in future Mr Conor")

		return value

	# def create(self, validated_data):
	# 	"""
	# 	custom create for PatientSerializer
	# 	"""

	# 	#automatique capwords name and firstanme
	# 	validated_data['name'] = capwords(validated_data['name'])
	# 	validated_data['firstname'] = capwords(validated_data['firstname'])
		


	# 	patient = Patient.objects.create(**validated_data)
	# 	return patient



