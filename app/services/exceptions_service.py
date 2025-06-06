import random
from typing import List
from fastapi import HTTPException


class ExceptionsService:
    def throw_random_exception(self) -> None:
        # raise a random http exception with a funny message
        exceptions: List[HTTPException] = [
            HTTPException(code, msg)
            for code, msg in [
                (400, "Bad Request: Your request is like a bad joke, nobody gets it."),
                (401, "Unauthorized: You need a secret handshake to access this."),
                (403, "Forbidden: Even the door is locked, and the key is lost."),
                (404, "Not Found: This endpoint is playing hide and seek."),
                (
                    405,
                    "Method Not Allowed: You tried to use the wrong key on the door.",
                ),
                (
                    408,
                    "Request Timeout: Your request took too long, did you fall asleep?",
                ),
                (
                    500,
                    "Internal Server Error: Something broke inside, but we don't know what.",
                ),
            ]
        ]

        raise random.choice(exceptions)
