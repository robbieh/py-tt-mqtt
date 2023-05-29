import turntouch
import paho.mqtt.client as mqtt
import threading
import time

ttmac = ""
hass = "hass.local"
mclient = mqtt.Client(client_id="turnTouch", clean_session=True, userdata=None, protocol=mqtt.MQTTv311, transport="tcp")
mclient.connect("hass.local")

class MyHandler(turntouch.DefaultActionHandler):
    def action_north(self):
        print("up")
        mclient.connect(hass)
        mclient.publish("turntouch/press","up")
        #mclient.publish("turntouch/battery",tt.battery)
    def action_north_double_tap(self):
        print("double up")
        mclient.connect(hass)
        mclient.publish("turntouch/press","double up")
        mclient.publish("turntouch/mode","lights", retain=True)
    def action_north_hold(self):
        print("hold up")
        mclient.connect(hass)
        mclient.publish("turntouch/press","hold up")
    def action_east(self):
        print("right")
        mclient.connect(hass)
        mclient.publish("turntouch/press","right")
    def action_west(self):
        print("left")
        mclient.connect(hass)
        mclient.publish("turntouch/press","left")
    def action_south(self):
        print("down")
        mclient.connect(hass)
        mclient.publish("turntouch/press","down")
    def action_south_double_tap(self):
        print("double down")
        mclient.connect(hass)
        mclient.publish("turntouch/press","double down")
        mclient.publish("turntouch/mode","media", retain=True)
    def action_multi_north_east_west_south(self):
        print("all")
        mclient.connect(hass)
        mclient.publish("turntouch/press","all")


#print("connected to tt and mqtt")
def periodic_updates(mclient, tt):
    while True:
        global connected
        print("batt update", tt.battery)
        mclient.publish("turntouch/battery",tt.battery)
        time.sleep(600)

update_thread = None

while True:
    try:
        print("connecting")
        tt = turntouch.TurnTouch(ttmac)
        tt.handler = MyHandler()
        #if update_thread is None:
        #    update_thread = threading.Thread(target=periodic_updates, args=(mclient, tt,) )
        #    update_thread.start()
        print("listening")
        tt.listen(only_one=False)
    except turntouch.TurnTouchException:
        print("disconnected, turntouchexception")
    except KeyError:
        print("disconnected, keyerror")


