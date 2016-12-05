# Copyright 2016 Google Inc. All Rights Reserved.
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

from async_query_params import main


def test_main_use_named_params(cloud_config, capsys):
    main(use_named_params=True, corpus='romeoandjuliet', min_word_count=100)
    out, _ = capsys.readouterr()
    assert 'love' in out


def test_main_use_positional_params(cloud_config, capsys):
    main(use_named_params=False, corpus='romeoandjuliet', min_word_count=100)
    out, _ = capsys.readouterr()
    assert 'love' in out
