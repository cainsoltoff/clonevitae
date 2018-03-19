from django.db import models

class Variant(models.Model):
    # I ran code that looked at the max len of each of the char fields and added a buffer or kept it a text field if
    # flexibility seemed necessary. Some discussion with those that know the data would be able to set better guidelines
    # for field types/sizes.

    gene = models.CharField(max_length=25, null=True, blank=True)
    nucleotide_change = models.TextField(null=True, blank=True)
    protein_change = models.CharField(max_length=50, null=True, blank=True)
    other_mappings = models.TextField(null=True, blank=True)
    alias = models.TextField(null=True, blank=True)
    transcripts = models.TextField(null=True, blank=True)
    region = models.CharField(max_length=75, null=True, blank=True)
    reported_classification = models.CharField(max_length=100, null=True, blank=True) # TODO: Compress this field w/ enum or int
    inferred_classification = models.CharField(max_length=100, null=True, blank=True) # TODO: Compress this field w/ enum or int
    source = models.CharField(max_length=25, null=True, blank=True)  # TODO: Compress this field w/ enum or int
    last_evaluated = models.DateField(null=True, blank=True)
    last_updated = models.DateField(null=True, blank=True)
    url = models.TextField(null=True, blank=True)
    submitter_comment = models.TextField(null=True, blank=True)
    assembly = models.CharField(max_length=10, null=True, blank=True)
    chromosome = models.CharField(max_length=2, null=True, blank=True)
    genomic_start = models.CharField(max_length=15, null=True, blank=True)
    genomic_stop = models.CharField(max_length=15, null=True, blank=True)
    ref = models.CharField(max_length=75, null=True, blank=True)
    alt = models.CharField(max_length=100, null=True, blank=True)
    accession = models.CharField(max_length=25, null=True, blank=True)
    reported_ref = models.CharField(max_length=75, null=True, blank=True)
    reported_alt = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        """String representation"""
        return "%s / %s / %s" % (self.gene, self.nucleotide_change, self.protein_change)