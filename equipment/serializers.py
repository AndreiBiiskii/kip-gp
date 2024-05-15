from rest_framework import serializers

from equipment.models import GP, Kait, Kip, Contractor, Worker, Approve


class GPSerializer(serializers.ModelSerializer):
    class Meta:
        model = GP
        fields = ['id', 'number', ]



class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = ('__all__')


class ApproveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Approve
        fields = ('__all__')


class KaitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kait
        fields = ('__all__')


class ContractorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contractor
        fields = ('__all__')


class KipSerializerCopy(serializers.ModelSerializer):
    class Meta:
        model = Kip
        fields = ('__all__')


class KipSerializer(serializers.ModelSerializer):
    poz_GP = GPSerializer()

    class Meta:
        model = Kip
        fields = ['id', 'date_at', 'fio_locksmith_1', 'tag', 'poz_GP', 'installation_location', 'type',
                  'name_of_equipment',
                  'serial_number',
                  'description', 'notes']

    def create(self, validated_data):
        validated_data['poz_GP'] = (GP.objects.get(number=validated_data['poz_GP']['number']))
        return Kip.objects.create(**validated_data)

    def update(self, instance, validated_data):
        validated_data['poz_GP'] = (GP.objects.get(number=validated_data['poz_GP']['number']))
        instance = super().update(instance, validated_data)
        instance.save()
        return instance
