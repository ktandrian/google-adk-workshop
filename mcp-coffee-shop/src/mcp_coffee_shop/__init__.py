from .server import serve


def main():
    """MCP Coffee Shop"""
    import argparse
    import asyncio

    parser = argparse.ArgumentParser(
        description="give a model the ability to run a function"
    )

    _ = parser.parse_args()
    asyncio.run(serve())
