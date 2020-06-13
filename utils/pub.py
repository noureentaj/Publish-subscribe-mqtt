import utils.publisher as pub

def publish(topic,value):
    p = pub.Publish(topic,value)
    p.connect()
    p.publish()

