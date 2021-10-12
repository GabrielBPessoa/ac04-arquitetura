
#!/usr/bin/env python
import pika
import sys

link = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = link.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

message = "Hello World!"
channel.basic_publish(exchange='logs', routing_key='', body=message)
print("Sent %r" % message)
link.close()