# -*- coding: utf-8 -*-
#BEGIN_HEADER
import os
import json

from kb_functional_enrichment_1.Utils.FunctionalEnrichmentUtil import FunctionalEnrichmentUtil
#END_HEADER


class kb_functional_enrichment_1:
    '''
    Module Name:
    kb_functional_enrichment_1

    Module Description:
    A KBase module: kb_functional_enrichment_1
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "1.0.0"
    GIT_URL = "https://github.com/Tianhao-Gu/kb_functional_enrichment_1.git"
    GIT_COMMIT_HASH = "60d0290a53d5683dccd45e484ba98eb46031b9f6"

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.config = config
        self.config['SDK_CALLBACK_URL'] = os.environ['SDK_CALLBACK_URL']
        self.config['KB_AUTH_TOKEN'] = os.environ['KB_AUTH_TOKEN']
        #END_CONSTRUCTOR
        pass


    def run_fe1(self, ctx, params):
        """
        run_fe1: run functional enrichment one
        :param params: instance of type "FEOneInput" (required params:
           genome_ref: Genome object reference workspace_name: the name of
           the workspace it gets saved to optional params: num_threads:
           number of threads) -> structure: parameter "genome_ref" of type
           "obj_ref" (An X/Y/Z style reference), parameter "workspace_name"
           of String, parameter "num_threads" of Long
        :returns: instance of type "FEOneResult" (result_directory: folder
           path that holds all files generated by run_deseq2_app report_name:
           report name generated by KBaseReport report_ref: report reference
           generated by KBaseReport) -> structure: parameter
           "result_directory" of String, parameter "report_name" of String,
           parameter "report_ref" of String
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN run_fe1
        print '--->\nRunning kb_functional_enrichment_1.run_fe1\nparams:'
        print json.dumps(params, indent=1)

        for key, value in params.iteritems():
            if isinstance(value, basestring):
                params[key] = value.strip()

        fe1_runner = FunctionalEnrichmentUtil(self.config)
        returnVal = fe1_runner.run_fe1(params)
        #END run_fe1

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method run_fe1 return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]
    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
