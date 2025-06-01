from rest_framework import serializers
from .models import Held, Attribut, Talent, Ausruestung


class AttributSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribut
        fields = ['id', 'name', 'wert']


class TalentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Talent
        fields = ['id', 'name', 'wert']


class AusruestungSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ausruestung
        fields = ['id', 'name', 'typ']


class HeldSerializer(serializers.ModelSerializer):
    attribute = AttributSerializer(many=True, required=False)
    talente = TalentSerializer(many=True, required=False)
    ausruestung = AusruestungSerializer(many=True, required=False)

    class Meta:
        model = Held
        fields = ['id', 'name', 'rasse', 'kultur', 'profession',
                  'lebenspunkte', 'ausdauer', 'attribute', 'talente', 'ausruestung']
        read_only_fields = ['user']

    def create(self, validated_data):
        attr_data = validated_data.pop('attribute', [])
        talent_data = validated_data.pop('talente', [])
        ausruestung_data = validated_data.pop('ausruestung', [])
        validated_data.pop('user', None)

        held = Held.objects.create(user=self.context['request'].user, **validated_data)

        for attr in attr_data:
            Attribut.objects.create(held=held, **attr)
        for talent in talent_data:
            Talent.objects.create(held=held, **talent)
        for ausr in ausruestung_data:
            Ausruestung.objects.create(held=held, **ausr)

        return held
