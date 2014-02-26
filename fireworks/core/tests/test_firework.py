#!/usr/bin/env python

"""
TODO: Modify unittest doc.
"""

from __future__ import division

__author__ = "Shyue Ping Ong"
__copyright__ = "Copyright 2012, The Materials Project"
__version__ = "0.1"
__maintainer__ = "Shyue Ping Ong"
__email__ = "shyuep@gmail.com"
__date__ = "2/26/14"

import unittest

from fireworks.core.firework import FireWork, Workflow, FireTaskBase
from fireworks.user_objects.firetasks.script_task import PyTask


class WorkflowTest(unittest.TestCase):

    def test_init(self):

        fws = []
        for i in xrange(5):
            fw = FireWork([PyTask(func="print", args=[i])], fw_id=i)
            fws.append(fw)
        wf = Workflow(fws, links_dict={0: [1, 2, 3], 1: [4], 2: [4]})
        self.assertIsInstance(wf, Workflow)
        self.assertRaises(ValueError, Workflow, fws,
                          links_dict={0: [1, 2, 3], 1: [4], 100: [4]})
        self.assertRaises(ValueError, Workflow, fws,
                          links_dict={0: [1, 2, 3], 1: [4], 2: [100]})


if __name__ == '__main__':
    unittest.main()
