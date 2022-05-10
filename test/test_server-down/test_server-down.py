import pytest

def test_web_has_server_down(docker_compose, nginxproxy):
    conf = nginxproxy.get_conf().decode('ASCII')
    r = nginxproxy.get("http://web.nginx-proxy.tld/port")
    assert r.status_code in [502, 503]
    # In a HiQDev fork, Docker-Gen generates only containers with exposed ports.
    # Since the `web` container is in a net "none", there are no exposed ports,
    # So the address will not even be generated.
    #assert conf.count("server 127.0.0.1 down;") == 1
