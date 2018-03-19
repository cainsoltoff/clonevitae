from rest_framework import generics
from django.http import HttpResponse
import json

from . import models

from django.core import serializers

def get_entries_for_gene(request):

    q = request.GET.get('gene', '')
    genes = models.Variant.objects.filter(gene=q)

    data = serializers.serialize('json', genes, fields = ('gene',
                                                        'nucleotide_change',
                                                        'protein_change',
                                                        'alias',
                                                        'region',
                                                        'reported_classification',
                                                        'last_evaluated',
                                                        'last_updated',
                                                        'url',
                                                        'source'))

    return HttpResponse(data, 'application/json')

def get_autocomplete_options(request):
    #TODO: Once up and running, if autocomplete too slow, implement a Trie on the list of unique gene names for fast prefix lookup

    q = request.GET.get('term', '')
    genes = models.Variant.objects.filter(gene__istartswith=q)

    results = []
    geneSet = set()
    for g in genes:
        geneSet.add(g.gene)

    for (counter, g) in enumerate(geneSet):
        gene_json = {}
        gene_json['label'] = g
        gene_json['value'] = g

        results.append(gene_json)

    data = json.dumps(results)

    return HttpResponse(data, 'application/json')