from concurrent import futures
import grpc
from grpc_reflection.v1alpha import reflection
import glossary_pb2
import glossary_pb2_grpc

from database import SessionLocal, Base, engine
import crud

Base.metadata.create_all(bind=engine)


class GlossaryService(glossary_pb2_grpc.GlossaryServiceServicer):

    def GetTerms(self, request, context):
        db = SessionLocal()
        terms = crud.get_terms(db)
        db.close()

        return glossary_pb2.TermsList(
            terms=[
                glossary_pb2.Term(
                    keyword=t.keyword,
                    description=t.description
                )
                for t in terms
            ]
        )

    def GetTerm(self, request, context):
        db = SessionLocal()
        term = crud.get_term_by_keyword(db, request.keyword)
        db.close()

        if not term:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Term not found")
            return glossary_pb2.Term()

        return glossary_pb2.Term(
            keyword=term.keyword,
            description=term.description
        )

    def CreateTerm(self, request, context):
        db = SessionLocal()

        existing = crud.get_term_by_keyword(db, request.keyword)
        if existing:
            db.close()
            context.set_code(grpc.StatusCode.ALREADY_EXISTS)
            context.set_details("Term already exists")
            return glossary_pb2.Term()

        term = crud.create_term(
            db,
            keyword=request.keyword,
            description=request.description
        )

        db.close()

        return glossary_pb2.Term(
            keyword=term.keyword,
            description=term.description
        )

    def UpdateTerm(self, request, context):
        db = SessionLocal()
        term = crud.get_term_by_keyword(db, request.keyword)

        if not term:
            db.close()
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Term not found")
            return glossary_pb2.Term()

        term = crud.update_term(
            db,
            db_term=term,
            description=request.description
        )

        db.close()

        return glossary_pb2.Term(
            keyword=term.keyword,
            description=term.description
        )

    def DeleteTerm(self, request, context):
        db = SessionLocal()
        term = crud.get_term_by_keyword(db, request.keyword)

        if not term:
            db.close()
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Term not found")
            return glossary_pb2.Empty()

        crud.delete_term(db, term)
        db.close()

        return glossary_pb2.Empty()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    glossary_pb2_grpc.add_GlossaryServiceServicer_to_server(
        GlossaryService(), server
    )

    SERVICE_NAMES = (
        glossary_pb2.DESCRIPTOR.services_by_name['GlossaryService'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)

    server.add_insecure_port("[::]:50051")
    server.start()

    print("gRPC server running on port 50051 with reflection")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
