#!/usr/bin/env python
#coding: utf-8

from distutils.util import strtobool

agent = {}
agent['agent']  = {'victory':0.0,'deffence':0.0,'countV':0.0,'countD':0.0}
agent['LR']     = {'victory':0.0,'deffence':0.0,'countV':0.0,'countD':0.0}
agent['random'] = {'victory':0.0,'deffence':0.0,'countV':0.0,'countD':0.0}
agent['mid']    = {'victory':0.0,'deffence':0.0,'countV':0.0,'countD':0.0}

with open('log.txt','r') as f :
	for line in f:
		word = line.split(",")
		word[2] = strtobool(word[2].split("\n")[0])
		if word[2] : agent[word[0]]['victory']  += 1.0
		else 			 : agent[word[1]]['deffence'] += 1.0
		agent[word[0]]['countV'] += 1.0
		agent[word[1]]['countD'] += 1.0

for agentName in agent.keys() :
	print '---',agentName,'---'
	print agent[agentName]
	if agent[agentName]['countV'] :
		print 'vicp =',str(agent[agentName]['victory']  / agent[agentName]['countV'])
	if agent[agentName]['countD'] :
		print 'defp =',str(agent[agentName]['deffence'] / agent[agentName]['countD'])
	print 