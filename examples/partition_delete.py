#!/usr/bin/env python

from __future__ import print_function

import pyslurm

partition = "mark"
try:
    pyslurm.slurm_delete_partition(partition)
except ValueError as e:
    print("Partition ({0}) delete failed - {1}".format(partition, e.args[0]))
else:
    print("Partition ({0}) deleted".format(partition))
