from mcp.server.fastmcp import FastMCP

from openkrx_mcp.client import OpenKrxClient, format_response


def register_tools(mcp: FastMCP, client: OpenKrxClient):
    @mcp.tool()
    async def get_etf_daily(basDd: str) -> str:
        """ETF 일별매매정보를 조회합니다.

        Args:
            basDd: 기준일자 (YYYYMMDD)
        """
        data = await client.get("etp/etf_bydd_trd", {"basDd": basDd})
        return format_response(data)

    @mcp.tool()
    async def get_etn_daily(basDd: str) -> str:
        """ETN 일별매매정보를 조회합니다.

        Args:
            basDd: 기준일자 (YYYYMMDD)
        """
        data = await client.get("etp/etn_bydd_trd", {"basDd": basDd})
        return format_response(data)

    @mcp.tool()
    async def get_elw_daily(basDd: str) -> str:
        """ELW 일별매매정보를 조회합니다.

        Args:
            basDd: 기준일자 (YYYYMMDD)
        """
        data = await client.get("etp/elw_bydd_trd", {"basDd": basDd})
        return format_response(data)
