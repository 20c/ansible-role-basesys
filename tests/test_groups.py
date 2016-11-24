
import pytest
testinfra_hosts = pytest.testinfra_hosts


def test_groups_exist(Ansible, File):
    config = File('/etc/group')
    assert config.exists
    assert config.contains('^testplain:')
    assert config.contains('^testsudo:')
    assert config.contains('^testsudonp:')


def test_groups_sudoers(Ansible, File):
    config = File('/etc/sudoers')
    assert config.exists
    assert not config.contains('^%testplain ')
    assert config.contains('^%testsudo ALL=(ALL) ALL$')
    assert config.contains('^%testsudonp ALL=(ALL) NOPASSWD: ALL$')
