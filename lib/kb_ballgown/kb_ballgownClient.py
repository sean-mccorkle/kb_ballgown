# -*- coding: utf-8 -*-
############################################################
#
# Autogenerated by the KBase type compiler -
# any changes made here will be overwritten
#
############################################################

from __future__ import print_function
# the following is a hack to get the baseclient to import whether we're in a
# package or not. This makes pep8 unhappy hence the annotations.
try:
    # baseclient and this client are in a package
    from .baseclient import BaseClient as _BaseClient  # @UnusedImport
except:
    # no they aren't
    from baseclient import BaseClient as _BaseClient  # @Reimport


class kb_ballgown(object):

    def __init__(
            self, url=None, timeout=30 * 60, user_id=None,
            password=None, token=None, ignore_authrc=False,
            trust_all_ssl_certificates=False,
            auth_svc='https://kbase.us/services/authorization/Sessions/Login'):
        if url is None:
            raise ValueError('A url is required')
        self._service_ver = None
        self._client = _BaseClient(
            url, timeout=timeout, user_id=user_id, password=password,
            token=token, ignore_authrc=ignore_authrc,
            trust_all_ssl_certificates=trust_all_ssl_certificates,
            auth_svc=auth_svc)

    def run_ballgown_app(self, params, context=None):
        """
        run_ballgown_app: run Ballgown app
        http://bioconductor.org/packages/release/bioc/html/ballgown.html
        :param params: instance of type "BallgownInput" (required params:
           expressionset_ref: ExpressionSet object reference
           diff_expression_matrix_set_name:
           KBaseSets.DifferetialExpressionMatrixSet name alpha_cutoff: q
           value cutoff fold_change_cutoff: fold change cutoff num_threads:
           number of threads workspace_name: the name of the workspace it
           gets saved to optional params: maximum_num_genes: used to filter
           genes in the differential expression matrix fold_scale_type: one
           of ["linear", "log2+1", "log10+1"]) -> structure: parameter
           "expressionset_ref" of type "obj_ref" (An X/Y/Z style reference),
           parameter "diff_expression_matrix_set_suffix" of String, parameter
           "alpha_cutoff" of Double, parameter "fold_change_cutoff" of
           Double, parameter "num_threads" of Long, parameter
           "workspace_name" of String, parameter "maximum_num_genes" of Long,
           parameter "fold_scale_type" of String
        :returns: instance of type "BallgownResult" (result_directory: folder
           path that holds all files generated by run_ballgown_app
           diff_expression_obj_ref: generated RNASeqDifferetialExpression
           object reference filtered_expression_matrix_ref: generated
           ExpressionMatrix object reference report_name: report name
           generated by KBaseReport report_ref: report reference generated by
           KBaseReport) -> structure: parameter "result_directory" of String,
           parameter "diff_expression_matrix_set_ref" of type "obj_ref" (An
           X/Y/Z style reference), parameter "report_name" of String,
           parameter "report_ref" of String
        """
        return self._client.call_method(
            'kb_ballgown.run_ballgown_app',
            [params], self._service_ver, context)

    def status(self, context=None):
        return self._client.call_method('kb_ballgown.status',
                                        [], self._service_ver, context)
