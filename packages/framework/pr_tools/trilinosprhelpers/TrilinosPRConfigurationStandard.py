#!/usr/bin/env python
# -*- mode: python; py-indent-offset: 4; py-continuation-offset: 4 -*-
"""
Custom PR Executor for Standard testing
"""

import os
import subprocess

from . import TrilinosPRConfigurationBase
from gen_config import GenConfig
from pathlib import Path


class TrilinosPRConfigurationStandard(TrilinosPRConfigurationBase):
    """
    Implements Standard mode Trilinos Pull Request Driver
    """
    def __init__(self, args):
        super(TrilinosPRConfigurationStandard, self).__init__(args)


    def execute_test(self):
        """
        Execute the test
        """
        print("+" + "="*78 + "+")
        print("|   E X E C U T E   S T A N D A R D   P U L L R E Q E S T   T E S T")
        print("+" + "="*78 + "+")

        #
        # Typically, we execute the test from $WORKSPACE/TFW_testing_single_configure_prototype
        # We'll skip it if we're doing a dry-run.
        #
        print("")
        print("--- Change directory to {}".format(self.working_directory_ctest))
        if not self.args.dry_run:
            os.chdir(self.working_directory_ctest)
        print("--- OK")
        print("")

        # Use GenConffig to write the configure script for cmake
        gc = GenConfig(["-y", "--force",
                        "--cmake-fragment",
                        os.path.join(self.arg_workspace_dir,
                                     self.config_script),
                        self.arg_pr_genconfig_job_name],
                       gen_config_ini_file=(Path(self.arg_pr_gen_config_file)))

        if not self.args.dry_run:
            gc.write_cmake_fragment()

        # Execute the call to ctest.
        # - NOTE: simple_testing.cmake can be found in the TFW_single_configure_support_scripts
        #         repository.
        cmd = ['ctest', '-S', 'simple_testing.cmake',
                      '-Dbuild_name={}'.format(self.pullrequest_build_name),
                      '-Dskip_by_parts_submit=OFF',
                      '-Dskip_update_step=ON',
                      '-Ddashboard_model=Experimental',
                      '-Ddashboard_track={}'.format(self.arg_pullrequest_cdash_track),
                      '-DPARALLEL_LEVEL={}'.format(self.concurrency_build),
                      '-DTEST_PARALLEL_LEVEL={}'.format(self.concurrency_test),
                      '-Dbuild_dir={}/pull_request_test'.format(self.arg_workspace_dir),
                      '-Dconfigure_script=' +
                          os.path.join(self.arg_workspace_dir,
                                       self.config_script),
                      '-Dpackage_enables=' + self.arg_filename_packageenables,
                      '-Dsubprojects_file=' + self.arg_filename_subprojects
                    ]

        print("--- ctest command:")
        print("--- cmd = {}".format(" \\\n   ".join(cmd)))
        print("")

        if not self.args.dry_run:
            try:
                subprocess.check_call(cmd, env=os.environ)
                # Note: check_call will throw an exception if there's a problem.
            except:
                print("--- ctest command failed!")
                return 1
        else:
            print("--- SKIPPED DUE TO DRYRUN")
        print("")

        return 0




