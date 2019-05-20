# encoding=utf-8

import sys

sys.path.insert(0, "..")

import time
import OPCUA.mock_data as mock_data

from opcua import ua, Server

if __name__ == "__main__":
    # setup our server
    server = Server()
    server.set_endpoint("opc.tcp://0.0.0.0:8002/freeopcua/server/")

    # setup our own namespace, not really necessary but should as spec
    uri = "http://examples.freeopcua.github.io"
    idx = server.register_namespace(uri)

    # get Objects node, this is where we should put our nodes
    objects = server.get_objects_node()

    # populating our address space
    myobj = objects.add_object(idx, "MyObject")
    myvar = myobj.add_variable(idx, "MyVariable", 6.7)
    myvar.set_writable()  # Set MyVariable to be writable by clients

    temp_sensor = objects.add_object(nodeid=idx, bname='Temperature')
    temp_sensor_interval = temp_sensor.add_variable(idx, "TempInterval", 5)
    temp_sensor_data = temp_sensor.add_variable(idx, "TempData", mock_data.get_temp())
    temp_sensor_interval.set_writable()
    # starting!
    server.start()
    server.historize_node_data_change(myvar, period=None, count=100)

    try:
        count = 0
        while True:
            nextInterval = float(temp_sensor_interval.get_value())
            time.sleep(nextInterval)
            count += 0.1
            myvar.set_value(count)
            temp_sensor_data.set_value(mock_data.get_temp())
    finally:
        # close connection, remove subcsriptions, etc
        server.stop()
