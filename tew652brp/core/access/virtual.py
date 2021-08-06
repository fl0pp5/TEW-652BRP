import xml.etree.ElementTree as ET


class VServerInfo:
    __slots__ = ('name', 'internal_ip', 'enabled', 'protocol', 'public_port', 'private_port')

    def __init__(self, name, internal_ip, enabled, protocol, public_port, private_port):
        self.name = name
        self.internal_ip = internal_ip
        self.enabled = enabled
        self.protocol = protocol
        self.public_port = public_port
        self.private_port = private_port

    def __str__(self):
        return f'name: {self.name} | ' \
               f'ip: {self.internal_ip} | ' \
               f'enabled: {self.enabled} | ' \
               f'protocol: {self.protocol} | ' \
               f'public_port: {self.public_port} | ' \
               f'private_port: {self.private_port}'


class Parser:
    nodes = {
        'name': 'vsRule_VirtualServerName_',
        'internal_ip': 'vsRule_InternalIPAddr_',
        'enabled': 'vsRule_Enable_',
        'protocol': 'vsRule_Protocol_',
        'public_port': 'vsRule_PublicPort_',
        'private_port': 'vsRule_PrivatePort_',
    }

    keys = nodes.keys()
    values = nodes.values()

    @staticmethod
    def find_all_virtual_servers(xml):
        return ET.fromstring(xml).findall('IGD_WANDevice_i_VirServRule_i_')

    @staticmethod
    def extract(xml):
        return VServerInfo(**{key: xml.find(node).text for key, node in zip(Parser.keys, Parser.values)})


def _get_servers(session, url):
    data = {
        'ccp_act': 'get',
        'num_inst': '1',
        'oid_1': 'IGD_WANDevice_i_VirServRule_i_',
        'inst_1': '11000',
    }
    return session.post(url, data=data).text


def get_virtual_server_list(session, url):
    xml = _get_servers(session, url)
    servers = Parser.find_all_virtual_servers(xml)
    return [Parser.extract(server) for server in servers]

