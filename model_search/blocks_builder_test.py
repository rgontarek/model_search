# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Tests for model_search.blocks_builder."""

from model_search import blocks_builder
import tensorflow.compat.v2 as tf


class BlocksBuilderTest(tf.test.TestCase):

  def test_constructor(self):
    blocks = blocks_builder.Blocks()
    input_tensor = tf.zeros([3, 32, 32, 3])
    block_type = blocks_builder.BlockType.FIXED_CHANNEL_CONVOLUTION_16
    _ = blocks[block_type].build([input_tensor], is_training=True)

  def test_all_blocks_are_there(self):
    blocks = blocks_builder.Blocks()
    for block_type in blocks_builder.BlockType:
      if block_type == blocks_builder.BlockType.EMPTY_BLOCK:
        continue
      blocks[block_type]  # pylint: disable=pointless-statement


if __name__ == "__main__":
  tf.enable_v2_behavior()
  tf.test.main()
