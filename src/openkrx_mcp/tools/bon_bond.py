from mcp.server.fastmcp import FastMCP

from openkrx_mcp.client import OpenKrxClient, format_response


def register_tools(mcp: FastMCP, client: OpenKrxClient):
    @mcp.tool()
    async def get_kts_bond_daily(basDd: str) -> str:
        """국채전문유통시장(KTS) 일별매매정보를 조회합니다.

        Args:
            basDd: 기준일자 (YYYYMMDD)
        """
        data = await client.get("bon/kts_bydd_trd", {"basDd": basDd})
        return format_response(data)

    @mcp.tool()
    async def get_general_bond_daily(basDd: str) -> str:
        """일반채권시장 일별매매정보를 조회합니다.

        Args:
            basDd: 기준일자 (YYYYMMDD)
        """
        data = await client.get("bon/bnd_bydd_trd", {"basDd": basDd})
        return format_response(data)

    @mcp.tool()
    async def get_small_bond_daily(basDd: str) -> str:
        """소액채권시장 일별매매정보를 조회합니다.

        Args:
            basDd: 기준일자 (YYYYMMDD)
        """
        data = await client.get("bon/smb_bydd_trd", {"basDd": basDd})
        return format_response(data)
