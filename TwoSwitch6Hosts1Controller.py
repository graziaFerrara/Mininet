from mininet.topo import Topo
from mininet.net import Mininet
from mininet.link import TCLink

class TwoSwitch6Hosts1Controller(Topo):
    
    def build(self):
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')
        h5 = self.addHost('h5')
        h6 = self.addHost('h6')
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        self.addLink(h1, s1, cls=TCLink, delay='1ms', bw=1)
        self.addLink(h2, s1, cls=TCLink, delay='1ms', bw=1)
        self.addLink(h3, s1, cls=TCLink, delay='1ms', bw=1)
        self.addLink(h4, s2, cls=TCLink, delay='100ms', bw=1)
        self.addLink(h5, s2, cls=TCLink, delay='100ms', bw=1)
        self.addLink(h6, s2, cls=TCLink, delay='100ms', bw=1, loss=1)
        self.addLink(s1, s2, cls=TCLink)

def create_custom_topology():
    topo = TwoSwitch6Hosts1Controller()
    net = Mininet(topo)
    net.start()

    net.interact()  # This allows you to interact with the Mininet CLI

    net.stop()

if __name__ == '__main__':
    create_custom_topology()