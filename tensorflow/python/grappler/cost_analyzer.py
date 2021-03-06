# Copyright 2017 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =============================================================================
"""Provides a proper python API for the symbols exported through swig."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow.python import pywrap_tensorflow as tf_wrap
from tensorflow.python.framework import errors


def GenerateCostReport(metagraph, per_node_report=False):
  """Analyze the cost of each TensorFlow op and node in the provided metagraph.

  Args:
    metagraph: An TensorFlow MetaGraphDef.
    per_node_report: by default the report contains stats aggregated on a per op
      type basis, setting per_node_report to True adds results for each
      individual node to the report.

  Returns:
    A string of cost report.
  """
  with errors.raise_exception_on_not_ok_status():
    ret_from_swig = tf_wrap.GenerateCostReport(metagraph.SerializeToString(),
                                               per_node_report)
  return ret_from_swig
