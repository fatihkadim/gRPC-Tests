import chat_pb2
import grpc

import chat_pb2
import chat_pb2_grpc


def run():
    # Sunucuya bağlan
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = chat_pb2_grpc.ChatServiceStub(channel)

        # -------------------------
        # SendMessage RPC
        # -------------------------
        message_request = chat_pb2.MessageRequest(
            username="Ahmet",
            content="Merhaba sunucu!"
        )

        message_response = stub.SendMessage(message_request)

        print("=== SendMessage ===")
        print(f"received : {message_response.received}")
        print(f"note     : {message_response.server_note}")

        # -------------------------
        # doMath RPC
        # -------------------------
        math_request = chat_pb2.mathReq(
            num1=34,
            num2=3,
            operation="toplama"
        )

        math_response = stub.doMath(math_request)

        print("\n=== doMath ===")
        print(f"Sonuç    : {math_response.final_answer}")
        print(f"received : {math_response.received}")
        print(f"note     : {math_response.note}")

        # motivation rpc
        mot_req = chat_pb2.nameReq(
            username = "Fatih"
        )
        mot_resp = stub.motivation(mot_req)
        print("\nMotivasyon")
        print(f"mesaj : {mot_resp.message}")

        # -------------------------
        # addTodo RPC
        # -------------------------
        todo1 = chat_pb2.TodoRequest(
            username="Fatih",
            task="gRPC ogrenmeye devam et"
        )
        resp1 = stub.addTodo(todo1)
        print("\n=== addTodo ===")
        print(f"saved       : {resp1.saved}")
        print(f"task_number : {resp1.task_number}")
        print(f"summary     : {resp1.summary}")

        todo2 = chat_pb2.TodoRequest(
            username="Fatih",
            task="Docker Compose ile deploy et"
        )
        resp2 = stub.addTodo(todo2)
        print(f"\nsaved       : {resp2.saved}")
        print(f"task_number : {resp2.task_number}")
        print(f"summary     : {resp2.summary}")

if __name__ == "__main__":
    run()