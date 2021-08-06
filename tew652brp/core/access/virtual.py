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
