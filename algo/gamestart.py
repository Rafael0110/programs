#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
with open('log.txt','a') as f :
  f.write('start,{}'.format(sys.argv[1]))
  f.flush()