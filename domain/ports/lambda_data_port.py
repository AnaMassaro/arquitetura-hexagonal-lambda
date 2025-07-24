from abc import ABC, abstractmethod


class LambdaDataPort(ABC):
    @abstractmethod
    def get_runtime(self, lambda_name: str) -> str:
        pass
