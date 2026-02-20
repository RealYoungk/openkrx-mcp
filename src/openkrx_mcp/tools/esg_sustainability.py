from mcp.server.fastmcp import FastMCP

from openkrx_mcp.client import OpenKrxClient, format_response


def register_tools(mcp: FastMCP, client: OpenKrxClient):
    @mcp.tool()
    async def get_sri_bond_info(basDd: str) -> str:
        """사회적책임투자(SRI) 채권 정보를 조회합니다.

        Args:
            basDd: 기준일자 (YYYYMMDD)
        """
        data = await client.get("esg/sri_bond_info", {"basDd": basDd})
        return format_response(data)

    @mcp.tool()
    async def get_esg_etp_info(basDd: str) -> str:
        """ESG ETP 정보를 조회합니다.

        Args:
            basDd: 기준일자 (YYYYMMDD)
        """
        data = await client.get("esg/esg_etp_info", {"basDd": basDd})
        return format_response(data)

    @mcp.tool()
    async def get_esg_index_info(basDd: str) -> str:
        """ESG 지수 정보를 조회합니다.

        Args:
            basDd: 기준일자 (YYYYMMDD)
        """
        data = await client.get("esg/esg_index_info", {"basDd": basDd})
        return format_response(data)
