
from testinfra.utils.ansible_runner import AnsibleRunner
import pytest
testinfra_hosts = pytest.testinfra_hosts


# TODO - can't get ansible facts
def notest_ssh_service(Ansible, Service, TestinfraBackend):
    host = TestinfraBackend.get_hostname()
    #    svc_name = Ansible.get_variables()['basesys_ssh_service']
    var = AnsibleRunner('.molecule/ansible_inventory').get_variables(host)
    print("VAR" + str(var))
    svc_name = var['basesys_ssh_service']
    assert svc_name

    print("SVSC " + svc_name)
    svc_name = 'sshd'
    assert svc_name
    svc = Service(svc_name)
    assert svc.is_running
    assert svc.is_enabled


# TODO docker images missing which
def notest_ssh_packages(Package):
    pkg = Package('openssh-server')
    assert pkg.is_installed


def test_ssh_disable_root(Ansible, File):
    config = File('/etc/ssh/sshd_config')
    assert config.exists
    assert config.contains('^PermitRootLogin no$')


def test_ssh_disable_password(Ansible, File):
    config = File('/etc/ssh/sshd_config')
    assert config.contains('^PasswordAuthentication no$')


def test_ssh_disable_v1(Ansible, File):
    config = File('/etc/ssh/sshd_config')
    assert config.contains('^Protocol 2$')
