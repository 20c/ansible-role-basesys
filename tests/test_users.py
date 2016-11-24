
import pytest
testinfra_hosts = pytest.testinfra_hosts


def test_groups_exist(Ansible, File):
    config = File('/etc/passwd')
    assert config.exists
    assert config.contains('^testuser:')
