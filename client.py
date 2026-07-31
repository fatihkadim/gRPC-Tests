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

if __name__ == "__main__":
    run()