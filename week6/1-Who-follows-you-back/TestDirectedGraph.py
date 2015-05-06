import unittest
from DirectedGraph import DirectedGraph
from DirectedGraph import NotStringNameOfNode


class TestDirectedGraph(unittest.TestCase):

    def setUp(self):
        self.graph = DirectedGraph()

    def test_init(self):
        self.assertIsInstance(self.graph, DirectedGraph)

    def test_add_edge(self):
        with self.assertRaises(NotStringNameOfNode):
            self.graph.add_edge(1, "aaa")
        self.graph.add_edge("aaa", "bbb")
        self.assertEqual(self.graph.gr_dict["aaa"], ["bbb"])

    def test_get_neighbors(self):
        self.assertFalse(self.graph.get_neighbors_for("aaaa"))
        self.graph.add_edge("aaa", "bbb")
        self.graph.add_edge("aaa", "cc")
        self.assertEqual(self.graph.get_neighbors_for("aaa"), ["bbb", "cc"])

    def test_path_between(self):
        self.graph.add_edge("aaa", "bbb")
        self.graph.add_edge("bbb", "cc")
        self.assertFalse(self.graph.path_between("gfd", "dsoai"))
        self.assertTrue(self.graph.path_between("aaa", "cc"))
        self.assertFalse(self.graph.path_between("cc", "bbb"))

if __name__ == "__main__":
    unittest.main()
