import grpc
import glossary_pb2
import glossary_pb2_grpc


channel = grpc.insecure_channel("localhost:50051")
stub = glossary_pb2_grpc.GlossaryServiceStub(channel)

stub.CreateTerm(
    glossary_pb2.CreateTermRequest(
        keyword="API",
        description="Application Programming Interface"
    )
)

term = stub.GetTerm(
    glossary_pb2.GetTermRequest(keyword="API")
)
print(term)

terms = stub.GetTerms(glossary_pb2.Empty())
print(terms)

stub.UpdateTerm(
    glossary_pb2.UpdateTermRequest(
        keyword="API",
        description="Updated description"
    )
)

stub.DeleteTerm(
    glossary_pb2.DeleteTermRequest(keyword="API")
)
