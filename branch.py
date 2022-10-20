from sre_constants import SUCCESS
import grpc
import server_pb2
import server_pb2_grpc


class Branch(server_pb2_grpc.CustomerBranchServicer):

    def __init__(self, id, balance, branches):
        # unique ID of the Branch
        self.id = id
        # replica of the Branch's balance
        self.balance = balance
        # the list of process IDs of the branches
        self.branches = branches
        # the list of Client stubs to communicate with the branches
        self.stubList = list()
        # a list of received messages used for debugging purpose
        self.recvMsg = list()
        # iterate the processID of the branches

        # TODO: students are expected to store the processID of the branches
        pass

    # TODO: students are expected to process requests from both Client and Branch
    # def MsgDelivery(self,request, context):
    def Query(self, request, context):
        return server_pb2.QueryResponse(balance = self.balance)

    def Withdraw(self, request, context):
        if request.amount <= self.balance:
            success = True
            self.balance -= request.amount
            # need to propogate branches
        else:
            success = False
        return server_pb2.WithdrawResponse(success = success)

    def Deposit(self, request, context):
        if request.amount >  0:
            success = True
            self.balance += request.amount
            # need to propogate branches
        else:
            success = False
        return server_pb2.DepositResponse(success = success)

