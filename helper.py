from clonevitae_api.models import Variant
import csv
from dateutil import parser
from datetime import datetime

def load_variant_db(filename='data/variants.tsv'):
    """
    Import the variants tsv file into the database using Variant model.
    """

    print('Starting TSV import...')

    with open(filename, encoding='Latin-1') as f:

        for counter, row in enumerate(csv.reader(f, delimiter='\t')):
            if counter == 0: continue # skip header row

            try:

                if row[0] != '':

                    row[10] = None if not row[10] else parser.parse(row[10]).strftime("%Y-%m-%d")
                    row[11] = None if not row[11] else parser.parse(row[11]).strftime("%Y-%m-%d")

                    fields = ('gene',
                            'nucleotide_change',
                            'protein_change',
                            'other_mappings',
                            'alias',
                            'transcripts',
                            'region',
                            'reported_classification',
                            'inferred_classification',
                            'source',
                            'last_evaluated',
                            'last_updated',
                            'url',
                            'submitter_comment',
                            'assembly',
                            'chromosome',
                            'genomic_start',
                            'genomic_stop',
                            'ref',
                            'alt',
                            'accession',
                            'reported_ref',
                            'reported_alt')


                    Variant.objects.create(**dict(zip(fields, row)))

                if counter % 5000 == 0:  # provide update on number of rows processed
                    print('Processed:', counter)
            except:

                print("Invalid record at ", counter)

    print('Done importing.')

