import argparse
import os
import sys

from mcp.server.fastmcp import FastMCP

from openkrx_mcp.client import OpenKrxClient
from openkrx_mcp.tools import (
    bon_bond,
    drv_derivatives,
    esg_sustainability,
    etp_securities,
    gen_commodities,
    idx_index,
    sto_stock,
)


def create_server(api_key: str, host: str = "0.0.0.0", port: int = 8000) -> FastMCP:
    mcp = FastMCP(
        "OpenKRX",
        instructions=(
            "OpenKRX MCP 서버는 한국거래소(KRX) Open API를 제공합니다. "
            "주식, 채권, 파생상품, ETF/ETN/ELW, 지수, 일반상품(금/석유/배출권), "
            "ESG 관련 일별 시세 및 종목 기본정보를 조회할 수 있습니다. "
            "모든 데이터는 2010년 이후 일별 데이터이며, 매일 오전 8시(KST)에 갱신됩니다. "
            "날짜 파라미터(basDd)는 YYYYMMDD 형식입니다."
        ),
        host=host,
        port=port,
    )
    client = OpenKrxClient(api_key)

    idx_index.register_tools(mcp, client)
    sto_stock.register_tools(mcp, client)
    etp_securities.register_tools(mcp, client)
    bon_bond.register_tools(mcp, client)
    drv_derivatives.register_tools(mcp, client)
    gen_commodities.register_tools(mcp, client)
    esg_sustainability.register_tools(mcp, client)

    return mcp


def main():
    parser = argparse.ArgumentParser(description="OpenKRX MCP Server")
    parser.add_argument("--api-key", default=os.environ.get("KRX_API_KEY", ""))
    parser.add_argument(
        "--transport",
        default=os.environ.get("MCP_TRANSPORT", "stdio"),
        choices=["stdio", "sse", "streamable-http"],
    )
    parser.add_argument("--host", default=os.environ.get("HOST", "0.0.0.0"))
    parser.add_argument("--port", type=int, default=int(os.environ.get("PORT", "8000")))
    args = parser.parse_args()

    if not args.api_key:
        print("Error: KRX_API_KEY 환경변수 또는 --api-key 인자가 필요합니다.", file=sys.stderr)
        sys.exit(1)

    server = create_server(args.api_key, host=args.host, port=args.port)
    server.run(transport=args.transport)


if __name__ == "__main__":
    main()
