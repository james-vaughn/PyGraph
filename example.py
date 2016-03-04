from pyGraph import PyGraph

test = PyGraph(4)
print("Initially...")
test.printGraph()

print("\nAfter connecting some nodes...")
test.connectAToB(0,2)
test.connectNodes(2,3)
test.connectNodes(3,1)
test.printGraph()

print("\n Is V1 connected to V3? {}".format(test.isConnected(3,2)))
print("\n Is V1 connected to V4? {}".format(test.isConnected(1,4)))

test.disconnectNodes(2,3)
print("\n Is V1 connected to V3? {}".format(test.isConnected(2,3)))
