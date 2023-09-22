# grpc_bank
Customer/client processes are able to interact with a bank branch by making remote procedure calls to a branch for getting the current balance, depositing or withdrawing. 
Communication is implemented using Google Protobufs. Deposits and withdrawals must be propagated by the branch to all other branches in the system so that the consistency 
can be maintained. The internal branch-to-branch communication can also be achieved by using remote procedure calls with gRPC. 
Read your Write and Monotonic Write consistency in the distributed system are implemented, with respect to the replicated balance in each branch. Both customer and branches 
maintain a set of write operations. When the customer sends a request to a branch the set of write operations is sent as well. The branch compares this set with its’ own 
set and uses this to enforce client-centric consistency, by waiting for write-operations the customer sent to other branches that have not been propagated yet.
A couple simplifications are made to limit the scope of the project: 
•	Assume no concurrent changes by customers 
•	relationship between customers and branches 
 
Diagram: The customer changes the branches while submitting request to the Bank

<img width="363" alt="image" src="https://github.com/Light-JH/grpc_bank/assets/68739569/de6eae2d-5b6e-45bd-b07f-c8d834e06c33">

