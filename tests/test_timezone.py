
import pytest
testinfra_hosts = pytest.testinfra_hosts


def test_localtime_linked(Ansible, File):
    local = File('/etc/localtime')
    assert local.is_symlink

    # check against UTC content, since distros link differently
    utc = File('/usr/share/zoneinfo/UTC')
    assert utc.sha256sum == local.sha256sum
