import os
import re
import winreg

def get_proxy_settings():
    proxy_settings = {}

    # Registry keys for proxy settings
    keys = [
        r'Software\Microsoft\Windows\CurrentVersion\Internet Settings',
        r'SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Internet Settings'  # For 32-bit applications on 64-bit Windows
    ]

    for key in keys:
        try:
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key, 0, winreg.KEY_READ) as reg_key:
                # Get proxy server
                proxy_server, _ = winreg.QueryValueEx(reg_key, 'ProxyServer')
                proxy_settings['server'] = proxy_server
                
                # Check if proxy is enabled
                proxy_enabled, _ = winreg.QueryValueEx(reg_key, 'ProxyEnable')
                proxy_settings['enabled'] = bool(proxy_enabled)

                # Get proxy exceptions
                proxy_exceptions, _ = winreg.QueryValueEx(reg_key, 'ProxyOverride')
                proxy_settings['exceptions'] = proxy_exceptions
                
                # Check if proxy is using autoconfiguration script
                auto_config_url, _ = winreg.QueryValueEx(reg_key, 'AutoConfigURL')
                if auto_config_url:
                    proxy_settings['auto_config_url'] = auto_config_url
                
                break  # Stop iterating if proxy settings are found
        except FileNotFoundError:
            pass  # Registry key not found

    return proxy_settings

def main():
    proxy_settings = get_proxy_settings()

    if proxy_settings['enabled']:
        print("Proxy Server:", proxy_settings['server'])
        print("Proxy Exceptions:", proxy_settings['exceptions'])
        if 'auto_config_url' in proxy_settings:
            print("Autoconfiguration URL:", proxy_settings['auto_config_url'])
    else:
        print("Proxy is not enabled.")

if __name__ == "__main__":
    main()
