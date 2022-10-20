import customer
import server_pb2

test_customer = customer.Customer(1, [])
test_customer.createStub()
response = test_customer.stub.Query(server_pb2.QueryRequest())
print(response)

response = test_customer.stub.Withdraw(server_pb2.WithdrawRequest(amount = 200))
print(response.success)

response = test_customer.stub.Query(server_pb2.QueryRequest())
print(response)

response = test_customer.stub.Withdraw(server_pb2.WithdrawRequest(amount = 50))
print(response.success)

response = test_customer.stub.Query(server_pb2.QueryRequest())
print(response)

response = test_customer.stub.Deposit(server_pb2.DepositRequest(amount = 100))
print(response.success)

response = test_customer.stub.Query(server_pb2.QueryRequest())
print(response)