class AsyncGeneratorContextManager:
    def __init__(self, async_gen):
        self.async_gen = async_gen

    async def __aenter__(self):
        return self.async_gen

    async def __aexit__(self, exc_type, exc, tb):
        await self.async_gen.aclose()

    def __aiter__(self):
        return self

    async def __anext__(self):
        return await self.async_gen.__anext__()
