
import re


def ntp_servers(arg):
    """ formats and returns a block of servers for ntp.conf file """
    #      regexp: "^server "
    #      line: "{{ basesys_ntp_servers | bsysf_ntp_servers }}"
    return '\n'.join(map('server {}'.format, arg))


def ntp_server_regex(servers, server_options=[]):
    """ returns a regex line for removing unlisted servers """
    servers = map(re.escape, servers)
    if server_options:
        optstr = ' '.join(map(re.escape, server_options))
        servers = map(str('{} ' + optstr + '$').format, servers)
#        servers = map('{}$').format, servers)
    else:
        servers = map('{}$'.format, servers)

    return '^server (?!{})'.format(
        '|'.join(servers),
        )
        #'|'.join(map(re.escape, servers)),
    #    ' '.join(map(re.escape, server_options)),
    #return '^server (?!{})'.format('|'.join(map(re.escape, arg)))


class FilterModule(object):
     def filters(self):
         return {
            'bsysf_ntp_servers': ntp_servers,
            'bsysf_ntp_server_regex': ntp_server_regex,
            }
