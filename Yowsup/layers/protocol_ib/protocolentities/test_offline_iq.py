from .test_ib import IbProtocolEntityTest
from .offline_ib import OfflineIbProtocolEntity
from Yowsup.structs import ProtocolTreeNode
class OfflineIbProtocolEntityTest(IbProtocolEntityTest):
    def setUp(self):
        super(OfflineIbProtocolEntityTest, self).setUp()
        self.ProtocolEntity = OfflineIbProtocolEntity
        self.node.addChild(ProtocolTreeNode("offline", {"count": "5"}))