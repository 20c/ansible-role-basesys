
# Ansible Role for configuring the base system

[![Travis CI](https://img.shields.io/travis/20c/ansible-role-basesys.svg?maxAge=3600)](https://travis-ci.org/20c/ansible-role-basesys)
[![Requires.io](https://img.shields.io/requires/github/20c/ansible-role-basesys.svg?maxAge=3600)](https://requires.io/github/20c/ansible-role-basesys/requirements)

An Ansible role for managing base system configuration


## Role Variables

```yml
# set to false to disable timezone management
basesys_timezone: "{{ timezone | d(False) }}"


#basesys_ntp_servers: []
basesys_ntp: "{{ basesys_ntp_servers | d(False) }}"
basesys_ntp_packages: [ntp]
basesys_ntp_package_state: latest
basesys_ntp_service: ntpd
basesys_ntp_config_file: /etc/ntp.conf
basesys_ntp_server_options: []


# set to true to enable ssh management
basesys_ssh: false

# set to false to not manage ssh packages
basesys_ssh_manage_package: true
basesys_ssh_packages: [openssh-server]
basesys_ssh_package_state: latest
basesys_ssh_service: sshd

# disable root login
basesys_ssh_disable_root: true
# disable password login
basesys_ssh_disable_password: true
# disable protocol version 1
basesys_ssh_disable_v1: true


# list of group dicts to add, false to disable group management
#
# basesys_groups:
#   - name: "{{ item.name }}"
#     gid: "{{ item.gid | d(omit) }}"
#     state: "{{ item.state | d(omit) }}"
#     system: "{{ item.system | d(omit) }}"
basesys_groups: false


# list of user dicts to add, false to disable user management
#
# basesys_users:
#   - name: "{{ item.name }}"
#     password: "{{ item.password | d(omit) }}"
#     comment: "{{ item.comment | d(omit) }}"
#     uid: "{{ item.uid | d(omit) }}"
#     home: "{{ item.home | d(omit) }}"
#     group: "{{ item.group | d(omit) }}"
#     groups: "{{ ','.join(item.groups | d([])) }}"
#     shell: "{{ item.shell | d(omit) }}"
#     state: "{{ item.state | d(omit) }}"
#     system: "{{ item.system | d(omit) }}"
basesys_users: false
```


## Example Playbook

```yml
  - hosts: servers
    roles:
      - role: basesys
        basesys_timezone: UTC
        basesys_ntp_servers:
          - 0.pool.ntp.org
          - 1.pool.ntp.org
          - 2.pool.ntp.org
          - 3.pool.ntp.org
        basesys_ntp_server_options:
          - iburst


```


### License

Copyright 2016 20C, LLC

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this softare except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and


## Author Information

https://github.com/20c/ansible-role-basesys

