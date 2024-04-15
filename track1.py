# Path: coding-challenge-racer/extract_svg_path
import os.path

import pygame

name = 'track1.svg'
background = pygame.image.load(os.path.splitext(__file__)[0] + '.jpg')
resolution = 0.1
lines = [
  (69.459796, 25.95779),
  (69.459796, 25.95779),
  (73.331953, 25.384138),
  (75.913391, 23.137331),
  (76.200217, 20.173458),
  (74.38365, 16.588128),
  (68.790535, 13.385233),
  (61.763288, 10.803795),
  (40.012285, 5.258484),
  (20.269067, 2.007785),
  (13.146211, 3.298504),
  (10.277946, 6.501399),
  (10.564773, 8.891619),
  (13.624255, 9.799902),
  (31.025057, 9.513076),
  (40.107893, 10.851599),
  (42.402505, 12.429145),
  (43.645419, 15.823257),
  (43.262984, 19.21737),
  (41.016177, 21.559785),
  (38.76937, 22.515873),
  (7.9833352, 25.718768),
  (4.876049, 27.678749),
  (3.5853302, 31.16847),
  (4.3502006, 34.180148),
  (6.6448119, 36.37915),
  (10.516968, 37.048412),
  (24.141223, 35.805497),
  (28.34801, 36.618172),
  (38.434739, 43.5498104),
  (41.685439, 44.219072),
  (46.274661, 43.5976148),
  (60.998417, 38.3391305),
  (68.694926, 36.952803),
  (70.989537, 37.717673),
  (78.112393, 42.1156783),
  (82.127963, 43.1195707),
  (87.338643, 42.4025047),
  (90.923973, 39.2952186),
  (91.497626, 35.996715),
  (89.633254, 34.227952),
  (84.087943, 33.845517),
  (38.0045, 33.941126),
  (33.941126, 32.506993),
  (32.028949, 30.4036),
  (32.506993, 28.204597),
  (35.805497, 26.531443),
  (41.446417, 25.766573),
]
