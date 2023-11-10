from mininet.topo import Topo
from mininet.net import Mininet
from mininet.link import TCLink

# Create a simple topology with 2 hosts and 1 switch. 
# The links between h1-s1 and h2-s2 have different features in terms of delay, bw,  ptk loss
class TwoSwitch4Hosts(Topo):
    def build(self):
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        self.addLink(h1, s1, cls=TCLink, delay='10ms', bw=1, loss=2)
        self.addLink(h2, s1, cls=TCLink, delay='100ms', bw=1)
        self.addLink(h3, s2, cls=TCLink)
        self.addLink(h4, s2, cls=TCLink)
        self.addLink(s1, s2, cls=TCLink)

def create_custom_topology():
    topo = TwoSwitch4Hosts()
    net = Mininet(topo)
    net.start()
    
    net.interact()  # This allows you to interact with the Mininet CLI

    net.stop()

if __name__ == '__main__':
    create_custom_topology()
