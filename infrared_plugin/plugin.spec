---
# This file and main.yml are required by Infrared project
config:
  plugin_type: other
  entry_point: main.yml
  roles_path: ../
subparsers:
  openstack-ansible-os_tempest:
    description: An ansible role for running tempest framework.
    include_groups: ["Ansible options", "Common options"]
    groups:
      - title: os_tempest
        options:

