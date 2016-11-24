
from testinfra.utils.ansible_runner import AnsibleRunner
testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def pytest_namespace():
    return {'testinfra_hosts': testinfra_hosts}
