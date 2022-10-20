import branch
import server_pb2_grpc
import grpc
from concurrent import futures

test_branch = branch.Branch(1, 100, [])

port = 50051
server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
server_pb2_grpc.add_CustomerBranchServicer_to_server(test_branch, server)
server.add_insecure_port('[::]:' + str(port))
server.start()
server.wait_for_termination()
