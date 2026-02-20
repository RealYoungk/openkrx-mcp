from mcp.server.fastmcp import FastMCP

from openkrx_mcp.client import OpenKrxClient, format_response


def register_tools(mcp: FastMCP, client: OpenKrxClient):
    @mcp.tool()
    async def get_oil_market_daily(basDd: str) -> str:
        """석유시장 일별매매정보를 조회합니다.

        Args:
            basDd: 기준일자 (YYYYMMDD)
        """
        data = await client.get("gen/oil_bydd_trd", {"basDd": basDd})
        return format_response(data)

    @mcp.tool()
    async def get_gold_market_daily(basDd: str) -> str:
        """금시장 일별매매정보를 조회합니다.

        Args:
            basDd: 기준일자 (YYYYMMDD)
        """
        data = await client.get("gen/gold_bydd_trd", {"basDd": basDd})
        return format_response(data)

    @mcp.tool()
    async def get_emissions_market_daily(basDd: str) -> str:
        """배출권시장 일별매매정보를 조회합니다.

        Args:
            basDd: 기준일자 (YYYYMMDD)
        """
        data = await client.get("gen/ets_bydd_trd", {"basDd": basDd})
        return format_response(data)
