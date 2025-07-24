from abc import ABC, abstractmethod


class InputEventPort(ABC):
    @abstractmethod
    def parse(self, event: dict) -> list[str]:
        pass

