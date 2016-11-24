
import pytest
testinfra_hosts = pytest.testinfra_hosts


def test_ntp_servers(Ansible, File):
    config = File('/etc/ntp.conf')
    assert config.exists
    assert config.contains('^server 0.pool.ntp.org iburst')
