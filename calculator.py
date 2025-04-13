from typing import Union
from mcp.server.fastmcp import FastMCP

# MCPサーバー初期化
mcp = FastMCP("calculator")

@mcp.tool()
async def add(a: Union[int, float], b: Union[int, float]) -> str:
    """足し算"""
    result = float(a + b)
    return f"[MCP計算] {a} + {b} = {result}"

@mcp.tool()
async def subtract(a: Union[int, float], b: Union[int, float]) -> str:
    """引き算"""
    result = float(a - b)
    return f"[MCP計算] {a} - {b} = {result}"

@mcp.tool()
async def multiply(a: Union[int, float], b: Union[int, float]) -> str:
    """掛け算"""
    result = float(a * b)
    return f"[MCP計算] {a} × {b} = {result}"

@mcp.tool()
async def divide(a: Union[int, float], b: Union[int, float]) -> str:
    """割り算を"""
    if b == 0:
        raise ZeroDivisionError("0で割ることはできません")
    result = float(a / b)
    return f"[MCP計算] {a} ÷ {b} = {result}"

if __name__ == "__main__":
    # サーバー起動
    mcp.run(transport='stdio')
