import unittest
from scapy.layers.inet import IP
from scapy.layers.l2 import Ether
from scapy.packet import Raw
from packetcapture import is_critical_security_risk

class TestPacketCapture(unittest.TestCase):
    def test_is_critical_security_risk(self):
        # Create a mock packet with a Raw layer containing a suspicious string
        mock_packet = Ether()/IP()/Raw(load="username")

        # Call the is_critical_security_risk function with the mock packet
        result = is_critical_security_risk(mock_packet)

        # Check if the function correctly identified the packet as a critical security risk
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()