#!/usr/bin/env python

from __future__ import print_function
import optparse

p = optparse.OptionParser()
options, arguments = p.parse_args()
filename = 'table.csv'

if len(arguments) > 0:
  filename = arguments[0]

fmeshnumber = 4

if len(arguments) > 1:
  fmeshnumber = int(arguments[1])
  
rowsize = 128

if len(arguments) > 2:
	rowsize = int(arguments[2])
  
minenergy = 0. #MeV

if len(arguments) > 3:
  minenergy = float(arguments[3])

maxenergy = 100. #MeV

if len(arguments) > 4:
  maxenergy = float(arguments[4])
  
print('')
print('')

print('usage: ./janis2fmesh.py <input csv> <fmesh number> <rowsize> <min energy> <max energy>')
print('default                  table.csv        4           128          0           100')

print('')
print('')

with open(filename) as f:
	content = [x.strip() for x in f.readlines()]
	
ei = []
xs = []

for line in content:
	components = line.split()
	if components[0] == "Incident":
		continue
	_ei = float(components[0]) * 1e-6
	_xs = float(components[2])
	
	if _ei <= maxenergy and _ei >= minenergy:
		ei.append(_ei)
		xs.append(_xs)

print('c -------------------------------------------------------------')
print('c')
print('c Title here')
print('c')
print('FMESH%d:<p> ...' % fmeshnumber)
print('c')
print('c Reaction rate modifier table')
print('c FROM: JANIS ......')
print('c')
print('DE%d LIN' % fmeshnumber, end='')

leng = rowsize;

for r in xrange(len(ei)):
	
	if leng + 14 > rowsize:
		print('\n     ', end='')
		leng = 5
	
	print('%.7E ' % ei[r], end='')
	leng += 14

print('')
print('DF%d LIN' % fmeshnumber, end='')

leng = rowsize;

for r in xrange(len(ei)):
	
	if leng + 14 > rowsize:
		print('\n     ', end='')
		leng = 5
	
	print('%.7E ' % xs[r], end='')
	leng += 14

print('')
print('c')
print('c -------------------------------------------------------------')
print('')
print('')








		




