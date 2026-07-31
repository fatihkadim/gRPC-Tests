import chat_pb2
import grpc
from concurrent import futures

import chat_pb2
import chat_pb2_grpc


class ChatServiceServicer(chat_pb2_grpc.ChatServiceServicer):
    def SendMessage(self, request, context):
        # request: istemciden gelen MessageRequest nesnesi
        print(f"[Sunucu] {request.username} dedi ki: {request.content}")

        # MessageResponse nesnesini oluşturup geri döndürüyoruz
        return chat_pb2.MessageResponse(
            received=True,
            server_note=f"Mesajın alındı, {request.username}!"
        )

    def doMath(self, request, context):

        if request.operation == "toplama":
            result = request.num1 + request.num2

        elif request.operation == "cikarma":
            result = request.num1 - request.num2

        elif request.operation == "bolme":
            result = request.num1 / request.num2

        elif request.operation == "carpma":
            result = request.num1 * request.num2

        else:
            context.abort(grpc.StatusCode.INVALID_ARGUMENT, "Geçersiz işlem")

        return chat_pb2.mathResp(
            final_answer=result,
            received=True,
            note=f"{request.num1} {request.operation} {request.num2} = {result}"
        )

    def motivation(self, request, context):
        message = f"Muhtesem bir insansın ama malsın. {request.username}"
        return chat_pb2.nameResp(
            received = True,
            message = message
        )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    chat_pb2_grpc.add_ChatServiceServicer_to_server(
        ChatServiceServicer(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    print("Sunucu 50051 portunda dinliyor...")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()