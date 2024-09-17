def apConfig(ssid, pwd, auth):
    import network
    ap_if = network.WLAN(network.AP_IF)
    ap_if.active(True)
    ap_if.config(essid=ssid, password=pwd, authmode= auth)
    while not ap_if.active():
        pass
    print('network config:', ap_if.ifconfig())
    

