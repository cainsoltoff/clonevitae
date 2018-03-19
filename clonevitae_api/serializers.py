from rest_framework import serializers
from . import models


class VariantSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'gene',
            'nucleotide_change',
            'protein_change',
            #'other_mappings',
            'alias',
            #'transcripts',
            'region',
            'reported_classification',
            #'inferred_classification',
            'source',
            'last_evaluated',
            'last_updated',
            'url',
            #'submitter_comment',
            #'assembly',
            #'chromosome',
            #'genomic_start',
            #'genomic_stop',
            #'ref',
            #'alt',
            #'accession',
            #'reported_ref',
            #'reported_alt',
        )
        model = models.Variant

