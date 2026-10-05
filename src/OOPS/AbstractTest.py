from abc import ABC, abstractmethod

class AbstractTest(ABC):
    @abstractmethod
    def test_method(self):
        pass

    