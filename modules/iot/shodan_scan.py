import shodan

def shodan_lookup(ip, api_key):
    try:
        api = shodan.Shodan(api_key)
        host = api.host(ip)

        result = []
        result.append(f"IP Address     : {host.get('ip_str', 'N/A')}")
        result.append(f"Organization   : {host.get('org', 'N/A')}")
        result.append(f"Operating System: {host.get('os', 'N/A')}")
        result.append("\nOpen Ports and Services:")

        for item in host.get('data', []):
            port = item.get('port', 'N/A')
            transport = item.get('transport', 'N/A')
            product = item.get('product', 'Unknown')
            banner = item.get('data', '').strip().replace('\r', '').replace('\n', ' ')[:200]

            result.append(f"- Port {port}/{transport}: {product}")
            result.append(f"  Banner: {banner}\n")

        return "\n".join(result)

    except shodan.APIError as e:
        return f"[!] Shodan API error: {str(e)}"
    except Exception as e:
        return f"[!] Unexpected error: {str(e)}"
