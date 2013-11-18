#!/usr/bin/env python2.6
"""
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Ambari Agent

"""

from resource_management import *

def hbase_service(
  name,
  action = 'start'): # 'start' or 'stop'
    
    import params
  
    role = name
    cmd = format("{daemon_script} --config {conf_dir}")
    pid_file = format("{pid_dir}/hbase-hbase-{role}.pid")
    
    daemon_cmd = None
    no_op_test = None
    
    if action == 'start':
      daemon_cmd = format("{cmd} start {role}")
      no_op_test = format("ls {pid_file} >/dev/null 2>&1 && ps `cat {pid_file}` >/dev/null 2>&1")
    elif action == 'stop':
      daemon_cmd = format("{cmd} stop {role} && rm -f {pid_file}")
  
    if daemon_cmd is not None:
      Execute ( daemon_cmd,
        not_if = no_op_test,
        user = params.hbase_user
      )
