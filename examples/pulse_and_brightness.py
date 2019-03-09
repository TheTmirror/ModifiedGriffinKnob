#!/usr/bin/env python

import time
import sys
sys.path.insert(0, '/home/pi/Desktop/Griffin')#/pypowermate')
from pypowermate import powermate

if __name__ == '__main__':
	if len(sys.argv) != 1:
		sys.stderr.write('usage: %s <input device>\n' % sys.argv[0])
		sys.exit(1)

	p = powermate.Powermate('/dev/input/by-id/usb-Griffin_Technology__Inc._Griffin_PowerMate-event-if00')

	speed = 255
	brightness = 255
	speed_mode = True

	print("- Rotate the knob to test different pulse speeds.")
	print("- Rotate the knob while it's pushed test different brightness levels.")

	while True:
		(ts, evt, val) = p.read_event()
		if evt == powermate.Powermate.EVENT_BUTTON:
			if val == powermate.Powermate.BUTTON_UP:
				speed_mode = True
				print("Speed mode activated.")
			else:
				speed_mode = False
				print("Brightness mode activated.")
		elif evt == p.EVENT_ROTATE:
			if speed_mode:
				speed += val
				speed = min(max(speed, 0), 510)
				print("Setting pulse speed %d" % speed)
				p.set_pulse(speed)
			else:
				brightness += val
				brightness = min(max(brightness, 0), 255)
				print("Setting brightness level %d" % brightness)
				p.set_steady_led(brightness)
