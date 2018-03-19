from django.test import TestCase
from django.urls import reverse
from .models import Variant
import datetime

import json
from urllib.request import urlopen
# Create your tests here.

from helper import load_variant_db

class ClonevitaeTestVariantModel(TestCase):

    def setUp(self):
        Variant.objects.create(gene="TESTGENE",
                               nucleotide_change = "NM_007299.3:c.2021-1465_2021-1461delTGTGGinsAGTGA",
                               protein_change = "p.Cys1787_Gly1788delinsSerAsp",
                               other_mappings = "abcdefg",
                               alias= "p.D1778G:GAT>GGT",
                               transcripts= "abcdefghij",
                               region= "U14680.1:exon 23",
                               reported_classification="Likely benign",
                               inferred_classification="Likely benign",
                               source = "Clinvar",
                               last_evaluated = datetime.date(2015, 6, 30),
                               last_updated = datetime.date(2017, 12, 31),
                               url = "https://www.ncbi.nlm.nih.gov/clinvar/RCV000048949/",
                               submitter_comment = "this is a comment",
                               assembly = "abcdefg",
                               chromosome = "12",
                               genomic_start = "123431a",
                               genomic_stop = "12343b",
                               ref = "aasdg;asfd",
                               alt = "asdgasdg",
                               accession = "asdgasdg",
                               reported_ref = "asdgasdg",
                               reported_alt = "asdgasdg")

    def testNewVariantCreation(TestCase):
        testVariant = Variant.objects.get(gene="TESTGENE")
        TestCase.assertEqual(testVariant.accession, "asdgasdg")

    def cleanUp(self):
        testVariant = Variant.objects.get(gene="TESTGENE")
        testVariant.delete()

class ClonevitaeTestAPI(TestCase):

    @classmethod
    def setUpClass(cls):
        super(ClonevitaeTestAPI, cls).setUpClass()
        load_variant_db()

    def test_autocomplete_api_status_codes(self):
        kwargs = {'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'}
        url = reverse('get_autcomplete')
        get_data = {'term': 'BR'}
        autocomplete_response = self.client.get(url, get_data, **kwargs)
        self.assertEqual(autocomplete_response.status_code, 200)

    def test_get_entries_for_gene_api_status_codes(self):
        kwargs = {'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'}
        url = reverse('get_entries_for_gene')
        get_data = {'term': 'BRCA2'}
        gene_entries_response = self.client.get(url, get_data, **kwargs)
        self.assertEqual(gene_entries_response.status_code, 200)

    def test_api_autofill_options(self):
        kwargs = {'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'}
        url = reverse('get_autcomplete')
        get_data = {'term': 'BR'}
        autocomplete_response = self.client.get(url, get_data, **kwargs)
        data = json.loads(autocomplete_response.content)

        autocomplete_prefix_check = [x['value'].startswith('BR') for x in data]
        self.assertEqual(all(autocomplete_prefix_check), True)

    def test_api_get_gene_options(self):
        kwargs = {'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'}
        url = reverse('get_entries_for_gene')
        get_data = {'gene': 'BRCA2'}
        gene_entries_response = self.client.get(url, get_data, **kwargs)
        data = json.loads(gene_entries_response.content)
        get_gene__entires_check = {x['fields']['gene']== 'BRCA2' for x in data}

        self.assertEqual(all(get_gene__entires_check), True)

        self.assertEqual(len(data), 1545) # this is probably not a good test because
        # of the hardcoded len check if you use a different test DB or DB
        # probably better to set up tests that read the CSV file raw and check the DB
        # against that

    def test_api_get_gene_options_null(self):
        kwargs = {'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'}
        url = reverse('get_entries_for_gene')
        get_data = {'gene': 'ABC123QQQQ'}
        gene_entries_response = self.client.get(url, get_data, **kwargs)
        data = json.loads(gene_entries_response.content)

        self.assertEqual(len(data), 0)

    def test_api_autofill_options_null(self):
        kwargs = {'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'}
        url = reverse('get_autcomplete')
        get_data = {'term': 'ZZXXXAA123'}
        autocomplete_response = self.client.get(url, get_data, **kwargs)
        data = json.loads(autocomplete_response.content)

        self.assertEqual(len(data), 0)

class HomePageTests(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')