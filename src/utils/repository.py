from abc import ABC, abstractmethod


class AbstractRepository(ABC):

    @abstractmethod
    async def get(self):
        raise NotImplementedError
